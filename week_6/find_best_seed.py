import sys
import argparse
import random
import pandas as pd
import numpy as np
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def main():
    parser = argparse.ArgumentParser(
        description="Vind de beste random seed voor het Ames Housing SGDRegressor model (gebaseerd op R-squared).")
    parser.add_argument('iterations', type=int,
                        help="Aantal keer dat het model getraind moet worden met random seeds.")
    args = parser.parse_args()

    num_iterations = args.iterations

    print("Dataset laden en voorbereiden...")
    try:
        df = pd.read_csv('AmesHousing.csv')
    except FileNotFoundError:
        print("Fout: Kan 'AmesHousing.csv' niet vinden. Zorg dat het bestand in dezelfde map staat.")
        sys.exit(1)

    df = df[df['Gr Liv Area'] < 4000].copy()
    target = 'SalePrice'
    features = [
        'Overall Qual', 'Gr Liv Area', 'Total Bsmt SF', 'Lot Area',
        'Year Built', 'Full Bath', 'Bedroom AbvGr', 'Neighborhood'
    ]

    df_subset = df[features + [target]].copy()
    df_subset.fillna(0, inplace=True)

    X = pd.get_dummies(df_subset[features], drop_first=True)
    y = np.log1p(df_subset[target])

    best_seed = None
    best_r2 = -float('inf')
    best_metrics = {}

    epochs = 4
    learning_rate = 0.005

    with tqdm(total=num_iterations, desc="Optimaliseren", unit="it") as pbar:
        for i in range(num_iterations):
            # Genereer een random seed (tussen 0 en 1.000.000)
            current_seed = random.randint(0, 1000000)

            # Splits de dataset met de nieuwe seed
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=current_seed)

            # Scaling
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Model initialiseren
            model = SGDRegressor(
                loss='squared_error',
                penalty='l2',
                alpha=0.01,
                eta0=learning_rate,
                random_state=current_seed
            )

            # Train het model
            for epoch in range(epochs):
                model.partial_fit(X_train_scaled, y_train)

            # Voorspellingen en terug transformeren naar dollars
            y_pred_log = model.predict(X_test_scaled)
            y_pred_dollars = np.expm1(y_pred_log)
            y_test_dollars = np.expm1(y_test)

            # Bereken metrics
            r2 = r2_score(y_test_dollars, y_pred_dollars)

            # Check of deze R-squared beter (hoger) is dan de beste tot nu toe
            if r2 > best_r2:
                best_r2 = r2
                best_seed = current_seed
                best_metrics = {
                    'rmse': np.sqrt(mean_squared_error(y_test_dollars, y_pred_dollars)),
                    'mae': mean_absolute_error(y_test_dollars, y_pred_dollars),
                    'r2': r2
                }

            # Update de progress bar info (postfix voegt tekst toe aan het einde van de balk)
            pbar.set_postfix({'Beste R2': f"{best_r2:.4f}"})
            pbar.update(1)

    print("\n" + "="*45)
    print(f"random_state (seed)             : {best_seed}")
    print(f"R-squared                       : {best_metrics['r2']:.4f}")
    print(f"Root Mean Squared Error (RMSE)  : ${best_metrics['rmse']:,.2f}")
    print(f"Mean Absolute Error (MAE)       : ${best_metrics['mae']:,.2f}")
    print("="*45)


if __name__ == "__main__":
    main()
