**DEAI-opdrachten Classificatie**

Je krijgt een dataset die bestaat uit ongeveer 3.000 huizen uit de
plaats Ames in de Amerikaanse staat Iowa. Hiermee ga je twee
classificatiemodellen maken:

-   Eentje voorspelt per huis of er wel of geen garage aanwezig is
    (binaire classificatie).

-   Eentje voorspelt per huis het kwaliteitsniveau (multi-class
    classificatie).

Per model heb je in totaal 11 features tot je beschikking.

Doorloop de onderstaande stappen twee keer, één keer per te maken model.

1.  Maak een nieuw Excelbestand, dit wordt je logboek.

2.  Maak een Jupyter Notebook waarin je het tabje "AmesHousing" van het
    bestand AmesHousing.xlsx inleest, als DataFrame in Python. Zorg
    ervoor dat elke Excel-kolom overeenkomt met een DataFrame-kolom.

3.  Open AmesHousing.xlsx in Excel en lees de inhoud van het tabje "Data
    Dictionary" goed door. Deze geeft de betekenis weer van elke feature
    én van de targetvariabele. Zoek uit in welke kolom de
    targetvariabele staat en maak een top 3 van features waarvan je
    verwacht dat die het meest voorspellend zijn voor de
    targetvariabele. Let op: minstens één van deze features moet
    categorisch zijn! Noteer de gekozen features en het target in je
    logboek.

4.  Prepareer je data in je Jupyter Notebook:

    a.  One-hot encode je uitgekozen categorische feature(s)

    b.  Splits de dataset horizontaal én verticaal, zodat er vier
        "stukken" ontstaan.

5.  Initialiseer een decision tree in je Jupyter Notebook en train deze
    op de juiste "stukken" uit stap 4b. Doe hierbij onderzoek naar de
    zogeheten "hyperparameters" die je bij dit model kan instellen met
    behulp van de pythonfunctie help(). Kies hierbij voor een
    willekeurige combinatie van minstens 2 hyperparameters. Noteer deze
    in je logboek.

6.  Evalueer je getrainde model uit stap 5 in je Jupyter Notebook met
    behulp van de juiste "stukken" uit stap 4b door verschillende
    relevante evaluatiemetrieken te (laten) berekenen. Noteer de waarden
    van deze metrieken in je logboek.

7.  Tijd om te experimenteren! Voer stappen 3 t/m 6 meerdere keren
    opnieuw uit en kijk of je je model beter kan laten presteren dan je
    "initiële run".

Experimenteer met (combinaties van):

a.  Meer/andere (aantallen) features. One-hot encode deze waar nodig.

b.  Meer/andere (aantallen) hyperparameters.

> Vul met elk van deze experimenten je Jupyter Notebook én je logboek
> aan. Gooi de code en resultaten van eerdere experimenten dus niet weg
> (hoe nutteloos zij af en toe lijken)! Code die niet werkt mag je
> uiteraard wél weggooien .

8.  Zorg ervoor dat je tijdens het portfoliogesprek kunt verantwoorden
    welke experimentresultaten jou inspireerden tot welke nieuwe
    experiment-configuraties uit stap 7 en in hoeverre deze nieuwe
    configuraties de modelprestaties verbeterden.
