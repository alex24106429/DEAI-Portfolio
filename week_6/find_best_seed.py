import sys
import argparse
import random
import pandas as pd
import numpy as np
from tqdm import tqdm
from joblib import Parallel, delayed
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def evaluate_seed(seed, X, y):
    """Worker functie die op 1 CPU core draait."""
    # Splits de dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=seed)

    # Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Model initialiseren (max_iter vervangt de Python for-loop met partial_fit)
    model = SGDRegressor(
        loss='squared_error',
        penalty='l2',
        alpha=0.01,
        eta0=0.005,
        max_iter=4,  # Zelfde als 4 epochs
        tol=None,    # Voorkomt early-stopping, dwingt exact 4 epochs af
        random_state=seed
    )

    # Train het model in C-geoptimaliseerde code in plaats van een Python loop
    model.fit(X_train_scaled, y_train)

    # Voorspellingen
    y_pred_log = model.predict(X_test_scaled)

    # Terug transformeren naar dollars
    y_pred_dollars = np.expm1(y_pred_log)
    y_test_dollars = np.expm1(y_test)

    # Bereken alleen R2 tijdens de iteraties voor maximale snelheid
    r2 = r2_score(y_test_dollars, y_pred_dollars)

    return seed, r2


def main():
    parser = argparse.ArgumentParser(
        description="Vind de beste random seed voor het Ames Housing SGDRegressor model.")
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

    # Data preppen
    X_df = pd.get_dummies(df_subset[features], drop_first=True)
    y_df = np.log1p(df_subset[target])

    # CONVERSIE NAAR NUMPY: Verwijder Pandas overhead in de loop
    X = X_df.to_numpy()
    y = y_df.to_numpy()

    # Genereer alle seeds vooraf
    seeds = [random.randint(0, 1000000) for _ in range(num_iterations)]

    best_seed = None
    best_r2 = -float('inf')

    print(
        f"Start optimalisatie over {num_iterations} iteraties met multiprocessing...")

    # Voer iteraties parallel uit op alle beschikbare CPU cores (n_jobs=-1)
    parallel_generator = Parallel(n_jobs=-1, return_as="generator")(
        delayed(evaluate_seed)(seed, X, y) for seed in seeds
    )

    # Gebruik tqdm om de generator te volgen
    with tqdm(total=num_iterations, desc="Optimaliseren", unit="it") as pbar:
        for seed, r2 in parallel_generator:
            if r2 > best_r2:
                best_r2 = r2
                best_seed = seed
                pbar.set_postfix({'Beste R2': f"{best_r2:.4f}"})
            pbar.update(1)

    # --- POST-PROCESSING ---
    # Bereken de overige metrics (RMSE, MAE) slechts 1 keer voor de winnende seed
    print("\nDefinitieve metrics berekenen voor de beste seed...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=best_seed)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    best_model = SGDRegressor(
        loss='squared_error', penalty='l2', alpha=0.01,
        eta0=0.005, max_iter=4, tol=None, random_state=best_seed
    )
    best_model.fit(X_train_scaled, y_train)

    y_pred_dollars = np.expm1(best_model.predict(X_test_scaled))
    y_test_dollars = np.expm1(y_test)

    best_rmse = np.sqrt(mean_squared_error(y_test_dollars, y_pred_dollars))
    best_mae = mean_absolute_error(y_test_dollars, y_pred_dollars)

    print("\n" + "="*45)
    print(f"random_state (seed)             : {best_seed}")
    print(f"R-squared                       : {best_r2:.4f}")
    print(f"Root Mean Squared Error (RMSE)  : ${best_rmse:,.2f}")
    print(f"Mean Absolute Error (MAE)       : ${best_mae:,.2f}")
    print("="*45)


if __name__ == "__main__":
    main()
