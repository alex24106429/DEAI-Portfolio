**DEAI-opdrachten Datawarehouse Design**

1.  Herken de feiten (3 in totaal) en de omliggende dimensies in je
    eigen gemaakte Source Data Model van BikeToDrive (je eigen
    uitwerking van het vorige werkcollege).

2.  Maak een Sterschema, waarin de feiten met de meetwaarden in het
    midden staan en correct verbonden zijn met de omliggende dimensies.
    Vergeet ook de verborgen dimensies niet. Zorg er ten slotte voor dat
    je er van elk van de volgende onderdelen minimaal 3 hebt:

    -   Afgeleide dimensiewaarde.

    -   Afgeleide meetwaarde.

3.  Maak per tabel uit het Sterschema een ETL-schema.

Algemene tips:

-   Voor het samen kunnen tekenen van een Sterschema en bijbehorende
    ETL-schema's is "Visual Paradigm", die je in week 2 al hebt
    gebruikt, prima geschikt. Als alternatief kan je overwegen om een
    account aan te maken op [Miro](https://miro.com/), om de twee
    modellen op een gezamenlijk digitaal bord te kunnen tekenen.

-   Houd goed in de gaten dat één feit/dimensie verspreid kan zijn over
    meerdere brontabellen, dus zorg ervoor dat je de juiste brontabellen
    samenvoegt en vervolgens als één dimensie identificeert.

-   Je hoeft niet alle attributen uit de brontabel(len) over te nemen in
    je Sterschema, je mag dus keuzes maken in welke attributen je wel en
    niet opneemt. Als je dit doet: houd deze keuzes schriftelijk bij
    (bijvoorbeeld in een logboek, o.i.d.). Bij het beoordelingsmoment
    moet je namelijk kunnen toelichten waarom jij en je duopartner
    bepaalde attributen achterwege hebben gelaten ("waarom droegen ze
    volgens jullie niks bij aan de uiteindelijke rapportages?").

-   Bij het afhandelen van de zgn. "conformed dimensies", dimensies
    waaraan meerdere feiten verbonden zijn, mag je voor de
    "snowflakemethode" of de "extra-attribuut-in-feit-methode" kiezen
    (zie HC3). Je moet bij beoordelingsmomenten wel kunnen toelichten
    wat jouw keuze betekent voor de snelheid en complexiteit van je
    datawarehouse.
