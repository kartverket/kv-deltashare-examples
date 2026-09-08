# Kartverkets Delta Share Eksempler

Dette er et eksempelrepo for uthenting av data gjennom delta share sikret med Maskinporten for virksomheter. 

Dersom du har vært med i uttesting av dette i pilotperioden kan du finne gammel dokumentasjon på github taggen [pilot](/tags/pilot).

## Struktur

- [main.py](main.py) - lister tilgjengelige tabeller eller henter en tabell.
- [config/oauth_config.example.share](config/oauth_config.example.share) - mal for din lokale Delta Sharing-profil.
- [examples/](examples/) - små eksempler på uthenting og metadata.
- [docs/dataflyt.mermaid](docs/dataflyt.mermaid) - dataflyt mellom konsument, Skyporten og Databricks.
- [docs/matrikkelen-utlevering-med-fodselsnummer.md](docs/matrikkelen-utlevering-med-fodselsnummer.md) - tabelldokumentasjon for Matrikkelen utlevering med fødselsnummer.

## Kom i gang

### 1. Opprett nøkkelpar

Lag nøkkelparet lokalt. Den private nøkkelen skal ikke deles eller committes.

```bash
mkdir -p keys
openssl genrsa -out keys/private-key.pem 2048
openssl rsa -in keys/private-key.pem -pubout -out keys/public-key.pem
```

På Windows kan kommandoene kjøres i Git Bash eller WSL.

### 2. Opprett Maskinporten-klient

Kort versjon:
Du er nødt til å opprette en klient i Maskinporten, som du knytter til motatt scope fra oss, og legger til din offentlig nøkkel. Du vil motta en klient-ID og nøkkel-ID som du må bruke i Delta Sharing-profilen.

Detaljert oppsett:

![Opprett klient](assets/opprett-klient.png)
![Velg Maskinporten](assets/maskinporten-type.png)
![Fyll ut klient og velg scope](assets/klient-oppsett.png)
![Client ID](assets/client-id.png)

### 3. Registrer offentlig nøkkel

På klienten, velg **Nøkler** og legg til en ny nøkkel. Lim inn innholdet i
`keys/public-key.pem`, lagre og noter nøkkelens `keyId`.

![Legg til nøkkel](assets/ny-nøkkel.png)
![Lim inn offentlig nøkkel](assets/public-key.png)
![Key ID](assets/key-id.png)

### 4. Opprett Delta Sharing-profil

Du vil motta en lenke med `endpoint` fra Kartverket. Kopier
[config/oauth_config.example.share](config/oauth_config.example.share) til
`config/oauth_config.share`, og fyll inn:

- `endpoint` - lenken du mottar fra Kartverket.
- `clientId` - klient-ID fra Maskinporten.
- `keyId` - nøkkel-ID fra Maskinporten.
- `scope` - scopet du mottar fra Kartverket.

(Kopier oauth_config_test.example.share til oauth_config_test.share for testmiljøet.)

Profilen må ha dette formatet:

```json
{
  "shareCredentialsVersion": 2,
  "type": "oauth_jwt_bearer_private_key_jwt",
  "endpoint": "[ENDPOINT_URL_FROM_KARTVERKET]",
  "auth": {
    "tokenEndpoint": "[MASKINPORTEN_TOKEN_ENDPOINT]",
    "clientId": "[MASKINPORTEN_CLIENT_ID]",
    "issuer": "[MASKINPORTEN_ISSUER]",
    "audience": "[AUDIENCE_FROM_KARTVERKET]",
    "scope": "[SCOPE_FROM_KARTVERKET]",
    "privateKey": {
      "privateKeyFile": "keys/private-key.pem",
      "keyId": "[MASKINPORTEN_KEY_ID]",
      "algorithm": "RS256"
    }
  }
}
```

### 5. Hent ut share-data

Før du kjører eksemplet (se [main.py](main.py)), anbefales det å sette opp et virtuelt miljø for å isolere avhengigheter. Fra rotmappen i prosjektet kjører man:

Med `uv`:

```bash
uv sync
uv run main.py
```

Skriptet lister tilgjengelige tabeller. Hent en tabell med:

```bash
uv run main.py --table SHARE.SCHEMA.TABLE
```

Med vanlig virtualenv på macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install .
python main.py
```

På Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install .
python main.py
```

_(Man trenger bare sette opp det virtuelle miljøet én gang.)_

## Eksempler

Eksemplene tar en fullt kvalifisert tabell på formen `SHARE.SCHEMA.TABLE`.

```bash
uv run examples/preview_first_ten_rows_of_shared_table.py --table SHARE.SCHEMA.TABLE
uv run examples/show_metadata_for_shared_table.py --table SHARE.SCHEMA.TABLE
```

## Datamodellering

Se [tabelldokumentasjonen](docs/matrikkelen-utlevering-med-fodselsnummer.md)
for tilgjengelige tabeller og kolonner. Relasjonsskisser kan ligge sammen med
denne dokumentasjonen ved behov.

## Annet

### Oppdateringsfrekvens

Vi oppdaterer dataene en gang i døgnet pt (oppdateringsvindu = 24 timer). For matrikkeldata er kilden Matrikkelen sin endringslogg.

### Versjonering

Målet er å holde dataproduktene stabile. Generelt må konsumenter forvente at nye kolonner vil kunne legges til i eksisterende dataprodukter uten varsling. Dette må håndteres av nedstrømskonsumenter.
