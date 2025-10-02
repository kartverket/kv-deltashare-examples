# External Table Documentation

## Table of Contents

- [dim_adresse](#dim-adresse)
- [dim_adressereferansekode](#dim-adressereferansekode)
- [dim_adressetilleggsnavnkildekode](#dim-adressetilleggsnavnkildekode)
- [dim_arsaktilfeilrettingkode](#dim-arsaktilfeilrettingkode)
- [dim_arsaktilforingkode](#dim-arsaktilforingkode)
- [dim_avlopskode](#dim-avlopskode)
- [dim_bruksenhetstypekode](#dim-bruksenhetstypekode)
- [dim_bygning](#dim-bygning)
- [dim_bygningsstatushistorikker](#dim-bygningsstatushistorikker)
- [dim_bygningsstatuskode](#dim-bygningsstatuskode)
- [dim_bygningstypekode](#dim-bygningstypekode)
- [dim_eierforholdkode](#dim-eierforholdkode)
- [dim_energikildekode](#dim-energikildekode)
- [dim_etasjeplankode](#dim-etasjeplankode)
- [dim_forretninger](#dim-forretninger)
- [dim_forretningsklassekode](#dim-forretningsklassekode)
- [dim_forretningstypekode](#dim-forretningstypekode)
- [dim_fylker](#dim-fylker)
- [dim_juridisk_person](#dim-juridisk-person)
- [dim_kommuner](#dim-kommuner)
- [dim_koordinatkvalitetkode](#dim-koordinatkvalitetkode)
- [dim_koordinatsystemkode](#dim-koordinatsystemkode)
- [dim_kostrafunksjonkode](#dim-kostrafunksjonkode)
- [dim_kulturminneartkode](#dim-kulturminneartkode)
- [dim_kulturminner](#dim-kulturminner)
- [dim_kulturminner_encrypted](#dim-kulturminner-encrypted)
- [dim_matrikkelenhet](#dim-matrikkelenhet)
- [dim_naringsgruppekode](#dim-naringsgruppekode)
- [dim_opprinnelseskode](#dim-opprinnelseskode)
- [dim_oppvarmingskode](#dim-oppvarmingskode)
- [dim_personidkode](#dim-personidkode)
- [dim_personkategorikode](#dim-personkategorikode)
- [dim_teig](#dim-teig)
- [dim_teiggrensepunkt](#dim-teiggrensepunkt)
- [dim_teiggrenser](#dim-teiggrenser)
- [dim_tinglysingsstatuskode](#dim-tinglysingsstatuskode)
- [dim_vannforsyningskode](#dim-vannforsyningskode)
- [dim_veger](#dim-veger)
- [dim_vernetypekode](#dim-vernetypekode)
- [fact_bruksenheter](#fact-bruksenheter)
- [fact_bruksenheter_historical](#fact-bruksenheter-historical)
- [fact_bygning](#fact-bygning)
- [fact_bygning_historical](#fact-bygning-historical)
- [fact_bygningsendring](#fact-bygningsendring)
- [fact_bygningsendring_historical](#fact-bygningsendring-historical)
- [fact_etasjer](#fact-etasjer)
- [fact_etasjer_historical](#fact-etasjer-historical)
- [fact_forretninger](#fact-forretninger)
- [fact_forretninger_historical](#fact-forretninger-historical)
- [fact_ikke_tinglyste_eierforhold](#fact-ikke-tinglyste-eierforhold)
- [fact_ikke_tinglyste_eierforhold_historical](#fact-ikke-tinglyste-eierforhold-historical)
- [fact_kulturminner](#fact-kulturminner)
- [fact_kulturminner_encrypted](#fact-kulturminner-encrypted)
- [fact_kulturminner_historical](#fact-kulturminner-historical)
- [fact_matrikkelenhet](#fact-matrikkelenhet)
- [fact_matrikkelenhet_historical](#fact-matrikkelenhet-historical)
- [fact_teig](#fact-teig)
- [fact_teig_historical](#fact-teig-historical)
- [fact_teiggrensepunkt](#fact-teiggrensepunkt)
- [fact_teiggrensepunkt_historical](#fact-teiggrensepunkt-historical)
- [fact_teiggrenser](#fact-teiggrenser)
- [fact_teiggrenser_historical](#fact-teiggrenser-historical)

---

## dim_adresse

**Description:**
Tabellen inneholder dimensjoner/attributter for adresser som kommer fra MatrikkelAPI. Tabellen er slått sammen av adressetypene matrikkeladresse og vegadresse. Kan benyttes sammen med fact_bruksenheter/fact_bruksenheter_historical (vegadresser) og fact_matrikkelenheter/fact_matrikkelenheter_historical (matrikkeladresser) ved å koble kolonnenen adresseId mot zk_adresseId som finnes i faktatabellene, i tillegg til gyldighetsrommet for den aktuelle raden (to_dateime/from_datetime). Hva som er gyldighetsrommet, avhenger av om man ønsker å hente ut nåtidsbilde fra faktatabellen, eller historisk bilde. For nåtidsbilde setter man inn timestamp for nå ( now() ), for historisk setter man inne timestamp for når man ønsker å imitere snapshottet tilbake i tid. Kan også benyttes sammen med dim_veger for å få informasjon om vegen som vegadressene er tilknyttet ved dim.zk_vegId = dim_veger.vegId. Eksempel på bruk ville ha vært en JOIN med fact_bruksenheter med condition: WHERE dim.adresseId = fact.zk_adresseId AND now() BETWEEN dim.to_datetime AND dim.from_datetime.

**Schema:**

| Column | Type |
|--------|------|
| adresseId | bigint |
| adresseId_date_updated | string |
| adresseType | string |
| adressetilleggsnavn | string |
| atkomster | array<struct<atkomsttypeKodeId:struct<value:bigint>,id:bigint,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,opphavKodeId:struct<value:bigint>,punkt:struct<metadata:struct<item:array<string>>,x:double,y:double,z:double>,uuid:struct<navnerom:string,uuid:string>,versjonId:bigint>> |
| bokstav | string |
| kommunalTilleggsdel | struct<metadata:struct<item:array<string>>> |
| kortnavn | string |
| nummer | bigint |
| zk_representasjonspunkt_koordinatkvalitetKodeId | bigint |
| zk_representasjonspunkt_koordinatsystemKodeId | bigint |
| zk_representasjonspunkt_originalKoordinatsystemKodeId | bigint |
| representasjonspunkt_position_x | double |
| representasjonspunkt_position_y | double |
| representasjonspunkt_position_z | double |
| representasjonspunkt_stedfestingVerifisert | boolean |
| undernummer | bigint |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zk_kretsIds | array<bigint> |
| zk_matrikkelenhetId | bigint |
| zk_tilleggsnavnKildekodeId | bigint |
| zk_vegId | bigint |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"46","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_adressereferansekode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| adressereferanseKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_adressetilleggsnavnkildekode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| adressetilleggsnavnkildeKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_arsaktilfeilrettingkode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| arsaktilfeilrettingKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_arsaktilforingkode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| arsaktilforingKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_avlopskode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| avlopsKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_bruksenhetstypekode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| bruksenhetstypeKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_bygning

**Description:**
Tabellen inneholder dimensjoner/attributter for bygninger som kommer fra MatrikkelAPI. Kan benyttes sammen med fact_bruksenheter/fact_bruksenheter_historical og fact_bygning/fact_bygning_historical ved å koble kolonnenen bygningId mot zk_bygningId/bygningId som finnes i faktatabellene, i tillegg til gyldighetsrommet for den aktuelle raden (to_dateime/from_datetime). Hva som er gyldighetsrommet, avhenger av om man ønsker å hente ut nåtidsbilde fra faktatabellen, eller historisk bilde. For nåtidsbilde setter man inn timestamp for nå ( now() ), for historisk setter man inne timestamp for når man ønsker å imitere snapshottet tilbake i tid. Eksempel på bruk ville ha vært en JOIN med fact_bruksenheter med condition: WHERE dim.bygningId = fact.zk_bygning AND now() BETWEEN dim.to_datetime AND dim.from_datetime

**Schema:**

| Column | Type |
|--------|------|
| bygningId | bigint |
| bygningId_date_updated | string |
| bygningsnummer | bigint |
| bygningsstatusBokmaal | string |
| bygningsstatusKode | string |
| zk_bygningsstatusKodeId | bigint |
| bygningsstatusNynorsk | string |
| bygningstypeBokmaal | string |
| bygningstypeKode | string |
| zk_bygningstypeKodeId | bigint |
| bygningstypeNynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"13","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_bygningsstatushistorikker

**Description:**
Tabellen inneholder bygningsstatushistorikker,som er en dimensjon (berikelse) inn mot fact_bygning. Data stammer fra MatrikkelAPI. Bygningsstatushistorikk viser hvilken status (lovlige statuser for bygningstiltak) en bygning har eller har gjennomgått. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Nyeste endring fra bygning er tatt ut, og bygningsstatushistorikk fra denne bygningsraden er tatt ut i denne tabellen. Kolonnene er sortert alfabetisk. Kan benyttes sammen med fact_bygning ved å gjøre en join av bygningId mot fact_bygning på kolonenne bygningId og zk_bygningsstatusKodeId (trenger begge sammen for unik nøkkel fra bygningId mot status). Kobling mot bygning via bygningId skal være tilstrekkelig alene da denne iden er unik per statushistorikk. Derfor har ikke denne dimensjonstabellen SCD2 logikk på datointervaller.

**Schema:**

| Column | Type |
|--------|------|
| bygningsstatushistorikkId | bigint |
| zk_arsakTilForingKodeId | bigint |
| arsaktilforingBokmaal | string |
| arsaktilforingKode | string |
| arsaktilforingNynorsk | string |
| zk_bygningId | bigint |
| bygningsnummer | bigint |
| bygningsstatusBokmaal | string |
| bygningsstatusKode | string |
| zk_bygningsstatusKodeId | bigint |
| bygningsstatusNynorsk | string |
| dato | date |
| oppdateringsdato | timestamp |
| registrertDato | string |
| slettetDato | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"15","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_bygningsstatuskode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| bygningsstatusKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_bygningstypekode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| bygningstypeKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_eierforholdkode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| eierforholdKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_energikildekode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| energikildeKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_etasjeplankode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| etasjeplanKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_forretninger

**Description:**
Tabellen inneholder dimensjoner/attributter for forretninger som kommer fra MatrikkelAPI. Forretning dokumenterer hendelser knyttet til en matrikkelenhet, inkludert naboenheter med felles punkter i forretningen. Matrikkelforskriften § 3 fastslår at matrikkelen inneholder opplysninger om historikk, som tidligere oppmålingsforretninger, fradelinger, sammenslåinger, seksjoneringer, grensejusteringer m.m., med dateringer og referanser til saksarkiv. Kan benyttes sammen med fact_forretninger med forretningId.

**Schema:**

| Column | Type |
|--------|------|
| forretningId | bigint |
| zk_arsakTilFeilrettingKodeId | bigint |
| forretningId_date_updated | string |
| forretningsdokumentdato | string |
| zk_forretningsklasseKodeId | bigint |
| zk_forretningstypeKodeId | bigint |
| kommunalSaksreferanse | string |
| matrikkelforingsdato | string |
| oppdatertAv | string |
| tinglysingsstatusEndretDato | string |
| uuid | struct<navnerom:string,uuid:string> |
| versjon | bigint |
| versjonId | bigint |
| from_datetime | timestamp |
| to_datetime | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"17","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_forretningsklassekode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| forretningsklasseKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_forretningstypekode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| forretningstypeKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_fylker

**Description:**
Tabellen inneholder dimensjoner/attributter for fylker. Gyldighetsrommet for hver rad er basert på gyldigTilDato-attributten fra matrikkelen.

**Schema:**

| Column | Type |
|--------|------|
| fylkeId | bigint |
| fylkesnavn | string |
| fylkesnummer | string |
| gyldigTilDato | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_juridisk_person

**Description:**
Denne tabellen er en endret klone av en sølvtabell til ekstern deling. Orginal tabellbeskrivelse: Tabellen inneholder dimensjoner/attributter for personer av typen juridisk person som kommer fra MatrikkelAPI. Matrikkelen inneholder alle enheter fra Enhetsregisteret, de er lagret som personer med organisasjonsnummer. Kan eksempelvis benyttes sammen med fact_eierforhold med juridiskPersonId. Tabellen er endret for ekstern deling. Følgende kolonner er bevart i ekstern tabell: juridiskPersonId, nummer, versjon, versjonId, from_datetime, to_datetime, juridiskPersonId_date_updated.

**Schema:**

| Column | Type |
|--------|------|
| juridiskPersonId | bigint |
| nummer | string |
| versjon | bigint |
| versjonId | bigint |
| from_datetime | timestamp |
| to_datetime | timestamp |
| juridiskPersonId_date_updated | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_kommuner

**Description:**
Tabellen inneholder dimensjoner/attributter for kommuner. Gyldighetsrommet for hver rad er basert på gyldigTilDato-attributten fra matrikkelen.

**Schema:**

| Column | Type |
|--------|------|
| kommuneId | bigint |
| kommunenavn | string |
| kommunenummer | string |
| zk_fylkeId | bigint |
| gyldigTilDato | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"5","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_koordinatkvalitetkode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| koordinatkvalitetKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_koordinatsystemkode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| koordinatsystemKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_kostrafunksjonkode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| kostrafunksjonKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_kulturminneartkode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| kulturminneartKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_kulturminner

**Description:**
Tabellen inneholder dimensjoner/attributter for kulturminner som kommer fra MatrikkelAPI. Opplysninger om kulturminner kan blant annet gjelde automatisk fredete kulturminner, vedtaksfredete kulturminner og kulturmiljø. Opplysninger om kulturminner vil framkomme som utdrag eller kopling mot Riksantikvarens register over kulturminner, Askeladden. Regler om dette fastsettes i avtale mellom Riksantikvaren og Statens kartverk. Kan benyttes sammen med fact_kulturminner.

**Schema:**

| Column | Type |
|--------|------|
| kulturminneId | bigint |
| enkeltminner | array<struct<bygningId:struct<value:bigint>,enkeltminneArtKodeId:struct<value:bigint>,enkeltminnenummer:string,id:bigint,kategoriKodeId:struct<value:bigint>,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,vernetypeKodeId:struct<value:bigint>,versjonId:bigint>> |
| kulturminneId_date_updated | string |
| lokalitetsnummer | string |
| matrikkelforingsdato | string |
| oppdatertAv | string |
| sistOppdatertDato | string |
| uuid | struct<navnerom:string,uuid:string> |
| versjon | bigint |
| versjonId | bigint |
| from_datetime | timestamp |
| to_datetime | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"30","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"true"}
```

---

## dim_kulturminner_encrypted

**Description:**
Tabellen inneholder krypterte dimensjoner/attributter for kulturminner som kommer fra MatrikkelAPI. Opplysninger om kulturminner kan blant annet gjelde automatisk fredete kulturminner, vedtaksfredete kulturminner og kulturmiljø. Opplysninger om kulturminner vil framkomme som utdrag eller kopling mot Riksantikvarens register over kulturminner, Askeladden. Regler om dette fastsettes i avtale mellom Riksantikvaren og Statens kartverk. Kan benyttes sammen med fact_kulturminner.

**Schema:**

| Column | Type |
|--------|------|
| kulturminneId | bigint |
| enkeltminner | array<struct<bygningId:struct<value:string>,enkeltminneArtKodeId:struct<value:string>,enkeltminnenummer:string,id:string,kategoriKodeId:struct<value:string>,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,vernetypeKodeId:struct<value:string>,versjonId:string>> |
| keyId | string |
| kulturminneId_date_updated | string |
| lokalitetsnummer | string |
| matrikkelforingsdato | string |
| oppdatertAv | string |
| sistOppdatertDato | string |
| uuid | struct<navnerom:string,uuid:string> |
| versjon | bigint |
| versjonId | bigint |
| from_datetime | timestamp |
| to_datetime | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_matrikkelenhet

**Description:**
Tabellen inneholder dimensjonene til matrikkelenheter som stammer fra MatrikkelAPI. De ulike matrikkelenhetene kommer som egne matrikkelbobler fra APIet, men er slått sammen i denne tabellen. Kan benyttes sammen med bl.a fact_bruksenheter/fact_bruksenheter_historical og fact_matrikkelenhet/fact_matrikkelenhet_historical ved å koble kolonnen matrikkelenhetId mot zk_matrikkelenhetId som finnes i faktatabellene, i tillegg til gyldighetsrommet for den aktuelle raden (to_dateime/from_datetime). Hva som er gyldighetsrommet, avhenger av om man ønsker å hente ut nåtidsbilde fra faktatabellen, eller historisk bilde. For nåtidsbilde setter man inn timestamp for nå ( now() ), for historisk setter man inne timestamp for når man ønsker å imitere snapshottet tilbake i tid. Eksempel på bruk ville ha vært en JOIN med fact_bruksenheter med condition: WHERE dim.matrikkelenhetId = fact.zk_matrikkelenhetId AND now() BETWEEN dim.to_datetime AND dim.from_datetime

**Schema:**

| Column | Type |
|--------|------|
| matrikkelenhetId | bigint |
| bruksnummer | bigint |
| etableringsdatoMatrikkelenhet | date |
| festenummer | bigint |
| gardsnummer | bigint |
| matrikkelenhetId_date_updated | string |
| matrikkelenhetType | string |
| seksjonsnummer | bigint |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zk_kommuneId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_naringsgruppekode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| naringsgruppeKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_opprinnelseskode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| opprinnelsesKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_oppvarmingskode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| oppvarmingsKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_personidkode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| personidKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_personkategorikode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| personkategoriKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_teig

**Description:**
Tabellen inneholder dimensjoner/attributter for teiger som kommer fra MatrikkelAPI. En teig er et sammenhengende areal som avgrenses av teiggrense. Teiger skal ikke overlappe hverandre. Naboteiger skal ha delt geometri. Matrikkelenheter som består av flere areal som er sammenhengende i bare et punkt er teigdelt etter denne definisjonen. Koordinatsystemet som benyttes er koordinatSystemKodeId 11, som refererer til EUREF89 UTM Sone 33.

**Schema:**

| Column | Type |
|--------|------|
| teigId | bigint |
| datafangstdato | struct<date:string> |
| flate | struct<exterior:struct<curveDirections:struct<item:array<struct<grenselinjeId:struct<value:bigint>,id:bigint,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,signed:boolean,uuid:struct<navnerom:string,uuid:string>,versjonId:bigint>>>,id:bigint,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,uuid:struct<navnerom:string,uuid:string>,versjonId:bigint>,interior:struct<item:array<struct<curveDirections:struct<item:array<struct<grenselinjeId:struct<value:bigint>,id:bigint,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,signed:boolean,uuid:struct<navnerom:string,uuid:string>,versjonId:bigint>>>,id:bigint,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,uuid:struct<navnerom:string,uuid:string>,versjonId:bigint>>>,metadata:struct<item:array<string>>> |
| kommunalTilleggsdel | struct<metadata:struct<item:array<string>>> |
| oppdatertAv | string |
| representasjonspunkt | struct<koordinatsystemKodeId:struct<value:bigint>,kvalitet:struct<malemetodeId:struct<value:bigint>,metadata:struct<item:array<string>>,noyaktighet:bigint>,metadata:struct<item:array<string>>,originalKoordinatsystemKodeId:struct<value:bigint>,position:struct<metadata:struct<item:array<string>>,x:double,y:double,z:double>,stedfestingVerifisert:boolean> |
| teigId_date_updated | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| avklartEiere | boolean |
| teigMedFlereMatrikkelenheter | boolean |
| tvist | boolean |
| uregistrertJordsameie | boolean |
| versjon | bigint |
| versjonId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_teiggrensepunkt

**Description:**
Tabellen inneholder dimensjoner/attributter for teiggrensepunkt som kommer fra MatrikkelAPI. Et teiggrensepunkt er et koordinatbestemt punkt som er påvist, beskrevet og/eller markert spesielt i den geografiske avgrensingen av teigen. Et teiggrensepunkt kan også være et registreringsteknisk hjelpepunkt. Punktet tilhører minst én teiggrense når grensen danner en lukket sløyfe, ellers tilhører det minst to teiggrenser. Teiggrensepunkter er enten start- eller sluttpunkt på en teiggrense. I matrikkelen er teiggrensepunktene «delte», noe som innebærer at sammenfallende punkter ikke tillates. Koordinatsystemet som benyttes er koordinatSystemKodeId 11, som refererer til EUREF89 UTM Sone 33.

**Schema:**

| Column | Type |
|--------|------|
| teiggrensepunktId | bigint |
| datafangstdato | struct<date:string> |
| noyaktighet | bigint |
| oppdatertAv | string |
| posisjon | struct<metadata:struct<item:array<string>>,x:double,y:double,z:double> |
| teiggrensepunktId_date_updated | string |
| from_datetime | timestamp |
| to_datetime | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"true"}
```

---

## dim_teiggrenser

**Description:**
Tabellen inneholder dimensjoner/attributter for teiggrenser som kommer fra MatrikkelAPI. En teiggrense avgrenser en teig. En teiggrense vil være sammensatt av punkter og inneholde informasjon om sine start- og endepunkt. Koordinatsystemet som benyttes er koordinatSystemKodeId 11, som refererer til EUREF89 UTM Sone 33.

**Schema:**

| Column | Type |
|--------|------|
| teiggrenseId | bigint |
| datafangstdato | struct<date:string> |
| kurvepunkter | struct<item:array<struct<metadata:struct<item:array<string>>,x:double,y:double,z:double>>> |
| noyaktighet | bigint |
| oppdatertAv | string |
| teiggrenseId_date_updated | string |
| from_datetime | timestamp |
| to_datetime | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"true"}
```

---

## dim_tinglysingsstatuskode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| tinglysingsstatusKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_vannforsyningskode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| vannforsyningsKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_veger

**Description:**
Tabellen inneholder dimensjoner/attributter for veger som kommer fra MatrikkelAPI. Kan kobles til dim_adresser via dim_adresse.zk_adresseId = dim_veger_adresseId

**Schema:**

| Column | Type |
|--------|------|
| vegId | bigint |
| adressekode | bigint |
| adressenavn | string |
| kortAdressenavn | string |
| stedsnummer | string |
| vegId_date_updated | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zk_kommuneId | bigint |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## dim_vernetypekode

**Description:**
None

**Schema:**

| Column | Type |
|--------|------|
| vernetypeKodeId | bigint |
| kodeverdi | string |
| navn_bokmaal | string |
| navn_nynorsk | string |
| from_datetime | timestamp |
| to_datetime | timestamp |
| zx_ingest_timestamp | timestamp |
| zx_ingest_file_name | string |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_bruksenheter

**Description:**
Tabellen inneholder fakta om bruksenheter og bruksenhetsnummer som stammer fra MatrikkelAPI. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med følgende dimensjoner: dim_bruksenhetstypekode, dim_bruksenheter, dim_addresse, dim_matrikkelenhet, dim_bygg. Fremmednøkler til dimensjonstabellene er prefikset med zk_, systemkolonner er prefikset med zx_.

**Schema:**

| Column | Type |
|--------|------|
| bruksenhetId | bigint |
| antallBad | bigint |
| antallRom | bigint |
| antallWC | bigint |
| bruksareal | double |
| bruksenhet_lopenummer | bigint |
| bruksenhetsnummer | string |
| byggSkjermingsverdig | boolean |
| etasjenummer | bigint |
| kostraLeieareal | boolean |
| oppdateringsdato | timestamp |
| skalUtga | boolean |
| zk_adresseId | bigint |
| zk_bruksenhetstypeKodeId | bigint |
| zk_bygningId | bigint |
| zk_etasjeplanKodeId | bigint |
| zk_kjokkentilgangId | bigint |
| zk_kostraFunksjonKodeId | bigint |
| zk_kostraVirksomhetId | bigint |
| zk_matrikkelenhetId | bigint |
| zx_ingest_file_name | string |
| zx_ingest_timestamp | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_bruksenheter_historical

**Description:**
Tabellen inneholder fakta om bruksenheter og bruksenhetsnummer som stammer fra MatrikkelAPI. Data er rensket for duplikater, men inneholder historikk basert på endringslogg fra matrikkelen. Iden for selve objektene vil være bruksenhetId. Fordi dette er en historisk tabell vil flere rader kunne ha samme bruksenhetId, man må da bruke et tidspunkt, f.eks oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av bruksenhetId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Kan benyttes sammen med følgende dimensjoner: dim_bruksenhetstypekode, dim_bruksenheter, dim_addresse, dim_matrikkelenhet, dim_bygg. Fremmednøkler til dimensjonstabellene er prefikset med zk_, systemkolonner er prefikset med zx_

**Schema:**

| Column | Type |
|--------|------|
| bruksenhetId | bigint |
| antallBad | bigint |
| antallRom | bigint |
| antallWC | bigint |
| bruksareal | double |
| bruksenhetId_historical | string |
| bruksenhet_lopenummer | bigint |
| bruksenhetsnummer | string |
| byggSkjermingsverdig | boolean |
| endringstype | string |
| etasjenummer | bigint |
| kostraLeieareal | boolean |
| oppdateringsdato | timestamp |
| skalUtga | boolean |
| zk_adresseId | bigint |
| zk_bruksenhetstypeKodeId | bigint |
| zk_bygningId | bigint |
| zk_etasjeplanKodeId | bigint |
| zk_kjokkentilgangId | bigint |
| zk_kostraFunksjonKodeId | bigint |
| zk_kostraVirksomhetId | bigint |
| zk_matrikkelenhetId | bigint |
| zx_ingest_file_name | string |
| zx_ingest_timestamp | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_bygning

**Description:**
Tabellen inneholder fakta om bygninger som stammer fra MatrikkelAPI. Bygning er matrikkelens representasjon av en planlagt, under oppføring, fullført eller av en eller annen grunn utgått bygning. Alle bygninger oppført etter 1983 er registrert. I enkelte kommuner har man registrert samtlige bygninger. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx_

**Schema:**

| Column | Type |
|--------|------|
| bygningId | bigint |
| bebygdAreal | double |
| bygningsnummer | bigint |
| etasjedata | struct<alternativtAreal:double,alternativtAreal2:double,antallBoenheter:bigint,bruksarealTilAnnet:double,bruksarealTilBolig:double,bruksarealTotalt:double,bruttoarealTilAnnet:double,bruttoarealTilBolig:double,bruttoarealTotalt:double,metadata:struct<item:array<string>>> |
| harHeis | boolean |
| harKulturminne | boolean |
| harSefrakminne | boolean |
| kommunalTilleggsdel | struct<alternativtArealBygning:double,antallEtasjer:bigint,antallRoklop:bigint,brenseltankNedgravd:bigint,fundamenteringsKodeId:struct<value:bigint>,kildePrivatVannforsyningKodeId:struct<value:bigint>,metadata:struct<item:array<string>>,privatKloakkRensingsKodeId:struct<value:bigint>,renovasjonsKodeId:struct<value:bigint>,septiktank:boolean> |
| kontaktpersoner | array<struct<datoFra:struct<date:string>,id:bigint,kontaktpersonKodeId:struct<value:bigint>,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,personId:struct<value:bigint>,versjonId:bigint>> |
| lopenummer | bigint |
| oppdateringsdato | timestamp |
| zk_representasjonspunkt_koordinatkvalitetKodeId | bigint |
| zk_representasjonspunkt_koordinatsystemKodeId | bigint |
| zk_representasjonspunkt_originalKoordinatsystemKodeId | bigint |
| representasjonspunkt_position_x | double |
| representasjonspunkt_position_y | double |
| representasjonspunkt_position_z | double |
| representasjonspunkt_stedfestingVerifisert | boolean |
| skjermingsverdig | boolean |
| tidligereByggId | bigint |
| ufullstendigAreal | boolean |
| utenBebygdAreal | boolean |
| zk_avlopsKodeId | bigint |
| zk_bruksenhetIds | array<struct<value:bigint>> |
| zk_bygningsstatusKodeId | bigint |
| zk_bygningstypeKodeId | bigint |
| zk_energikildeKodeIds | array<struct<value:bigint>> |
| zk_kommuneId | bigint |
| zk_naringsgruppeKodeId | bigint |
| zk_opprinnelsesKodeId | bigint |
| zk_oppvarmingsKodeIds | array<struct<value:bigint>> |
| zk_vannforsyningsKodeId | bigint |
| zx_ingest_file_name | string |
| zx_ingest_timestamp | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"76","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_bygning_historical

**Description:**
Tabellen inneholder fakta om bygninger som stammer fra MatrikkelAPI. Bygning er matrikkelens representasjon av en planlagt, under oppføring, fullført eller av en eller annen grunn utgått bygning. Alle bygninger oppført etter 1983 er registrert. I enkelte kommuner har man registrert samtlige bygninger. Data rensket for duplikater, men inneholder historikk basert på endringslogg fra matrikkelen. Iden for selve objektene vil være bygningId. Fordi dette er en historisk tabell vil flere rader kunne ha samme bygningId, man må da bruke et tidspunkt f.eks bruke oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av bygningId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__

**Schema:**

| Column | Type |
|--------|------|
| bygningId | bigint |
| bebygdAreal | double |
| bygningId_historical | string |
| bygningsnummer | bigint |
| endringstype | string |
| etasjedata | struct<alternativtAreal:double,alternativtAreal2:double,antallBoenheter:bigint,bruksarealTilAnnet:double,bruksarealTilBolig:double,bruksarealTotalt:double,bruttoarealTilAnnet:double,bruttoarealTilBolig:double,bruttoarealTotalt:double,metadata:struct<item:array<string>>> |
| harHeis | boolean |
| harKulturminne | boolean |
| harSefrakminne | boolean |
| kommunalTilleggsdel | struct<alternativtArealBygning:double,antallEtasjer:bigint,antallRoklop:bigint,brenseltankNedgravd:bigint,fundamenteringsKodeId:struct<value:bigint>,kildePrivatVannforsyningKodeId:struct<value:bigint>,metadata:struct<item:array<string>>,privatKloakkRensingsKodeId:struct<value:bigint>,renovasjonsKodeId:struct<value:bigint>,septiktank:boolean> |
| kontaktpersoner | array<struct<datoFra:struct<date:string>,id:bigint,kontaktpersonKodeId:struct<value:bigint>,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,personId:struct<value:bigint>,versjonId:bigint>> |
| lopenummer | bigint |
| oppdateringsdato | timestamp |
| zk_representasjonspunkt_koordinatkvalitetKodeId | bigint |
| zk_representasjonspunkt_koordinatsystemKodeId | bigint |
| zk_representasjonspunkt_originalKoordinatsystemKodeId | bigint |
| representasjonspunkt_position_x | double |
| representasjonspunkt_position_y | double |
| representasjonspunkt_position_z | double |
| representasjonspunkt_stedfestingVerifisert | boolean |
| skjermingsverdig | boolean |
| tidligereByggId | bigint |
| ufullstendigAreal | boolean |
| utenBebygdAreal | boolean |
| zk_avlopsKodeId | bigint |
| zk_bruksenhetIds | array<struct<value:bigint>> |
| zk_bygningsstatusKodeId | bigint |
| zk_bygningstypeKodeId | bigint |
| zk_energikildeKodeIds | array<struct<value:bigint>> |
| zk_kommuneId | bigint |
| zk_naringsgruppeKodeId | bigint |
| zk_opprinnelsesKodeId | bigint |
| zk_oppvarmingsKodeIds | array<struct<value:bigint>> |
| zk_vannforsyningsKodeId | bigint |
| zx_ingest_file_name | string |
| zx_ingest_timestamp | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"78","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_bygningsendring

**Description:**
Tabellen inneholder fakta om bygningsendringer som stammer fra MatrikkelAPI. Tabellen vil inneholde oversikt over endringer på en bygning. Bygningsendring er matrikkelens representasjon av en endring på en bygning. Alle bygninger oppført etter 1983 er registrert. I enkelte kommuner har man registrert samtlige bygninger. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx_

**Schema:**

| Column | Type |
|--------|------|
| bygningsendringId | bigint |
| bebygdAreal | double |
| bygningsnummer | bigint |
| etasjedata | struct<alternativtAreal:double,alternativtAreal2:double,antallBoenheter:bigint,bruksarealTilAnnet:double,bruksarealTilBolig:double,bruksarealTotalt:double,bruttoarealTilAnnet:double,bruttoarealTilBolig:double,bruttoarealTotalt:double,metadata:struct<item:array<string>>> |
| harHeis | boolean |
| harKulturminne | boolean |
| harSefrakminne | boolean |
| kommunalTilleggsdel | struct<alternativtArealBygning:double,antallEtasjer:bigint,antallRoklop:bigint,brenseltankNedgravd:bigint,fundamenteringsKodeId:struct<value:bigint>,kildePrivatVannforsyningKodeId:struct<value:bigint>,metadata:struct<item:array<string>>,privatKloakkRensingsKodeId:struct<value:bigint>,renovasjonsKodeId:struct<value:bigint>,septiktank:boolean> |
| kontaktpersoner | array<struct<datoFra:struct<date:string>,id:bigint,kontaktpersonKodeId:struct<value:bigint>,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,personId:struct<value:bigint>,versjonId:bigint>> |
| lopenummer | bigint |
| oppdateringsdato | timestamp |
| representasjonspunkt_koordinatkvalitetKodeId | bigint |
| representasjonspunkt_koordinatsystemKodeId | bigint |
| representasjonspunkt_originalKoordinatsystemKodeId | bigint |
| representasjonspunkt_position_x | double |
| representasjonspunkt_position_y | double |
| representasjonspunkt_position_z | double |
| representasjonspunkt_stedfestingVerifisert | boolean |
| skjermingsverdig | boolean |
| tidligereByggId | bigint |
| utenBebygdAreal | boolean |
| zk_avlopsKodeId | bigint |
| zk_bruksenhetIds | array<struct<value:bigint>> |
| zk_bygningId | bigint |
| zk_bygningsendringsKodeId | bigint |
| zk_bygningsstatusKodeId | bigint |
| zk_energikildeKodeIds | array<struct<value:bigint>> |
| zk_kommuneId | bigint |
| zk_naringsgruppeKodeId | bigint |
| zk_opprinnelsesKodeId | bigint |
| zk_oppvarmingsKodeIds | array<struct<value:bigint>> |
| zk_vannforsyningsKodeId | bigint |
| zx_ingest_file_name | string |
| zx_ingest_timestamp | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"77","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_bygningsendring_historical

**Description:**
Tabellen inneholder fakta om bygningsendringer som stammer fra MatrikkelAPI. Tabellen vil inneholde oversikt over endringer på en bygning. Bygningsendring er matrikkelens representasjon av en endring på en bygning. Alle bygninger oppført etter 1983 er registrert. I enkelte kommuner har man registrert samtlige bygninger. Data rensket for duplikater, men inneholder historikk basert på endringslogg fra matrikkelen. Iden for selve objektene vil være bygningsendringId. Fordi dette er en historisk tabell vil flere rader kunne ha samme bygningsendringId, man må da bruke et tidspunkt f.eks bruke oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av bygningsendringId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__

**Schema:**

| Column | Type |
|--------|------|
| bygningsendringId | bigint |
| bebygdAreal | double |
| bygningsendringId_historical | string |
| bygningsnummer | bigint |
| endringstype | string |
| etasjedata | struct<alternativtAreal:double,alternativtAreal2:double,antallBoenheter:bigint,bruksarealTilAnnet:double,bruksarealTilBolig:double,bruksarealTotalt:double,bruttoarealTilAnnet:double,bruttoarealTilBolig:double,bruttoarealTotalt:double,metadata:struct<item:array<string>>> |
| harHeis | boolean |
| harKulturminne | boolean |
| harSefrakminne | boolean |
| kommunalTilleggsdel | struct<alternativtArealBygning:double,antallEtasjer:bigint,antallRoklop:bigint,brenseltankNedgravd:bigint,fundamenteringsKodeId:struct<value:bigint>,kildePrivatVannforsyningKodeId:struct<value:bigint>,metadata:struct<item:array<string>>,privatKloakkRensingsKodeId:struct<value:bigint>,renovasjonsKodeId:struct<value:bigint>,septiktank:boolean> |
| kontaktpersoner | array<struct<datoFra:struct<date:string>,id:bigint,kontaktpersonKodeId:struct<value:bigint>,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,personId:struct<value:bigint>,versjonId:bigint>> |
| lopenummer | bigint |
| oppdateringsdato | timestamp |
| representasjonspunkt_koordinatkvalitetKodeId | bigint |
| representasjonspunkt_koordinatsystemKodeId | bigint |
| representasjonspunkt_originalKoordinatsystemKodeId | bigint |
| representasjonspunkt_position_x | double |
| representasjonspunkt_position_y | double |
| representasjonspunkt_position_z | double |
| representasjonspunkt_stedfestingVerifisert | boolean |
| skjermingsverdig | boolean |
| tidligereByggId | bigint |
| utenBebygdAreal | boolean |
| zk_avlopsKodeId | bigint |
| zk_bruksenhetIds | array<struct<value:bigint>> |
| zk_bygningId | bigint |
| zk_bygningsendringsKodeId | bigint |
| zk_bygningsstatusKodeId | bigint |
| zk_energikildeKodeIds | array<struct<value:bigint>> |
| zk_kommuneId | bigint |
| zk_naringsgruppeKodeId | bigint |
| zk_opprinnelsesKodeId | bigint |
| zk_oppvarmingsKodeIds | array<struct<value:bigint>> |
| zk_vannforsyningsKodeId | bigint |
| zx_ingest_file_name | string |
| zx_ingest_timestamp | timestamp |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"79","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_etasjer

**Description:**
Tabellen inneholder fakta om etasjer som stammer fra MatrikkelAPI. Etasje i bygning. For å kunne angi areal pr. etasje, siden bruksenheter kan gå over flere etasjer. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med dim_bygning på zk_bygningId på fremmednøklene.

**Schema:**

| Column | Type |
|--------|------|
| bygningId_etasjenummer | string |
| alternativtAreal | double |
| alternativtAreal2 | double |
| bruksarealTilAnnet | double |
| bruksarealTilBolig | double |
| bruttoarealTilBolig | double |
| bruttoarealTotalt | double |
| bygningsnummer | bigint |
| etasjenummer | bigint |
| zk_etasjeplanKodeId | bigint |
| oppdateringsdato | timestamp |
| oppdatertAv | string |
| versjonId | bigint |
| zk_bygningId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"14","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_etasjer_historical

**Description:**
Tabellen inneholder fakta om etasjer som stammer fra MatrikkelAPI. Etasje i bygning. For å kunne angi areal pr. etasje, siden bruksenheter kan gå over flere etasjer. Data rensket for duplikater, men inneholder historikk basert på endringslogg fra matrikkelen. Iden for selve objektene vil være bygningId_etasjenummer. Fordi dette er en historisk tabell vil flere rader kunne ha samme bygningId_etasjenummer, man må da bruke et tidspunkt f.eks bruke oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av bygningId_etasjenummer og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Kolonnene er sortert alfabetisk. Kan benyttes sammen med dim_bygning på zk_bygningId på fremmednøklene.

**Schema:**

| Column | Type |
|--------|------|
| bygningId_etasjenummer | string |
| alternativtAreal | double |
| alternativtAreal2 | double |
| bruksarealTilAnnet | double |
| bruksarealTilBolig | double |
| bruttoarealTilBolig | double |
| bruttoarealTotalt | double |
| bygningId_etasjenummer_historical | string |
| bygningsnummer | bigint |
| endringstype | string |
| etasjenummer | bigint |
| zk_etasjeplanKodeId | bigint |
| oppdateringsdato | timestamp |
| oppdatertAv | string |
| versjonId | bigint |
| zk_bygningId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"16","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_forretninger

**Description:**
Tabellen inneholder fakta om forretninger som stammer fra MatrikkelAPI. Forretning dokumenterer hendelser knyttet til en matrikkelenhet, inkludert naboenheter med felles punkter i forretningen. Matrikkelforskriften § 3 fastslår at matrikkelen inneholder opplysninger om historikk, som tidligere oppmålingsforretninger, fradelinger, sammenslåinger, seksjoneringer, grensejusteringer m.m., med dateringer og referanser til saksarkiv. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx_

**Schema:**

| Column | Type |
|--------|------|
| forretningId | bigint |
| annenReferanse | string |
| kommunalSaksreferanse | string |
| lopenummer | bigint |
| oppdateringsdato | timestamp |
| zk_teigIds | array<struct<value:bigint>> |
| zk_teiggrenseIds | array<struct<value:bigint>> |
| zk_teiggrensepunktIds | array<struct<value:bigint>> |
| zk_tinglysingsstatusKodeId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_forretninger_historical

**Description:**
Tabellen inneholder fakta om forretninger som stammer fra MatrikkelAPI. Forretning dokumenterer hendelser knyttet til en matrikkelenhet, inkludert naboenheter med felles punkter i forretningen. Matrikkelforskriften § 3 fastslår at matrikkelen inneholder opplysninger om historikk, som tidligere oppmålingsforretninger, fradelinger, sammenslåinger, seksjoneringer, grensejusteringer m.m., med dateringer og referanser til saksarkiv. Data rensket for duplikater, men inneholder historikk basert på endringslogg fra matrikkelen. Iden for selve objektene vil være forretningId. Fordi dette er en historisk tabell vil flere rader kunne ha samme forretningId, man må da bruke et tidspunkt f.eks bruke oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av forretningId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__

**Schema:**

| Column | Type |
|--------|------|
| forretningId | bigint |
| annenReferanse | string |
| endringstype | string |
| forretningId_historical | string |
| kommunalSaksreferanse | string |
| lopenummer | bigint |
| oppdateringsdato | timestamp |
| zk_teigIds | array<struct<value:bigint>> |
| zk_teiggrenseIds | array<struct<value:bigint>> |
| zk_teiggrensepunktIds | array<struct<value:bigint>> |
| zk_tinglysingsstatusKodeId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_ikke_tinglyste_eierforhold

**Description:**
Tabellen inneholder fakta om eierforhold som kommer fra MatrikkelAPI og beskriver de eierforholdene som ikke er tinglyst. Tabellen er slått sammen av de ulike eierforholdtypene juridiskpersonikketinglysteierforhold, kontaktinstans, matrikkelenhetikketinglysteierforhold og personikketinglysteierforhold. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Koblingskolonner til dimensjoner er prefikset med zk_. MatrikkelenhetId er ikke unik per eierforhold da en matrikkelenhet kan ha flere eierforhold, men hvert eierforhold har en egen eierforholdId. Eierforhold kan derfor kobles mot dim_matrikkelenhet ved å bruke zk_matrikkelenhetId. Systemkolonner er prefikset med zx_.

**Schema:**

| Column | Type |
|--------|------|
| eierforholdId | bigint |
| UUID | struct<navnerom:string,uuid:string> |
| andelNevner | bigint |
| andelTeller | bigint |
| datoFra | string |
| datoTil | string |
| drop_me_endringslogg_zx_ingest_timestamp | timestamp |
| eierforholdType | string |
| metadata | struct<item:array<string>> |
| oppdateringsdato | timestamp |
| zk_eiendeMatrikkelenhetId | bigint |
| zk_eierId | bigint |
| zk_eierforholdKodeId | bigint |
| zk_kommuneId | bigint |
| zk_matrikkelenhetId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_ikke_tinglyste_eierforhold_historical

**Description:**
Tabellen inneholder fakta om eierforhold som kommer fra MatrikkelAPI og beskriver de eierforholdene som ikke er tinglyst. Tabellen er slått sammen av de ulike eierforholdtypene juridiskpersonikketinglysteierforhold, kontaktinstans, matrikkelenhetikketinglysteierforhold og personikketinglysteierforhold. Data inneholder historikk basert på endringslogg for matrikkelenhet fra matrikkelen. Id for selve objektene vil være eierforholdId. Fordi dette er en historisk tabell vil flere rader kunne ha samme eierforholdId, man må da bruke et tidspunkt, for eksempel oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne for å skille mellom unike rader, som er en kombinasjon av eierforholdId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Koblingskolonner til dimensjoner er prefikset med zk_. Systemkolonner er prefikset med zx_. MatrikkelenhetId er ikke unik per eierforhold da en matrikkelenhet kan ha flere eierforhold, men hvert eierforhold har en egen eierforholdId. Eierforhold kan derfor kobles mot dim_matrikkelenhet ved å bruke zk_matrikkelenhetId.

**Schema:**

| Column | Type |
|--------|------|
| eierforholdId | bigint |
| UUID | struct<navnerom:string,uuid:string> |
| andelNevner | bigint |
| andelTeller | bigint |
| datoFra | string |
| datoTil | string |
| drop_me_endringslogg_zx_ingest_timestamp | timestamp |
| eierforholdId_historical | string |
| eierforholdType | string |
| endringstype | string |
| metadata | struct<item:array<string>> |
| oppdateringsdato | timestamp |
| zk_eiendeMatrikkelenhetId | bigint |
| zk_eierId | bigint |
| zk_eierforholdKodeId | bigint |
| zk_kommuneId | bigint |
| zk_matrikkelenhetId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_kulturminner

**Description:**
Tabellen inneholder fakta om kulturminner som stammer fra MatrikkelAPI. Opplysninger om kulturminner kan blant annet gjelde automatisk fredete kulturminner, vedtaksfredete kulturminner og kulturmiljø. Opplysninger om kulturminner vil framkomme som utdrag eller kopling mot Riksantikvarens register over kulturminner, Askeladden. Regler om dette fastsettes i avtale mellom Riksantikvaren og Statens kartverk. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx_

**Schema:**

| Column | Type |
|--------|------|
| kulturminneId | bigint |
| zk_matrikkelenhetIds | array<struct<value:bigint>> |
| oppdateringsdato | timestamp |
| zk_kulturminneArtKodeId | bigint |
| zk_kulturminnekategoriId | bigint |
| zk_vernetypeKodeId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"7","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_kulturminner_encrypted

**Description:**
Tabellen inneholder krypterte fakta om kulturminner som stammer fra MatrikkelAPI. Opplysninger om kulturminner kan blant annet gjelde automatisk fredete kulturminner, vedtaksfredete kulturminner og kulturmiljø. Opplysninger om kulturminner vil framkomme som utdrag eller kopling mot Riksantikvarens register over kulturminner, Askeladden. Regler om dette fastsettes i avtale mellom Riksantikvaren og Statens kartverk. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx_

**Schema:**

| Column | Type |
|--------|------|
| kulturminnerId | bigint |
| keyId | string |
| matrikkelenhetIds | array<struct<value:bigint>> |
| oppdateringsdato | timestamp |
| zk_kulturminneArtKodeId | bigint |
| zk_kulturminnekategoriId | bigint |
| zk_vernetypeKodeId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_kulturminner_historical

**Description:**
Tabellen inneholder fakta om kultummer som stammer fra MatrikkelAPI. Opplysninger om kulturminner kan blant annet gjelde automatisk fredete kulturminner, vedtaksfredete kulturminner og kulturmiljø. Opplysninger om kulturminner vil framkomme som utdrag eller kopling mot Riksantikvarens register over kulturminner, Askeladden. Regler om dette fastsettes i avtale mellom Riksantikvaren og Statens kartverk. Data rensket for duplikater, men inneholder historikk basert på endringslogg fra matrikkelen. Iden for selve objektene vil være kulturminnerId. Fordi dette er en historisk tabell vil flere rader kunne ha samme kulturminnerId, man må da bruke et tidspunkt f.eks bruke oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av kulturminnerId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__

**Schema:**

| Column | Type |
|--------|------|
| kulturminneId | bigint |
| endringstype | string |
| kulturminneId_historical | string |
| zk_matrikkelenhetIds | array<struct<value:bigint>> |
| oppdateringsdato | timestamp |
| zk_kulturminneArtKodeId | bigint |
| zk_kulturminnekategoriId | bigint |
| zk_vernetypeKodeId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"9","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_matrikkelenhet

**Description:**
Tabellen inneholder fakta om matrikkelenheter som stammer fra MatrikkelAPI. De ulike matrikkelenhetene kommer som egne matrikkelbobler fra APIet, men er slått sammen i denne tabellen. Det kan derfor være noen kolonner som ikke inneholder noen data (har null i verdi) for visse type matrikkelenheter, da dette ikke er relevant for den aktuelle typen. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Koblingskolonner til dimensjoner er prefikset med zk_. Systemkolonner er prefikset med zx_

**Schema:**

| Column | Type |
|--------|------|
| matrikkelenhetId | bigint |
| bruksnavn | string |
| drop_me_endringslogg_zx_ingest_timestamp | timestamp |
| eierforhold | struct<item:array<struct<andel:struct<nevner:bigint,teller:bigint>,andelsnummer:bigint,datoFra:struct<date:string>,datoTil:struct<date:string>,eiendeMatrikkelenhetId:struct<value:bigint>,eierId:struct<value:bigint>,eierforholdKodeId:struct<value:bigint>,id:bigint,kommuneId:struct<value:bigint>,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,uuid:struct<navnerom:string,uuid:string>,versjonId:bigint>>> |
| erSeksjonert | boolean |
| grensepunktmerkingMangler | boolean |
| harAktiveFestegrunner | boolean |
| harAnmerketKlage | boolean |
| harAvtaleGrensePunktfeste | boolean |
| harAvtaleStedbundenRettighet | boolean |
| harGrunnforurensing | boolean |
| harKulturminne | boolean |
| harRegistrertGrunnerverv | boolean |
| harRegistrertJordskifteKrevd | boolean |
| historiskOppgittAreal | double |
| inngarISamlaFastEiendom | boolean |
| kommunalTilleggsdel | struct<brukAvGrunnKodeId:struct<value:bigint>,metadata:struct<item:array<string>>> |
| mangelMatrikkelforingsKrav | boolean |
| matrikkelenhetType | string |
| nymatrikulert | boolean |
| oppdateringsdato | timestamp |
| oppmalingIkkeFullfort | boolean |
| skyld | double |
| tinglyst | boolean |
| underSammenslaingBestar | boolean |
| underSammenslaingUtgar | boolean |
| utgatt | boolean |
| zk_historiskArealkildeId | bigint |
| zk_kommuneId | bigint |
| zk_teigerForMatrikkelenhet | array<struct<hovedteig:boolean,id:bigint,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,teigId:struct<value:bigint>,uuid:struct<navnerom:string,uuid:string>,versjonId:bigint>> |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_matrikkelenhet_historical

**Description:**
Tabellen inneholder fakta om matrikkelenheter som stammer fra MatrikkelAPI. De ulike matrikkelenhetene kommer som egne matrikkelbobler fra APIet, men er slått sammen i denne tabellen. Det kan derfor være noen kolonner som ikke inneholder noen data (har null i verdi) for visse type matrikkelenheter, da dette ikke er relevant for den aktuelle typen. Data rensket for duplikater, men inneholder historikk basert på endringslogg fra matrikkelen. Iden for selve objektene vil være matrikkelenhetId. Fordi dette er en historisk tabell vil flere rader kunne ha samme matrikkelenhetId, man må da bruke et tidspunkt f.eks bruke oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av matrikkelenhetId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Koblingskolonner til dimensjoner er prefikset med zk_. Systemkolonner er prefikset med zx_

**Schema:**

| Column | Type |
|--------|------|
| matrikkelenhetId | bigint |
| bruksnavn | string |
| drop_me_endringslogg_zx_ingest_timestamp | timestamp |
| eierforhold | struct<item:array<struct<andel:struct<nevner:bigint,teller:bigint>,andelsnummer:bigint,datoFra:struct<date:string>,datoTil:struct<date:string>,eiendeMatrikkelenhetId:struct<value:bigint>,eierId:struct<value:bigint>,eierforholdKodeId:struct<value:bigint>,id:bigint,kommuneId:struct<value:bigint>,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,uuid:struct<navnerom:string,uuid:string>,versjonId:bigint>>> |
| endringstype | string |
| erSeksjonert | boolean |
| grensepunktmerkingMangler | boolean |
| harAktiveFestegrunner | boolean |
| harAnmerketKlage | boolean |
| harAvtaleGrensePunktfeste | boolean |
| harAvtaleStedbundenRettighet | boolean |
| harGrunnforurensing | boolean |
| harKulturminne | boolean |
| harRegistrertGrunnerverv | boolean |
| harRegistrertJordskifteKrevd | boolean |
| historiskOppgittAreal | double |
| inngarISamlaFastEiendom | boolean |
| kommunalTilleggsdel | struct<brukAvGrunnKodeId:struct<value:bigint>,metadata:struct<item:array<string>>> |
| mangelMatrikkelforingsKrav | boolean |
| matrikkelenhetId_historical | string |
| matrikkelenhetType | string |
| nymatrikulert | boolean |
| oppdateringsdato | timestamp |
| oppmalingIkkeFullfort | boolean |
| skyld | double |
| tinglyst | boolean |
| underSammenslaingBestar | boolean |
| underSammenslaingUtgar | boolean |
| utgatt | boolean |
| zk_historiskArealkildeId | bigint |
| zk_kommuneId | bigint |
| zk_teigerForMatrikkelenhet | array<struct<hovedteig:boolean,id:bigint,metadata:struct<item:array<string>>,oppdateringsdato:struct<timestamp:string>,oppdatertAv:string,teigId:struct<value:bigint>,uuid:struct<navnerom:string,uuid:string>,versjonId:bigint>> |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_teig

**Description:**
Tabellen inneholder fakta om teig som stammer fra MatrikkelAPI. En teig er et sammenhengende areal som avgrenses av teiggrense. Teiger skal ikke overlappe hverandre. Naboteiger skal ha delt geometri. Matrikkelenheter som består av flere areal som er sammenhengende i bare et punkt er teigdelt etter denne definisjonen. Koordinatsystemet som benyttes er koordinatSystemKodeId 11, som refererer til EUREF89 UTM Sone 33. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__. Oppdateringsdato brukes for å sikre at dataene er de nyeste tilgjengelige.

**Schema:**

| Column | Type |
|--------|------|
| teigId | bigint |
| lagretBeregnetAreal | double |
| oppdateringsdato | timestamp |
| zk_kommuneIdsForEndring | array<bigint> |
| zk_teigarealmerknadIds | array<bigint> |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_teig_historical

**Description:**
Tabellen inneholder fakta om teig som stammer fra MatrikkelAPI. En teig er et sammenhengende areal som avgrenses av teiggrense. Teiger skal ikke overlappe hverandre. Naboteiger skal ha delt geometri. Matrikkelenheter som består av flere areal som er sammenhengende i bare et punkt er teigdelt etter denne definisjonen. Koordinatsystemet som benyttes er koordinatSystemKodeId 11, som refererer til EUREF89 UTM Sone 33. Data rensket for duplikater, men inneholder historikk basert på endringslogg fra matrikkelen. Iden for selve objektene vil være teigId. Fordi dette er en historisk tabell vil flere rader kunne ha samme teigId, man må da bruke et tidspunkt f.eks bruke oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av teigId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__

**Schema:**

| Column | Type |
|--------|------|
| teigId | bigint |
| endringstype | string |
| lagretBeregnetAreal | double |
| oppdateringsdato | timestamp |
| teigId_historical | string |
| zk_kommuneIdsForEndring | array<bigint> |
| zk_teigarealmerknadIds | array<bigint> |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":null,"delta.columnMapping.mode":null,"delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_teiggrensepunkt

**Description:**
Tabellen inneholder fakta om teiggrensepunkt som stammer fra MatrikkelAPI. Et teiggrensepunkt er start- og endepunktene til en teiggrense. Koordinatsystemet som benyttes er koordinatSystemKodeId 11, som refererer til EUREF89 UTM Sone 33. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__. Oppdateringsdato brukes for å sikre at dataene er de nyeste tilgjengelige.

**Schema:**

| Column | Type |
|--------|------|
| teiggrensepunktId | bigint |
| zk_grensemerkeNedsattId | bigint |
| zk_grensepunkttypeId | bigint |
| zk_koordinatsystemKodeId | bigint |
| kvalitetmalemetodeId | bigint |
| oppdateringsdato | timestamp |
| zk_originalKoordinatsystemKodeId | bigint |
| versjon | bigint |
| versjonId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"9","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_teiggrensepunkt_historical

**Description:**
Tabellen inneholder fakta om teiggrensepunkt som stammer fra MatrikkelAPI. Et teiggrensepunkt er start- og endepunktene til en teiggrense. Koordinatsystemet som benyttes er koordinatSystemKodeId 11, som refererer til EUREF89 UTM Sone 33. Iden for selve objektene vil være teiggrensepunktId. Fordi dette er en historisk tabell vil flere rader kunne ha samme teiggrensepunktId, man må da bruke et tidspunkt f.eks bruke oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av teiggrensepunktId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__

**Schema:**

| Column | Type |
|--------|------|
| teiggrensepunktId | bigint |
| endringstype | string |
| zk_grensemerkeNedsattId | bigint |
| zk_grensepunkttypeId | bigint |
| zk_koordinatsystemKodeId | bigint |
| kvalitetmalemetodeId | bigint |
| oppdateringsdato | timestamp |
| zk_originalKoordinatsystemKodeId | bigint |
| teiggrensepunktId_historical | string |
| versjon | bigint |
| versjonId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"11","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_teiggrenser

**Description:**
Tabellen inneholder fakta om teiggrensepunkt som stammer fra MatrikkelAPI. Et teiggrensepunkt er start- og endepunktene til en teiggrense. Koordinatsystemet som benyttes er koordinatSystemKodeId 11, som refererer til EUREF89 UTM Sone 33. Data er deduplisert til å vise nåtidsbilde fra matrikkelen basert på siste innlesing fra endringslogg. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__. Oppdateringsdato brukes for å sikre at dataene er de nyeste tilgjengelige.

**Schema:**

| Column | Type |
|--------|------|
| teiggrenseId | bigint |
| zk_administrativGrenseKodeId | bigint |
| folgerTerrengdetaljId | bigint |
| zk_hjelpelinjetypeId | bigint |
| kvalitetmalemetodeId | bigint |
| lagretnoyaktighetsklasseId | bigint |
| omtvistet | boolean |
| oppdateringsdato | timestamp |
| versjon | bigint |
| versjonId | bigint |
| zk_endepunktId | bigint |
| zk_startpunktId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"12","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---

## fact_teiggrenser_historical

**Description:**
Tabellen inneholder fakta om teiggrenser som stammer fra MatrikkelAPI. En teiggrense vil avgrense en teig. Koordinatsystemet som benyttes er koordinatSystemKodeId 11, som refererer til EUREF89 UTM Sone 33. Data rensket for duplikater, men inneholder historikk basert på endringslogg fra matrikkelen. Iden for selve objektene vil være teiggrenseId. Fordi dette er en historisk tabell vil flere rader kunne ha samme teiggrenseId, man må da bruke et tidspunkt f.eks bruke oppdateringsdato eller ingest_dato for å få unik rad. Av tekniske årsaker finnes det en egen kolonne som heter key for å skille mellom unike rader, som er en kombinasjon av teiggrenseId og oppdateringsdato på raden. Kolonnene er sortert alfabetisk. Kan benyttes sammen med flere dimensjoner, hvilke dimensjoner dette er kan sees ved å se på kolonner prefiksen med zk_. fact_teiggrenser kan for eksempel kobles til dim_teiggrensepunkt via zk_startpunktId og zk_endepunktId mot teiggrensepunktId. Tilhørende dimensjon kobles opp ved hjelp av å joine på denne zk_ kolonnen. Systemkolonner er prefikset med zx__

**Schema:**

| Column | Type |
|--------|------|
| teiggrenseId | bigint |
| zk_administrativGrenseKodeId | bigint |
| endringstype | string |
| folgerTerrengdetaljId | bigint |
| zk_hjelpelinjetypeId | bigint |
| kvalitetmalemetodeId | bigint |
| lagretnoyaktighetsklasseId | bigint |
| omtvistet | boolean |
| oppdateringsdato | timestamp |
| teiggrenseId_historical | string |
| versjon | bigint |
| versjonId | bigint |
| zk_endepunktId | bigint |
| zk_startpunktId | bigint |

**Properties:**
```json
{"delta.columnMapping.maxColumnId":"14","delta.columnMapping.mode":"name","delta.enableChangeDataFeed":"true","delta.enableDeletionVectors":"false"}
```

---
