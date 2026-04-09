**[Power BI verbinden met SQLite -- Handleiding]{.underline}**

1.  Download en installeer de benodigde software:

    a.  Download en installeer Power BI Desktop
        [hier](https://www.microsoft.com/en-us/download/details.aspx?id=58494).

    b.  Download en installeer SQLite-ODBC (Open Database Connectivity)
        [hier](http://ch-werner.de/sqliteodbc/sqliteodbc_w64.exe).

2.  Configureer je "ODBC gegevensbronnen" (of "ODBC Data Sources"), deze
    staat standaard op elk Windows-device:

    a.  Open deze door hiernaar te zoeken in je zoekbalk.

    b.  Klik rechts op "Toevoegen" en kies voor "SQLite3 ODBC Driver".
        Klik daarna op "Voltooien".

![A screenshot of a computer AI-generated content may be
incorrect.](media/image1.png){width="4.658333333333333in"
height="3.3364599737532807in"}

c.  Geef een betekenisvolle naam aan de databaseconnectie, bijvoorbeeld
    "SQLite_BikeToDrive_DWH" o.i.d..

d.  Kies het juiste SQLite-bestand via "Browse..." . Klik vervolgens op
    "OK", je kan de rest van de velden dus leeg laten. Als het goed is
    zie je in het hoofdmenu nu je nieuw aangebrachte connectie staan.

![A screenshot of a computer AI-generated content may be
incorrect.](media/image2.png){width="2.876768372703412in"
height="2.5248523622047245in"}

3.  Open de connectie vanuit Power BI Desktop

    a.  Open Power BI Desktop, klik op "Leeg rapport"

    b.  Klik linksboven op "Gegevens ophalen" -\> "Meer..." -\>
        "Overige" -\> "ODBC".

    c.  Kies voor de naam die je bij stap 2c hebt gegeven en klik op
        "OK".

    d.  Klik op het tabblad "Windows" en kies voor "Mijn huidige
        referenties gebruiken". Klik vervolgens op "Verbinden".

Nu zie je dat Power BI "leest" welke tabellen in de betreffende database
zitten, ten teken dat het verbinden van Power BI met SQLite met succes
is voltooid.

![A screenshot of a computer AI-generated content may be
incorrect.](media/image3.png){width="3.9138976377952757in"
height="3.815964566929134in"}

![A screenshot of a computer AI-generated content may be
incorrect.](media/image4.png){width="4.559673009623797in"
height="2.6196008311461068in"}
