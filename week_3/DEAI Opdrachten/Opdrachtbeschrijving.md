**DEAI-opdrachten Source Data Model Implementation**

1.  Zorg dat je (wederom) de volgende operationele SQLite-databronnen
    hebt (in dezelfde zip-map als deze opdrachtbeschrijving):

    a.  BikeToDrive_1_Accessoireverkoop.db

    b.  BikeToDrive_2_Fietsverkoop.db

    c.  BikeToDrive_3_Onderhoud.db

    d.  BikeToDrive_4_Accessoire_Inkoop.db

    e.  BikeToDrive_5_Fiets_Inkoop.db

2.  Maak een nieuw .db-bestand, dit wordt je uiteindelijke SDM.

3.  Maak voor de eerste twee operationele databronnen een Relationeel
    Implementatiemodel (RIM).

    a.  De onderste drie databronnen hebben al een Relationeel
        Implementatiemodel. Deze staan in dezelfde zip-map als deze
        opdrachtbeschrijving.

    b.  De bovenste twee databronnen moeten in deze opdracht nog wél
        "from scratch" gemodelleerd worden. Maar hiervoor per databron
        een nieuw .txt-bestand aan waarin je een werkend script
        schrijft.

    c.  Zorg ervoor dat je in alle nieuwe relationele
        implementatiemodellen álle tabellen, álle attributen, álle
        primaire sleutels en álle vreemde sleutels opneemt.

4.  Voordat je aan deze stap begint moet je in totaal vijf relationele
    implementatiemodellen hebben.

    a.  Voeg al deze modellen samen tot één groot script dat het
        volledige SDM aanmaakt.

    b.  Voer dit script uit in SQLite, zodat de volledige datastructuur
        geïmplementeerd wordt.

5.  Vul de tabellen van het nieuw aangemaakte Source Data Model. Schrijf
    hiervoor een script in Jupyter Notebook. Beslis bij de uitvoering
    van onderstaande stappen tijdig welk van de 4 inlaadstrategieën uit
    het hoorcollege je gebruikt.

> Je uiteindelijke Jupyter Notebook moet het volgende kunnen:

a.  Alle tabellen uit het SDM leegmaken. Dit is dus een soort
    "reset-knop" voor de invulling van je SDM-tabellen.

b.  Data van elk .db-bestand overzetten naar het Source Data Model.
    Besteed hierbij extra aandacht aan de database-overschrijdende
    associaties.

> **Naar verwachting is dit een lastige en tijdrovende stap, begin hier
> dus tijdig mee!**

6.  Test je Jupyter Notebook door in de operationele databronnen
    bepaalde wijzigingen aan te brengen (rijen toevoegen, updaten of
    verwijderen) en vervolgens te kijken of het SDM deze updates
    volledig overneemt na het uitvoeren van het Jupyter Notebook.
