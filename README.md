# Kv-deltashare-examples

Dette er et eksempelrepo for uthenting av data gjennom delta share sikret med Maskinporten for virksomheter. 

Dersom du har vært med i uttesting av dette i pilotperioden kan du finne dokumentasjonen derfra på taggen [pilot](/tags/pilot)

## Flytdiagram

Tilgang og dataflyt sett fra konsumentsiden:

```mermaid
sequenceDiagram
    autonumber
    Consumer->>+Consumer: Create signed JWT grant
    Consumer->>+Maskinporten: signed JWT grant
    GCP-->>-Consumer: file config.share
    loop DeltaShareProtocol using config.share
        Consumer->>+Databricks: Maskinporten token
        Databricks->>-Consumer: Data
    end

```

## Kom i gang

### Manuelt førstegangsoppsett for å lage Maskinporten-token

Du trenger å opprette en Maskinporten-klient og hente nødvendige verdier som skal populere config.share. Fra Kartverket vil du få en recipient-url. 

### Hent ut share-data

Før du kjører notebooken, anbefales det å sette opp et virtuelt miljø for å isolere avhengigheter. Fra rotmappen i prosjektet kjører man:

```
python3 -m venv venv
```

_(Man trenger bare sette opp det virtuelle miljøet én gang)_

Hver man gang skal kjøre programmet må man aktivere det virtuelle miljøet:

```
source venv/bin/activate  # På macOS/Linux
venv\Scripts\activate     # På Windows
```

Man vil se at det virtuelle miljøet er aktivert ved å se at man får navnet på sitt viritiuell miljø i terminalen:

Installer nødvendige Python-pakker fra requirements.txt:

`pip3 install -r requirements.txt`


## Datamodellering



## Annet

### Oppdateringsfrekvens

Vi oppdaterer dataene en gang i døgnet pt (oppdateringsvindu = 24 timer). For matrikkeldata er kilden Matrikkelen sin endringslogg.

Dersom det er flere endringer på samme objekt innenfor oppdateringsvinduet, vil vi kun registere den siste endringen for å få korrekt oppdateringstid/endringstidspunkt.

### Versjonering

Målet er å holde dataproduktene stabile. Vilkår for delingsmekanismen er under utarbeidelse.

Generelt må konsumenter forvente at nye kolonner vil kunne legges til i eksisterende dataprodukter uten varsling. Dette må håndteres av nedstrømskonsumenter. Transaksjonsloggen i deltashare skal sørge for at nye kolonner populeres med ny data.

### FAQ

> _dim_adresse_ har noen innslag hvor `to_datetime = null`, hvordan skal vi tolke disse resultatene.

Disse adressene må behandles som gyldige adresser, tilsvarende de som har et fremtidig timestamp.

> Pandas gir meg ingen datoer frem i tid, hva skjer?

Pandas får en overflow på tid når vi bruker fremtidig dato 9999-01-01. Denne blir dermed 1815.
