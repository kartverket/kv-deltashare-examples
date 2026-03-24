# External Table Documentation - Grunnbok

### Generelt

Dimensjonstabeller er implementert med Slowly Changing Dimensions type 2 (SCD2)-historikk. Det innebærer at hver rad har et gyldighetsintervall angitt ved _from_datetime_ og _to_datetime_. Tidligste mulige _from_datetime_ er 2017-04-13. dim_fysisk_person_encrypted har ikke historikk.

Kolonner med prefiks zk\_ angir fremmednøkler. For eksempel er _zk_kommuneId_ fremmednøkkel til tabell _dim_kommune_ og kan joines på dens primærnøkkel _kommuneId_. Kolonner med prefiks zx\_ angir interne systemkolonner, for eksempel zx_ingest_timestamp som angir tidspunktet raden ble lastet inn på dataplattformen.

Boolske verdier er oppgitt som et tall, 0 eller 1. De tolkes 0 = False, 1 = True.

Se domenemodellen for mer informasjon: https://grunnbok.no/grunnbok/modell/grunnbok-domene-v2-modell/index.html

---

### Krypterte tabeller

Tabeller med suffiks \_encrypted er krypterte tabeller som kan inneholde persondata. Alle kolonner bortsett fra kolonner som er nødvendige for intern databehandling er krypterte, uavhengig av om kolonnen i seg selv inneholder persondata eller ikke.

Kolonne _keyId_ angir id til krypteringsnøkkelen som kan brukes til å dekryptere den angitte kolonnen. Krypteringsnøkler finnes i egne tabeller med navn keys_encrypted\_{deltasharereferanse}, èn tabell for hver deltashare.

Alle krypterte verdier blir strings i krypteringsprosessen, og må tolkes av konsument etter dekryptering. Tabellene i denne oversikten angir den logiske datatypen til krypterte verdier - altså slik de skal tolkes etter dekryptering.

---

## Table of Contents

### Dimension Tables

- [dim_adresse_encrypted](#dim_adresse_encrypted)
- [dim_aarsaksgebyrfritakkode](#dim_aarsaksgebyrfritakkode)
- [dim_aarsaksparagrafkode](#dim_aarsaksparagrafkode)
- [dim_anketypekode](#dim_anketypekode)
- [dim_boligtypekode](#dim_boligtypekode)
- [dim_borettslag](#dim_borettslag)
- [dim_brukstypekode](#dim_brukstypekode)
- [dim_delavrett](#dim_delavrett)
- [dim_delavrett_til_registerenhetsrett](#dim_delavrett_til_registerenhetsrett)
- [dim_delavrett_til_registerenhetsrettsandel](#dim_delavrett_til_registerenhetsrettsandel)
- [dim_dokument](#dim_dokument)
- [dim_dokumentstatuskode](#dim_dokumentstatuskode)
- [dim_dokavgiftsaarsakkode](#dim_dokavgiftsaarsakkode)
- [dim_embetekode](#dim_embetekode)
- [dim_fysisk_person_encrypted](#dim_fysisk_person_encrypted)
- [dim_identifikasjonsnummertypekode](#dim_identifikasjonsnummertypekode)
- [dim_juridisk_person](#dim_juridisk_person)
- [dim_kommune](#dim_kommune)
- [dim_omsetning_encrypted](#dim_omsetning_encrypted)
- [dim_omsetningstypekode](#dim_omsetningstypekode)
- [dim_omsattregisterenhetsrett_encrypted](#dim_omsattregisterenhetsrett_encrypted)
- [dim_overfoering_omfatter_encrypted](#dim_overfoering_omfatter_encrypted)
- [dim_periodekode](#dim_periodekode)
- [dim_registerenhet](#dim_registerenhet)
- [dim_registerenhetsrett](#dim_registerenhetsrett)
- [dim_registerenhetsrettsandel_encrypted](#dim_registerenhetsrettsandel_encrypted)
- [dim_registerenhetsrettstypekode](#dim_registerenhetsrettstypekode)
- [dim_registerenhettypekode](#dim_registerenhettypekode)
- [dim_rettsstiftelse](#dim_rettsstiftelse)
- [dim_saksinformasjon](#dim_saksinformasjon)
- [dim_saksinformasjon_behandlingsutfallkode](#dim_saksinformasjon_behandlingsutfallkode)
- [dim_saksinformasjon_saksstatuskode](#dim_saksinformasjon_saksstatuskode)
- [dim_saksperson_encrypted](#dim_saksperson_encrypted)
- [dim_valutakode](#dim_valutakode)

### Fact Tables

- [fact_dokument](#fact_dokument)
- [fact_omsetning_beloep_encrypted](#fact_omsetning_beloep_encrypted)
- [fact_omsetning_encrypted](#fact_omsetning_encrypted)
- [fact_overfoering_encrypted](#fact_overfoering_encrypted)
- [fact_registerenhet](#fact_registerenhet)
- [fact_registerenhetsrettsandel_encrypted](#fact_registerenhetsrettsandel_encrypted)
- [fact_rettsstiftelse](#fact_rettsstiftelse)
- [fact_rettsstiftelse_beloep](#fact_rettsstiftelse_beloep)
- [fact_rettsstiftelse_beloepforperiode](#fact_rettsstiftelse_beloepforperiode)

---

## DIMENSION TABLES

---

### dim_adresse_encrypted

**Description:**

Tabellen inneholder alle adresser lagret i Grunnboken. Tabellen inkluderer kategoriene UtenlandskAdresse, Vegadresse, Matrikkeladresser og KonvertertAdresse.

Vegadresser og Matrikkeladresser har kilde i matrikkelen. Disse kan knyttes til dim_adresse fra matrikkelen med zk_matrikkel_adresseId, til fact_bruksenheter med zk_matrikkel_bruksenhetId eller til dim_matrikkelenhet med kommunenummer, gaardsnummer, bruksnummer, festenummer og/eller undernummer.

**Schema:**

| Column                    | Type      | Comment                                           |
| ------------------------- | --------- | ------------------------------------------------- |
| adresseId                 | bigint    | Primærnøkkel                                      |
| zk_matrikkel_adresseId    | bigint    | Fremmednøkkel til dim_adresse i matrikkelen       |
| zk_matrikkel_bruksenhetId | bigint    | Fremmednøkkel til fact_bruksenheter i matrikkelen |
| zk_landkodekodeid         | bigint    | Fremmednøkkel til dim_landkodekode                |
| zk_kommuneid              | bigint    | Fremmednøkkel dim dim_kommune                     |
| adresseKategori           | string    |
| bolignummer               | int       |
| adressekode               | string    |
| adressenavn               | string    |
| husnummer                 | int       |
| bokstav                   | string    |
| gaardsnummer              | int       | Likt gårdsnummer i matrikkelen                    |
| bruksnummer               | int       | Likt bruksnummer i matrikkelen                    |
| festenummer               | int       | Likt festenummer i matrikkelen                    |
| undernummer               | int       | Likt undernummer i matrikkelen                    |
| adressetekst              | string    |
| keyId                     | bigint    |
| oppdateringsdato          | timestamp |
| from_datetime             | timestamp |
| to_datetime               | timestamp |
| zx_ingest_timestamp       | timestamp |

---

### dim_aarsaksgebyrfritakkode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser for årsaker til gebyrfritak. Tabellen refereres til fra fact_rettsstiftelse.

**Schema:**

| Column                   | Type      | Comment      |
| ------------------------ | --------- | ------------ |
| aarsaksgebyrfritakkodeid | bigint    | Primærnøkkel |
| aarsaksgebyrfritak       | string    |
| oppdateringsdato         | timestamp |
| from_datetime            | timestamp |
| to_datetime              | timestamp |

---

### dim_aarsaksparagrafkode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser for årsaksparagrafen. Tabellen refereres til fra fact_rettsstiftelse.

**Schema:**

| Column                | Type      | Comment      |
| --------------------- | --------- | ------------ |
| aarsaksparagrafkodeid | bigint    | Primærnøkkel |
| aarsaksparagraf       | string    |
| oppdateringsdato      | timestamp |
| from_datetime         | timestamp |
| to_datetime           | timestamp |

---

### dim_anketypekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser for typen avgjørelse en anke gjelder, for eksempel "Anke over nektig". Tabellen refereres til fra fact_rettsstiftelse.

**Schema:**

| Column           | Type      | Comment      |
| ---------------- | --------- | ------------ |
| anketypekodeid   | bigint    | Primærnøkkel |
| anketype         | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_boligtypekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over boligtyper, altså hva en registerenhetsretts eventuelle bebyggelse kan anvendes til. Tabellen er referert til fra dim_omsattregisterenhetsrett_encrypted.

**Schema:**

| Column           | Type      | Comment      |
| ---------------- | --------- | ------------ |
| boligtypekodeid  | bigint    | Primærnøkkel |
| boligtype        | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_borettslag

**Description:**

Borettslag er ”eit samvirkeføretak som har til føremål å gi andelseigarane bruksrett til eigen bustad i føretakets eigedom (burett)”, jf. burettslagslova § 1-1 første ledd. zk_personId knytter til dim_juridisk_person (for organisasjonsnummer) eller dim_fysisk_person_encrypted (for løpenummer) og angir Borettslagets organisasjons- eller løpenummer.

**Schema:**

| Column              | Type      | Comment                                                                 |
| ------------------- | --------- | ----------------------------------------------------------------------- |
| borettslagId        | bigint    | Primærnøkkel                                                            |
| zk_personId         | bigint    | Fremmednøkkel til dim_juridisk_person eller dim_fysisk_person_encrypted |
| historisk           | boolean   |
| oppdateringsdato    | timestamp |
| from_datetime       | timestamp |
| to_datetime         | timestamp |
| zx_ingest_timestamp | timestamp |

---

### dim_brukstypekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over brukstyper, altså hva en registerenhetsrett kan anvendes til. Tabellen er referert til fra dim_omsattregisterenhetsrett_encrypted.

**Schema:**

| Column           | Type      | Comment      |
| ---------------- | --------- | ------------ |
| brukstypekodeid  | bigint    | Primærnøkkel |
| brukstype        | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_delavrett

**Description:**

Del av en rett som er etablert i en rettsstiftelse. Rettsstiftelsene av kategori "HeftelseIRettihet" og "TvangsforretningIRettighet" hefter i andre rettsstiftelser, og delAvRett angir denne rettsstiftelsen samt eventuelle begrensninger til registerenhetsrett eller registerenhetsrettsandel.

zk_kilde_rettsstiftelseId angir hvilken rettsstiftelsen DelAvRett har opphav i.

zk_maal_rettsstiftelseId angir hvilken rettsstiftelsen DelAvRett er knyttet til.

Registerenhetsrett som DelAvRett er begrenset til er angitt i tabellen dim_delavrett_til_registerenhetsrett_encrypted.

Registerenhetsrettsandel som DelAvRett er begrenset til er angitt i tabellen dim_delavrett_til_registerenhetsrettsandel_encrypted.

**Schema:**

| Column                    | Type      | Comment                               |
| ------------------------- | --------- | ------------------------------------- |
| delavrettId               | bigint    | Primærnøkkel                          |
| zk_kilde_rettsstiftelseId | bigint    | Fremmednøkkel til fact_rettsstiftelse |
| zk_maal_rettsstiftelseId  | bigint    | Fremmednøkkel til fact_rettsstiftelse |
| oppdateringsdato          | timestamp |
| from_datetime             | timestamp |
| to_datetime               | timestamp |
| zx_ingest_timestamp       | timestamp |

---

### dim_delavrett_til_registerenhetsrett_encrypted

**Description:**

Denne tabellen angir hvilke registerenhetsretter en rettsstiftelse er begrenset til. Denne tabellen gjelder hvis en rettsstiftelse er begrenset til alle andelene i en registerenhetsrett. Hvis en rettsstiftelse er begrenset til en eller flere registerenhetsrettsandeler, men ikke alle, vil den finnes i dim_delavrett_til_registerenhetsrettsandel_encrypted.

zk_delavrettId angir DelAvRett og zk_registerenhetsrettsId angir registerenhetsrett som DelAvRett er begrenset til. Den korresponderende rettsstiftelsen kan finnes i dim_delavrett.

**Schema:**

| Column                           | Type      | Comment                                  |
| -------------------------------- | --------- | ---------------------------------------- |
| delavrettTilRegisterenhetsrettId | bigint    | Primærnøkkel                             |
| zk_delavrettId                   | bigint    | Fremmednøkkel til dim_delavrett          |
| zk_registerenhetsrettId          | bigint    | Fremmednøkkel til dim_registerenhetsrett |
| keyId                            | bigint    |
| oppdateringsdato                 | timestamp |
| from_datetime                    | timestamp |
| to_datetime                      | timestamp |
| zx_ingest_timestamp              | timestamp |

---

### dim_delavrett_til_registerenhetsrettsandel_encrypted

**Description:**

Denne tabellen angir hvilke registerenhetsrettsandeler en rettsstiftelse er begrenset til. Denne tabellen gjelder når en rettsstiftelse er begrenset til en eller flere andeler av en registerenhetsrett, men ikke samtlige andeler. Hvis en rettsstiftelse er begrenset til en hel registerenhetsrett vil den finnes i dim_delavrett_til_registerenhetsrett_encrypted.

zk_delavrettId angir DelAvRett og zk_registerenhetsrettsandelId angir registerenhetsrettsandel som DelAvRett er begrenset til. Den korresponderende rettsstiftelsen kan finnes i dim_delavrett.

**Schema:**

| Column                                 | Type      | Comment                                         |
| -------------------------------------- | --------- | ----------------------------------------------- |
| delavrettTilRegisterenhetsrettsandelId | bigint    | Primærnøkkel                                    |
| zk_delavrettId                         | bigint    | Fremmednøkkel til dim_delavrett                 |
| zk_registerenhetsrettsandelId          | bigint    | Fremmednøkkel til fact_registerenhetsrettsandel |
| keyId                                  | bigint    |
| oppdateringsdato                       | timestamp |
| from_datetime                          | timestamp |
| to_datetime                            | timestamp |
| zx_ingest_timestamp                    | timestamp |

---

### dim_dokument

**Description:**

Denne tabellen inneholder dimensjonsdata om dokumenter. Data om dokumenter er delt i en dimensjontabell (dim_dokument) og en faktatabell (fact_dokument).

Det er dokumenter som tinglyses, og et dokument kan inneholde flere bestemmelser som skal tinglyses. Hver slik bestemmelse registreres inn som en rettsstiftelse tilhørende dokumentet. En rettsstiftelse har altså hverken selvstendig dato eller tinglyststatus, det er dokumentets dato og status som gjelder.

zk_dokumentId i fact_rettsstiftelse angir rettsstiftelsens dokument. registreringstidspunkt i fact_dokument angir dokumentets dato. zk_dokumentstatusKodeId i fact_dokument knyttes til dim_dokumentstatuskode for å angi dokumentets status (f.eks. "tinglyst").

**Schema:**

| Column              | Type      | Comment      |
| ------------------- | --------- | ------------ |
| dokumentId          | bigint    | Primærnøkkel |
| dokumentaar         | int       |
| dokumentnummer      | int       |
| datoregistrert      | boolean   |
| historisk           | boolean   |
| oppdateringsdato    | timestamp |
| from_datetime       | timestamp |
| to_datetime         | timestamp |
| zx_ingest_timestamp | timestamp |

---

### dim_dokumentavgiftsaarsakkode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over årsaker til at dokumentavgiften er beregnet på den aktuelle måten, enten dette er hovedregelen om full dokumentavgift, nedsatt dokumentavgift, eller fritak fra dokumentavgift. Tabellen refereres til fra fact_omsetning_encrypted.

**Schema:**

| Column                      | Type      | Comment      |
| --------------------------- | --------- | ------------ |
| dokumentavgiftsaarsakkodeid | bigint    | Primærnøkkel |
| dokumentavgiftsaarsak       | string    |
| oppdateringsdato            | timestamp |
| from_datetime               | timestamp |
| to_datetime                 | timestamp |

---

### dim_dokumentstatuskode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over offisielle dokumentstatuser tinglysingsdokumentene kan ha. Tabellen refereres til fra dim_dokument.

**Schema:**

| Column               | Type      | Comment      |
| -------------------- | --------- | ------------ |
| dokumentstatuskodeid | bigint    | Primærnøkkel |
| dokumentstatus       | string    |
| oppdateringsdato     | timestamp |
| from_datetime        | timestamp |
| to_datetime          | timestamp |

---

### dim_embetekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over alle embetenummer i kildesystemet. Tinglysingen lå tidligere ved domstolene. Disse er/var organisert i ulike embeter, hvor flere kommuner kunne sogne til et embete. Flere dokumenter kan derfor ha samme årstall og dokumentnummer, men er altså ført i ulike embeter. Dette er grunnen til at embete må med som identifikasjon av dokumentet.

Dokumenter som tinglyses i dag i fast eiendom har embetenummer 200, i borett 201.

**Schema:**

| Column           | Type      | Comment      |
| ---------------- | --------- | ------------ |
| embetekodeid     | bigint    | Primærnøkkel |
| embete           | string    | Embetenummer |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_fysisk_person_encrypted

**Description:**

Tabellen inneholder alle fysiske personer som er registrert i grunnboksdatabasen. Tabellen inneholder både personer med fødselsnummer og med løpenummer (sistnevne kan være både fysiske og juridiske personer).

Merk, denne dimensjonstabellen har _ikke_ SCD2-historikk.

**Schema:**

| Column                             | Type      | Comment                                             |
| ---------------------------------- | --------- | --------------------------------------------------- |
| fysiskPersonId                     | bigint    | Primærnøkkel                                        |
| zk_identifikasjonsnummerTypeKodeId | bigint    | Fremmednøkkel til dim_identifikasjonsnummertypekode |
| identifikasjonsnummer              | string    |
| navn                               | string    |
| historisk                          | boolean   |
| keyId                              | bigint    |
| oppdateringsdato                   | timestamp |
| zx_ingest_timestamp                | timestamp |

---

### dim_identifikasjonsnummertypekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser for identifikasjonsnummertyper, som kan være fødselsnummer (herunder også D-nummer), organisasjonsnummer eller løpenummer. Løpenummer er internt opprettede identifikasjonsnummer der fødselsnummer eller organisasjonsnummer mangler, og kan være tilknyttet til fysiske personer eller organisasjoner.

**Schema:**

| Column                          | Type      | Comment      |
| ------------------------------- | --------- | ------------ |
| identifikasjonsnummertypekodeid | bigint    | Primærnøkkel |
| identifikasjonsnummertype       | string    |
| oppdateringsdato                | timestamp |
| from_datetime                   | timestamp |
| to_datetime                     | timestamp |

---

### dim_juridisk_person

**Description:**

Tabellen inneholder juridiske personer som er registrert i grunnboksdatabasen. Tabellen inneholder bare juridiske personer med organisasjonsnummer. Juridiske personer med løpenummer er inneholdt i dim_fysisk_person_encrypted.

**Schema:**

| Column                             | Type      | Comment                                             |
| ---------------------------------- | --------- | --------------------------------------------------- |
| juridiskPersonId                   | bigint    | Primærnøkkel                                        |
| zk_identifikasjonsnummerTypeKodeId | bigint    | Fremmednøkkel til dim_identifikasjonsnummertypekode |
| identifikasjonsnummer              | string    | Organisasjonsnummer                                 |
| navn                               | string    |
| historisk                          | boolean   |
| oppdateringsdato                   | timestamp |
| from_datetime                      | timestamp |
| to_datetime                        | timestamp |
| zx_ingest_timestamp                | timestamp |

---

### dim_kommune

**Description:**

Tabellen inneholder norske kommuner med kommunenummer og navn, både historiske og nåværende. _historisk_ = 1 angir om kommunen er historisk. _historisk_ = 0 er en nåværende kommune.

**Schema:**

| Column              | Type      | Comment                 |
| ------------------- | --------- | ----------------------- |
| kommuneId           | bigint    | Primærnøkkel            |
| kommunenummer       | string    | Kommunenummer, 4 siffer |
| navn                | string    | Kommunenavn             |
| historisk           | boolean   |
| oppdateringsdato    | timestamp |
| from_datetime       | timestamp |
| to_datetime         | timestamp |
| zx_ingest_timestamp | timestamp |

---

### dim_omsetning_encrypted

**Description:**

Denne tabellen inneholder omsetninger. En omsetning er kjøp og salg (eller annen type overdragelse, eks skifteoppgjør) av registerenhetsretter eller registerenhetsrettsandeler. I de fleste tilfeller skjer omsetningen ved at noen kjøper eller på annen måte erverver registerenhetsrettsandeler av de som er rettighetshavere til registerenhetsretten. Men omsetningen kan også skje på andre måter.

Ved Arealoverføring mellom matrikkelenheter skjer det en omsetning, og det kan bli beregnet dokumentavgift. Det blir imidlertid ikke omsatt Registerenhetsrettsandeler, da hjemmelsforholdene ikke endres. Det som endres er det arealet man har registerenhetsrett til.

Det samme gjelder ved endring av sameiebrøk mellom seksjoner i et seksjonssameie. Verdier flyttes da mellom seksjonene.

Informasjon om registerenhetsrettene som er omsatt under en omsetning finnes i dim_omsattregisterenhetsrett_encrypted, som kan knyttes til omsetning med sin fremmednøkkel zk_omsetningId.

Informasjon om registerenhetsrettsandelene som er omsatt under en omsetning finnes i dim_omsattregisterenhetsrettsandel_encrypted. Omsattregisterenhetsrettsandel kan knyttes til omsetning via dim_omsattregisterenhetsrett_encrypted med fremmednøkkelen zk_omsattregisterenhetsrettId.

Beløp knyttet til en omsetning ligger i fact_omsetning_beloep_encrypted, som knyttes til dim_omsetning/fact_omsetning ved zk_omsetningId. Hvilke registerenhetsretter som er omsatt kan finnes i dim_omsattregisterenhetsrett_encrypted.

**Schema:**

| Column                        | Type      | Comment      |
| ----------------------------- | --------- | ------------ |
| omsetningId                   | bigint    | Primærnøkkel |
| omsetningKategori             | string    |
| utlysttilsalgpaadetfriemarked | boolean   |
| hardokumentavgift             | boolean   |
| keyId                         | bigint    |
| oppdateringsdato              | timestamp |
| from_datetime                 | timestamp |
| to_datetime                   | timestamp |
| zx_ingest_timestamp           | timestamp |

---

### dim_landkodekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser for landkoder. Landkoder er to bokstaver, for eksempel "NO" for Norge.

**Schema:**

| Column           | Type      | Comment      |
| ---------------- | --------- | ------------ |
| landkodekodeid   | bigint    | Primærnøkkel |
| landkode         | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_omsetningstypekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over omsetningstyper, altså nærmere hva som er årsaken til at registerenhetsretten skifter hjemmelshaver. Tabellen refereres til fra fact_omsetning_encrypted.

**Schema:**

| Column               | Type      | Comment      |
| -------------------- | --------- | ------------ |
| omsetningstypekodeid | bigint    | Primærnøkkel |
| omsetningstype       | string    |
| oppdateringsdato     | timestamp |
| from_datetime        | timestamp |
| to_datetime          | timestamp |

---

### dim_omsattregisterenhetsrett_encrypted

**Description:**

Tabellen inneholder informasjon om de omsatte Registerenhetsrettene tilknyttet en omsetning. Kan knyttes til dim_omsetning_encrypted/fact_omsetning_encrypted med zk_omsetningId og til dim_registerenhetsrett med zk_registerenhetsrettId.

Boligtype angir hva partene selv har oppgitt om eventuell bebyggelse vedørerende registerenhetsretten. Brukstype angir hva partene selv har oppgitt er registerenhetsrettens brukstype.

**Schema:**

| Column                           | Type      | Comment                                    |
| -------------------------------- | --------- | ------------------------------------------ |
| omsattRegisterenhetsrettId       | bigint    | Primærnøkkel                               |
| zk_omsetningId                   | bigint    | Fremmednøkkel til fact_omsetning_encrypted |
| zk_registerenhetsrettId          | bigint    | Fremmednøkkel til dim_registerenhetsrett   |
| zk_boligtypekodeid               | bigint    | Fremmednøkkel til dim_boligtypekode        |
| zk_brukstypekodeid               | bigint    | Fremmednøkkel til dim_brukstypekode        |
| omsattRegisterenhetsrettKategori | string    |
| keyId                            | bigint    |
| oppdateringsdato                 | timestamp |
| from_datetime                    | timestamp |
| to_datetime                      | timestamp |
| zx_ingest_timestamp              | timestamp |

---

### dim_omsattregisterenhetsrettsandel_encrypted

**Description:**

Tabellen inneholder informasjon om de omsatte Registerenhetsrettsandelene tilknyttet en omsetning. Omsatte registerenhetsrettsandeler kan knyttes til omsetning via dim_omsattregisterenhetsrett_encrypted.

zk_omsattregisterenhetsrettId angir omsattregisterenhetsrett, og zk_omsetningId i dim_omsattregisterenhetsrett_encrypted angir den tilknyttede omsetningen.
zk_registerenhetsrettsandelId angir den aktuelle registerenhetsrettsandelen.

**Schema:**

| Column                                 | Type      | Comment                                                  |
| -------------------------------------- | --------- | -------------------------------------------------------- |
| omsattRegisterenhetsrettsandelId       | bigint    | Primærnøkkel                                             |
| zk_omsatteregisterenhetsrettsId        | bigint    | Fremmednøkkel til dim_omsattregisterenhetsrett_encrypted |
| omsattRegisterenhetsrettsandelKategori | string    |
| keyId                                  | bigint    |
| oppdateringsdato                       | timestamp |
| from_datetime                          | timestamp |
| to_datetime                            | timestamp |
| zx_ingest_timestamp                    | timestamp |

---

### dim_overfoering_omfatter_encrypted

**Description:**

Tabellen inneholder hvilke registerenhetsretter eller registerenhetsrettsandel som en rettsstiftelse/heftelse er overført fra og overført til i forbindelse med en overføringen. Informasjon om overføringen ligger i fact_overfoering_encrypted, som kan knyttes til med zk_overfoeringId.

For hver oppføring vil ENTEN zk_fra_registerenhetsrettId og zk_til_registerenhetsrettId har verdier ELLER zk_fra_registerenhetsrettsandelId og zk_til_registerenhetsrettsandelId ha verdier. zk_fra_registerenhetsrettId angir registerenhetsretten en heftelse er overført fra, og zk_til_registerenhetsrettId angir registerenhetsretten den er overført til. zk_fra_registerenhetsrettsandelId angir registerenhetsrettsandelen en heftelse er overført fra, og zk_til_registerenhetsrettsandelId angir registerenhetsrettsandelen den er overført til.

**Schema:**

| Column                            | Type      | Comment                                                                                                               |
| --------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| overfoeringOmfatterId             | bigint    | Primærnøkkel                                                                                                          |
| zk_overfoeringId                  | bigint    | Fremmednøkkel til fact_overfoering_encrypted                                                                          |
| zk_fra_registerenhetsrettId       | bigint    | Fremmednøkkel til dim_registerenhetsrett for registerenhetsretten som rettsstiftelsen er overført fra                 |
| zk_til_registerenhetsrettId       | bigint    | Fremmednøkkel til dim_registerenhetsrett for registerenhetsretten som rettsstiftelsen er overført til                 |
| zk_fra_registerenhetsrettsandelId | bigint    | Fremmednøkkel til dim_registerenhetsrettsandel_encrypted for registerenhetsretten som rettsstiftelsen er overført fra |
| zk_til_registerenhetsrettsandelId | bigint    | Fremmednøkkel til dim_registerenhetsrettsandel_encrypted for registerenhetsretten som rettsstiftelsen er overført til |
| keyId                             | bigint    |
| oppdateringsdato                  | timestamp |
| from_datetime                     | timestamp |
| to_datetime                       | timestamp |
| zx_ingest_timestamp               | timestamp |

---

### dim_periodekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over periodetyper. Dette er enten måned, år eller blank.

**Schema:**

| Column           | Type      | Comment      |
| ---------------- | --------- | ------------ |
| periodekodeid    | bigint    | Primærnøkkel |
| periode          | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_registerenhet

**Description:**

En registerenhet er enheten man registrerer en rettsstiftelse på. For en fast eiendom er registerenheten en matrikkelenhet, for borett er det en borettslagsandel. Dette angis i kolonnen _registerenhetKategori_.

Registerenheter som har registerenhetKategori lik _Matrikkelenhet_, _Festegrunn_ eller _Seksjon_ kan knyttes til matrikkelenheter i matrikkelen ved hjelp av kommunenummer, gaardsnummer, bruksnummer, festenummer og/eller seksjonsnummer. Verdi lik 0 i disse feltene tilsvarer en nullverdi. Kommunenummer er lagret i dim_kommune og kan knyttes til med fremmednøkkel zk_kommuneId i fact_registerenhet.

Registerenheter med registerenhetKategori lik _Borettslagsandel_ har fremmednøkkel zk_borettslagId til dim_borettslag og har et andelsnummer.

Registerenhet er delt i dim_registerenhet og fact_registerenhet. Gårdsnummer, bruksnummer osv. finnes i dim_registerenhet. Fremmednøkler finnes i fact_registerenhet. Begge har primærnøkkel registerenhetId.

**Schema:**

| Column                        | Type      | Comment                                                            |
| ----------------------------- | --------- | ------------------------------------------------------------------ |
| registerenhetId               | bigint    | Primærnøkkel                                                       |
| registerenhetKategori         | string    | "Matrikkelenhet", "Festegrunn", "Seksjon" eller "Borettslagsandel" |
| utgaatt                       | boolean   |
| gaardsnummer                  | int       | Likt gårdsnummer i matrikkelen                                     |
| bruksnummer                   | int       | Likt bruksnummer i matrikkelen                                     |
| festenummer                   | int       | Likt festenummer i matrikkelen                                     |
| seksjonsnummer                | int       | Likt seksjonsnummer i matrikkelen                                  |
| andelsnummer                  | int       | Andelsnummer for en borettslagsandel                               |
| tinglyst                      | boolean   |
| beregneterseksjonert          | boolean   |
| beregnetharaktivefestegrunner | boolean   |
| jordsameie                    | boolean   |
| oppdateringsdato              | timestamp |
| from_datetime                 | timestamp |
| to_datetime                   | timestamp |
| zx_ingest_timestamp           | timestamp |

---

### dim_registerenhetsrett

**Description:**

En registerenhetsrett er en form for eierskap eller eierrettighet over en registerenhet. Dette kan være eiendomsrett (den som har det kalles grunneier til en matrikkelenhet, andelseier til en borettslagsandel), festerett (fester) og framfesterett til en matrikkelenhet, og borett iht brl. § 2-13 til en borettslagsandel.

I grunnboken vil man kun referere til tinglyst registerenhetsrett. Dermed skal det alltid finnes en rettsstiftelse som etablerer registerenhetsretten. En Registerenhetsrett kan sees på som en representant for en slik rettsstiftelse. I dette tilfellet er eier angitt ved zk_realkobletTil_registerenhetId som fremmednøkkel til dim_registerenhet / fact_registerenhet.

En registerenhetsrett kan knyttes til tilhørende registerenhet i dim_registerenhet / fact_registerenhet med zk_registernhetId.

**Schema:**

| Column                      | Type      | Comment                                      |
| --------------------------- | --------- | -------------------------------------------- |
| registerenhetsrettId        | bigint    | Primærnøkkel                                 |
| zk_registerenhetId          | bigint    | Fremmednøkkel til fact_registerenhet         |
| zk_registerenhetsrettKodeId | bigint    | Fremmednøkkel til dim_registerenhetsrettkode |
| oppdateringsdato            | timestamp |
| from_datetime               | timestamp |
| to_datetime                 | timestamp |
| zx_ingest_timestamp         | timestamp |

---

### dim_registerenhetsrettsandel_encrypted

**Description:**

En Registerenhetsrettsandel representerer andelen en person har i en Registerenhetsrett. Andelen er ikke lokalisert til en bestemt del av en registerenhet, men angir kun en brøk. Denne andelen kan være resultatet av en eller flere overdragelser, og representerer alltid summen av disse. Hvis andelen er historisk, angir den en tidligere slik summert andel.

Realsameier og jordsameier eies av registerenheter istedenfor personer (de eies indirekte av de personene som til enhver tid eier disse registerenhetene igjen).

Registerenhetsrettsandel er delt i dim_registerenhetsrettsandel og fact_registerenhetsrettsandel. Begge har primærnøkkel registerenhetsrettsandelId. Eierandelen er angitt med brøk og teller i fact_registerenhetsrettsandel.

**Schema:**

| Column                     | Type      | Comment      |
| -------------------------- | --------- | ------------ |
| registerenhetsrettsandelId | bigint    | Primærnøkkel |
| lopenummer                 | int       |
| historisk                  | boolean   |
| keyId                      | bigint    |
| oppdateringsdato           | timestamp |
| from_datetime              | timestamp |
| to_datetime                | timestamp |
| zx_ingest_timestamp        | timestamp |

---

### dim_registerenhetsrettstypekode

Denne kodelistetabellen inneholder koder og beskrivelser over ulike typer registerenhetsretter. Det kan være enten eiendomsrett, festerett, framfesterett 1-3 eller borett iht. avtale inngått etter bestemmelsen i borettslagsloven § 2-13 (B).

**Description:**

**Schema:**

| Column                        | Type      | Comment      |
| ----------------------------- | --------- | ------------ |
| registerenhetsrettstypekodeId | bigint    | Primærnøkkel |
| registerenhetsrettstype       | string    |
| oppdateringsdato              | timestamp |
| from_datetime                 | timestamp |
| to_datetime                   | timestamp |

---

### dim_registerenhettypekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over registerenhettyper, som kan være matrikkelenhet, festegrunn, seksjon eller borettslagsandel.

**Schema:**

| Column                  | Type      | Comment      |
| ----------------------- | --------- | ------------ |
| registerenhettypekodeId | bigint    | Primærnøkkel |
| registerenhettype       | string    |
| oppdateringsdato        | timestamp |
| from_datetime           | timestamp |
| to_datetime             | timestamp |

---

### dim_rettsstiftelse

**Description:**

Denne tabellen inneholder rettsstiftelser. En Rettsstiftelse er en bestemmelse i et dokument som stifter, forandrer, overdrar, behefter, anerkjenner eller opphever en rettighet i en registerenhet.

Det vil si tinglyst overdragelse av registerenhetsrett, heftelser, registerenhetsendringer, rettsendringer, anmerkninger og personkoblingsendringer.

Overdragelse av registerenhetsrett = Hjemmelsopplysninger

Heftelser = Heftelse (tidligere Pengeheftelser og Servitutter i fast eiendom og Heftelser i borett)

Registerenhetsendringer = Grunndata (fast eiendom), Opplysninger fra borettslaget (borett)

Rettsendringer = Påtegninger på andre rettsstiftelser

Anmerkninger = Påtegninger på person eller andel av matrikkelenhet/borettslagsandel

Personkoblingsendringer = Endring av id på person (vises ikke på grunnboksutskrift)

Et dokument kan ha flere rettsstiftelser. Dokumentet kan finnes ved zk_dokumentId i fact_rettsstiftelse. Dersom rettsstiftelsen innebærer en omsetning kan omsetningen i dim_omsetning_encrypted finnes ved zk_omsetningId i fact_rettsstiftelse.

Rettsstiftelser er delt i dim_rettsstiftelse og fact_rettsstiftelse. Begge har primærnøkkel rettsstiftelseId.

**Schema:**

| Column                 | Type      | Comment      |
| ---------------------- | --------- | ------------ |
| rettsstiftelseId       | bigint    | Primærnøkkel |
| rettsstiftelseKategori | string    |
| rettsstiftelsesnummer  | int       |
| hargebyr               | boolean   |
| saksnummer             | string    |
| tingrett               | string    |
| verdiendring           | boolean   |
| prioritet              | string    |
| navn                   | string    |
| foreloepig             | boolean   |
| identifikator_nve      | string    |
| historisk              | boolean   |
| oppdateringsdato       | timestamp |
| from_datetime          | timestamp |
| to_datetime            | timestamp |
| zx_ingest_timestamp    | timestamp |

---

### dim_rettsstiftelse_til_dokument

**Description:**

Denne tabeller angir dokumenter som ankes for rettsstiftelser av kategorien "Anke". zk_rettsstiftelseId angir rettsstiftelsen og zk_dokumentId angir dokumentet som ankes.

**Schema:**

| Column                      | Type      | Comment                               |
| --------------------------- | --------- | ------------------------------------- |
| rettsstiftelseTilDokumentId | bigint    | Primærnøkkel                          |
| zk_rettsstiftelseId         | bigint    | Fremmednøkkel til fact_rettsstiftelse |
| zk_dokumentId               | bigint    | Fremmednøkkel til fact_dokument       |
| oppdateringsdato            | timestamp |
| from_datetime               | timestamp |
| to_datetime                 | timestamp |
| zx_ingest_timestamp         | timestamp |

---

### dim_rettsstiftelse_til_person_encrypted

**Description:**

Denne tabellen knytter rettsstiftelser, herunder heftelser, til personer.

rettsstiftelseTilPersonKategori angir rollen den aktuelle personen har med hensyn til rettsstiftelsen, for eksempel "SAKSOEKER" eller "RETTIGHETSHAVER_AKTIV". Hver kategori angir en kobling i domenemodellen. Kategorier som med suffix "\_historisk" angir historiske rader.

zk_rettsstiftelseId angir den aktuelle rettsstiftelsen. zk_personId angir personen, som enten kan være en juridisk person i dim_juridisk_person eller en fysisk person i dim_fysisk_person_encrypted.

**Schema:**

| Column                          | Type      | Comment                                                             |
| ------------------------------- | --------- | ------------------------------------------------------------------- |
| rettsstiftelseTilPersonId       | bigint    | Primærnøkkel                                                        |
| rettsstiftelseTilPersonKategori | string    |
| zk_rettsstiftelseId             | bigint    | Fremmednøkkel til fact_rettsstiftelse                               |
| zk_personId                     | bigint    | Fremmednøkkel til dim_juridisk_person / dim_fysisk_person_encrypted |
| keyId                           | bigint    |
| oppdateringsdato                | timestamp |
| from_datetime                   | timestamp |
| to_datetime                     | timestamp |
| zx_ingest_timestamp             | timestamp |

---

### dim_rettsstiftelse_til_registerenhetsrett_encrypted

**Description:**

Denne tabellen inneholder relasjoner mellom rettsstiftelser og registerenhetsretter, og typer koblinger:

HEFTER_I / HEFTER_I_HISTORISK:
Rader med kategori "HEFTER_I" eller "HEFTER_I_HISTORISK" angir rettsstiftelser som hefter i en registerenhetsrett, det vil si at heftelsen gjelder alle andeler i registerenhetsretten. Dersom en rettsstiftelse hefter i én eller flere, men ikke alle, registerenhetsrettsandeler, er koblingen i stedet modellert i tabellen fact_hefte_i_registerenhetsrettsandel_encrypted.
Kategorien HEFTER_I_HISTORISK benyttes for historiske relasjoner.

REALKOBLET_TIL:
Rader med kategori REALKOBLET_TIL angir registerenhetsretter som er rettighetshaver(e) til en heftelse (rettsstiftelse).

zk_rettsstiftelseId angir den aktuelle rettsstiftelsen. zk_registerenhetsrettId angir registerenhetsretten. rettsstiftelseTilRegisterenhetsrettKategori angir typen relasjon mellom rettsstiftelsen og registerenhetsretten. Gyldige verdier er "HEFTER_I", "HEFTER_I_HISTORISK" eller "REALKOBLET_TIL".

**Schema:**

| Column                                      | Type      | Comment                                  |
| ------------------------------------------- | --------- | ---------------------------------------- |
| rettsstiftelseTilRegisterenhetsrettId       | bigint    | Primærnøkkel                             |
| rettsstiftelseTilRegisterenhetsrettKategori | string    |
| zk_rettsstiftelseId                         | bigint    | Fremmednøkkel til fact_rettsstiftelse    |
| zk_registerenhetsrettId                     | bigint    | Fremmednøkkel til dim_registerenhetsrett |
| keyId                                       | bigint    |
| oppdateringsdato                            | timestamp |
| from_datetime                               | timestamp |
| to_datetime                                 | timestamp |
| zx_ingest_timestamp                         | timestamp |

---

### dim_rettsstiftelse_til_rettsstiftelse

**Description:**

Denne tabellen inneholder informasjon om rettsstiftelser som hefter i andre rettsstiftelser. Det gjelder rettsstiftelser av kategori "PrioritetsbestemmelseForDokumentnummer", "FremleieAvtale" og "Ombytte".

zk_kilde_rettsstiftelseId angir den heftende rettsstiftelsen og zk_maal_rettsstiftelse angir rettsstiftelsen den hefter i.

**Schema:**

| Column                                  | Type      | Comment                               |
| --------------------------------------- | --------- | ------------------------------------- |
| rettsstiftelseTilRettsstiftelseId       | bigint    | Primærnøkkel                          |
| rettsstiftelseTilRettsstiftelseKategori | string    |
| zk_kilde_rettsstiftelseId               | bigint    | Fremmednøkkel til fact_rettsstiftelse |
| zk_maal_rettsstiftelseId                | bigint    | Fremmednøkkel til fact_rettsstiftelse |
| keyId                                   | bigint    |
| oppdateringsdato                        | timestamp |
| from_datetime                           | timestamp |
| to_datetime                             | timestamp |
| zx_ingest_timestamp                     | timestamp |

---

### dim_saksinformasjon

**Description:**

Denne tabellen inneholder saksinformasjon, det vil si metadata om en _sak_. En sak oppretter et dokument, og flere dokumenter kan referere til samme sak.

Saksinformasjon og tilhørende dokumenter kan knyttes med fremmednøkkel zk_saksinformasjon i fact_dokument.

Saksinformasjon er knyttet til en til tre _sakspersoner_. Sakspersoner er lagret i dim_saksperson_encrypted, som inneholder fremmednøkkel zk_saksinformasjonId.

**Schema:**

| Column                                    | Type      | Comment                                                     |
| ----------------------------------------- | --------- | ----------------------------------------------------------- |
| saksinformasjonId                         | bigint    | Primærnøkkel                                                |
| saksnummer                                | int       |
| zk_saksinformasjonSaksstatusKodeId        | bigint    | Fremmednøkkel til dim_saksinformasjon_saksstatusKode        |
| zk_saksinformasjonBehandlingstufallkodeId | bigint    | Fremmednøkkel til dim_saksinformasjon_behandlingsutfallKode |
| mottaksdato                               | date      |                                                             |
| foelgebrevsdato                           | date      |                                                             |
| oppdateringsdato                          | timestamp |
| from_datetime                             | timestamp |
| to_datetime                               | timestamp |
| zx_ingest_timestamp                       | timestamp |

---

### dim_saksinformasjon_behandlingsutfallkode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over behandlingsutfall for en sak. Utfallet kan enten være nektet, avvist, tinglyst eller uavklart.

**Schema:**

| Column                                 | Type      | Comment                                 |
| -------------------------------------- | --------- | --------------------------------------- |
| saksinformasjonBehandlingsutfallKodeId | bigint    | Primærnøkkel                            |
| saksinformasjonBehandlingsutfall       | string    | Beskrivende tekst for behandlingsutfall |
| oppdateringsdato                       | timestamp |
| from_datetime                          | timestamp |
| to_datetime                            | timestamp |

---

### dim_saksinformasjon_saksstatuskode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over saksstatusen til en sak, altså hvor i behandlingsprosessen saken befinner seg. Saksstatus kan være utkast, klar_for_mottak, under_behandling, klar_for_avvisning eller avsluttet.

**Schema:**

| Column                          | Type      | Comment                          |
| ------------------------------- | --------- | -------------------------------- |
| saksinformasjonSaksstatusKodeId | bigint    | Primærnøkkel                     |
| saksinformasjonSaksstatus       | string    | Beskrivende tekst for saksstatus |
| oppdateringsdato                | timestamp |
| from_datetime                   | timestamp |
| to_datetime                     | timestamp |

---

### dim_saksperson_encrypted

**Description:**

Denne tabellen inneholder informasjon om sakspersoner. Personene kan både være norske eller utenlandske borgere eller organisasjoner.

Tabellen inneholder informasjon om personen slik den var da saken ble registrert og blir ikke oppdatert siden. Det betyr at for eksempel hvis en person har endret identifikasjonsnummer (f.eks. gått fra D-nummer til fødselsnummer) kan vedkommende ikke knyttes på tvers av dim_saksperson_encrypted og dim_fysisk_person_encrypted, siden kun sistnevnte vil bli oppdatert.

En oppføring i saksinformasjon har en til tre tilhørende sakspersoner. En sak kan ha opptil én saksperson av hver sakspersonrolle: "innsender", "mottaker" og "fakturamottaker".

**Schema:**

| Column                             | Type      | Comment                                             |
| ---------------------------------- | --------- | --------------------------------------------------- |
| sakspersonId                       | bigint    | Primærnøkkel                                        |
| zk_saksinformasjonId               | bigint    | Fremmednøkkel til dim_saksinformasjon               |
| zk_identifikasjonsnummerTypeKodeId | bigint    | Fremmednøkkel til dim_identifikasjonsnummertypekode |
| identifikasjonsnummer              | string    |
| sakspersonrolle                    | string    | "innsender", "mottaker" eller "fakturamottaker"     |
| adresselinje1                      | string    |
| adresselinje2                      | string    |
| adresselinje3                      | string    |
| epostadresse                       | string    |
| referanse                          | string    |
| postnummer                         | string    |
| poststed                           | string    |
| land                               | string    |
| keyId                              | bigint    |
| oppdateringsdato                   | timestamp |
| from_datetime                      | timestamp |
| to_datetime                        | timestamp |
| zx_ingest_timestamp                | timestamp |

---

### dim_valutakodekode

**Description:**

Denne kodelistetabellen inneholder koder og beskrivelser over valutakoder.

**Schema:**

| Column           | Type      | Comment      |
| ---------------- | --------- | ------------ |
| valutakodekodeid | bigint    | Primærnøkkel |
| valutakode       | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

## FACT TABLES

---

### fact_dokument

**Description:**

Denne tabellen inneholder data om dokumenter. Data om dokumenter er delt i en dimensjontabell (dim_dokument) og en faktatabell (fact_dokument).

Det er dokumenter som tinglyses, og et dokument kan inneholde flere bestemmelser som skal tinglyses. Hver slik bestemmelse registreres inn som en rettsstiftelse tilhørende dokumentet. En rettsstiftelse har altså hverken selvstendig dato eller tinglyststatus, det er dokumentets dato og status som gjelder.

zk_dokumentId i fact_rettsstiftelse angir rettsstiftelsens dokument. registreringstidspunkt i fact_dokument angir dokumentets dato. zk_dokumentstatusKodeId i fact_dokument knyttes til dim_dokumentstatuskode for å angi dokumentets status (f.eks. "tinglyst").

**Schema:**

| Column                      | Type      | Comment                                                                                  |
| --------------------------- | --------- | ---------------------------------------------------------------------------------------- |
| dokumentId                  | bigint    | Primærnøkkel                                                                             |
| zk_saksinformasjonId        | bigint    | Fremmenøkkel til dim_saksinformasjon                                                     |
| zk_omdokulertTil_dokumentId | bigint    | Fremmednøkkel til dim_dokument / fact_dokument for et dokument som har blitt omdokulert. |
| zk_embetekodeId             | bigint    | Fremmednøkkel til dim_embetekode                                                         |
| zk_dokumentstatusKodeId     | bigint    | Fremmednøkkel til dim_dokumentstatuskode                                                 |
| zk_valutakodeKodeId         | bigint    | Fremmednøkkel til dim_valutakodekode som angir valutakode for gebyrbeløpet               |
| gebyrbeloepsverdi           | int       |
| gebyrbeloepstekst           | string    |
| registreringstidspunkt      | timestamp | Tidspunktet dokumentet ble registrert                                                    |
| oppdateringsdato            | timestamp |
| zx_ingest_timestamp         | timestamp |

---

### fact_hefte_i_registerenhetsrettsandel_encrypted

**Description:**

Denne tabellen knytter rettsstiftelser til registerenhetsrettsandel for rettsstiftelser (heftelser) som hefter i en eller flere registerenhetsrettsandel, men ikke alle andelene i en registerenhetsrett. For rettsstiftelser som hefter i en registerenhetsrett, dvs. alle andelene i en registerenhetsrett, finnes koblingen i dim_rettsstiftelse_til_registerenhetsrett_encrypted.

zk_rettsstiftelseId angir den aktuelle rettsstiftelsen. zk_registerenhetsrettsandelId angir registerenhetsrettsandelen som rettsstiftelsen hefter i.

Teller og nevner angir ikke en brøkdel av brøken i registerenhetsrettsandelen, men en brøk av hele Registerenhetsretten. Brøken er normalt lik, men kan være mindre enn brøken i registerenhetsrettsandelen.

**Schema:**

| Column                        | Type      | Comment                                                  |
| ----------------------------- | --------- | -------------------------------------------------------- |
| dokumentId                    | bigint    | Primærnøkkel                                             |
| zk_rettsstiftelseId           | bigint    | Fremmenøkkel til dim_rettsstiftelse                      |
| zk_registerenhetsrettsandelId | bigint    | Fremmednøkkel til dim_registerenhetsrettsandel_encrypted |
| teller                        | int       |
| nevner                        | int       |
| historisk                     | boolean   |
| keyId                         | bigint    |
| oppdateringsdato              | timestamp |
| zx_ingest_timestamp           | timestamp |

---

### fact_omsetning_beloep_encrypted

**Description:**

Denne tabellen inneholder pengebeløp knyttet til en omsetning. Beløp er oppgitt i et helt tall uten desimaler. Den tilhørende omsetningen kan finnes i dim_omsetning_encrypted med fremmednøkkelen zk_omsetningId.

**Schema:**

| Column                  | Type      | Comment                                   |
| ----------------------- | --------- | ----------------------------------------- |
| omsetningBeloepId       | bigint    | Primærnøkkel                              |
| zk_omsetningId          | bigint    | Fremmednøkkel til dim_omsetning_encrypted |
| zk_valutakodeKodeId     | bigint    | Fremmednøkkel til dim_valutakodekode      |
| omsetningBeloepKategori | string    |
| beloepsverdi            | int       |
| beloepstekst            | string    |
| keyId                   | bigint    |
| oppdateringsdato        | timestamp |
| zx_ingest_timestamp     | timestamp |

---

### fact_omsetning_encrypted

**Description:**

Denne tabellen inneholder omsetninger. En omsetning er kjøp og salg (eller annen type overdragelse, eks skifteoppgjør) av registerenhetsretter eller registerenhetsrettsandeler. I de fleste tilfeller skjer omsetningen ved at noen kjøper eller på annen måte erverver registerenhetsrettsandeler av de som er rettighetshavere til registerenhetsretten. Men omsetningen kan også skje på andre måter.

Ved Arealoverføring mellom matrikkelenheter skjer det en omsetning, og det kan bli beregnet dokumentavgift. Det blir imidlertid ikke omsatt Registerenhetsrettsandeler, da hjemmelsforholdene ikke endres. Det som endres er det arealet man har registerenhetsrett til.

Det samme gjelder ved endring av sameiebrøk mellom seksjoner i et seksjonssameie. Verdier flyttes da mellom seksjonene.

Informasjon om registerenhetsrettene som er omsatt under en omsetning finnes i dim_omsattregisterenhetsrett_encrypted, som kan knyttes til omsetning med sin fremmednøkkel zk_omsetningId.

Informasjon om registerenhetsrettsandelene som er omsatt under en omsetning finnes i dim_omsattregisterenhetsrettsandel_encrypted. Omsattregisterenhetsrettsandel kan knyttes til omsetning via dim_omsattregisterenhetsrett_encrypted med fremmednøkkelen zk_omsattregisterenhetsrettId.

Beløp knyttet til en omsetning ligger i fact_omsetning_beloep_encrypted, som knyttes til dim_omsetning/fact_omsetning ved zk_omsetningId. Hvilke registerenhetsretter som er omsatt kan finnes i dim_omsattregisterenhetsrett_encrypted.

**Schema:**

| Column                         | Type      | Comment                                         |
| ------------------------------ | --------- | ----------------------------------------------- |
| omsetningId                    | bigint    | Primærnøkkel                                    |
| zk_omsetningstypeKodeId        | bigint    | Fremmednøkkel til dim_omsetningstypekode        |
| zk_dokumentavgiftsaarsakkodeid | bigint    | Fremmednøkkel til dim_dokumentavgiftsaarsakkode |
| keyId                          | bigint    |
| oppdateringsdato               | timestamp |
| zx_ingest_timestamp            | timestamp |

---

### fact_overfoering_encrypted

**Description:**

Tabellen inneholder overføringer av rettsstiftelser. Når heftelser overføres i forbindelse med fradeling, seksjonering med flere, logges hvilke heftelser som blir overført, hvilken rettsstiftelse som er årsak til overføringen, hvilke Registerenhetsretter heftelsene overføres fra og hvilke Registerenhetsretter (eller Registerenhetsrettsandeler) heftelsene overføres til.

zk_overfoert_rettstiftelseId angir rettstiftelseId til den overførte rettsstiftelsen (heftelsen). zk_overfoerende_rettstiftelseId angir rettstiftelseId til den rettsstiftelsen som er årsak til overføringen.

Registerenhetsrettene og/eller registerenhetsrettsandelene som rettsstiftelsene/heftelsene er overført fra og overført til er lagret i dim_overfoering_omfatter_encrypted, som kan knyttes til fact_overfoering_encrypted på zk_overfoeringId.

**Schema:**

| Column                          | Type      | Comment                                                                           |
| ------------------------------- | --------- | --------------------------------------------------------------------------------- |
| overfoeringId                   | bigint    | Primærnøkkel                                                                      |
| zk_overfoert_rettstiftelseId    | bigint    | Fremmednøkkel til dim_rettsstiftelse for rettsstiftelsen som er overført          |
| zk_overfoerende_rettstiftelseId | bigint    | Fremmednøkkel til dim_rettsstiftelse for rettsstiftelsen som utløser overføringen |
| oppdateringsdato                | timestamp |
| zx_ingest_timestamp             | timestamp |

---

### fact_registerenhet

**Description:**

En registerenhet er enheten man registrerer en rettsstiftelse på. For en fast eiendom er registerenheten en matrikkelenhet, for borett er det en borettslagsandel. Dette angis i kolonnen _registerenhetKategori_.

Registerenheter som har registerenhetKategori lik _Matrikkelenhet_, _Festegrunn_ eller _Seksjon_ kan knyttes til matrikkelenheter i matrikkelen ved hjelp av kommunenummer, gaardsnummer, bruksnummer, festenummer og/eller seksjonsnummer. Verdi lik 0 i disse feltene tilsvarer en nullverdi. Kommunenummer er lagret i dim_kommune og kan knyttes til med fremmednøkkel zk_kommuneId i fact_registerenhet.

Registerenheter med registerenhetKategori lik _Borettslagsandel_ har fremmednøkkel zk_borettslagId til dim_borettslag og har et andelsnummer.

Registerenhet er delt i dim_registerenhet og fact_registerenhet. Gårdsnummer, bruksnummer osv. finnes i dim_registerenhet. Fremmednøkler finnes i fact_registerenhet. Begge har primærnøkkel registerenhetId.

**Schema:**

| Column                            | Type      | Comment                                                                          |
| --------------------------------- | --------- | -------------------------------------------------------------------------------- |
| registerenhetId                   | bigint    | Primærnøkkel                                                                     |
| zk_kommuneId                      | bigint    | Fremmednøkkel til dim_kommune                                                    |
| zk_borettslagId                   | bigint    | Fremmednøkkel til dim_borettslag                                                 |
| zk_adresseId                      | bigint    | Fremmednøkkel til dim_adresse_encrypted                                          |
| zk_omnummererttil_registerenhetId | bigint    | Fremmednøkkel til dim_registerenhet for registerenheter som er blitt omnummerert |
| oppdateringsdato                  | timestamp |
| zx_ingest_timestamp               | timestamp |

---

### fact_registerenhetsrettsandel_encrypted

**Description:**

En Registerenhetsrettsandel representerer andelen en person har i en Registerenhetsrett. Andelen er ikke lokalisert til en bestemt del av en registerenhet, men angir kun en brøk. Denne andelen kan være resultatet av en eller flere overdragelser, og representerer alltid summen av disse. Hvis andelen er historisk, angir den en tidligere slik summert andel.

Realsameier og jordsameier eies av registerenheter istedenfor personer (de eies indirekte av de personene som til enhver tid eier disse registerenhetene igjen). I dette tilfellet er eier angitt ved zk_realkobletTil_registerenhetId som fremmednøkkel til dim_registerenhet / fact_registerenhet.

Registerenhetsrettsandel er delt i dim_registerenhetsrettsandel og fact_registerenhetsrettsandel. Begge har primærnøkkel registerenhetsrettsandelId. Eierandelen er angitt med brøk og teller i fact_registerenhetsrettsandel.

**Schema:**

| Column                           | Type      | Comment                                                                                          |
| -------------------------------- | --------- | ------------------------------------------------------------------------------------------------ |
| registerenhetsrettsandelId       | bigint    | Primærnøkkel                                                                                     |
| zk_registerenhetsrettId          | bigint    | Fremmednøkkel til dim_registerenhetsrett                                                         |
| zk_rettighetshaver_personId      | bigint    | Fremmednøkkel til dim_juridisk_person og dim_fysisk_person_encrypted som angir rettighetshaveren |
| zk_realkobletTil_registerenhetId | bigint    | Fremmednøkkel til dim_registerenhet når en registerenhet er rettighetshaver                      |
| teller                           | int       |
| nevner                           | int       |
| keyId                            | bigint    |
| oppdateringsdato                 | timestamp |
| zx_ingest_timestamp              | timestamp |

---

### fact_rettsstiftelse

**Description:**

Denne tabellen inneholder rettsstiftelser. En Rettsstiftelse er en bestemmelse i et dokument som stifter, forandrer, overdrar, behefter, anerkjenner eller opphever en rettighet i en registerenhet.

Det vil si tinglyst overdragelse av registerenhetsrett, heftelser, registerenhetsendringer, rettsendringer, anmerkninger og personkoblingsendringer.

Overdragelse av registerenhetsrett = Hjemmelsopplysninger

Heftelser = Heftelse (tidligere Pengeheftelser og Servitutter i fast eiendom og Heftelser i borett)

Registerenhetsendringer = Grunndata (fast eiendom), Opplysninger fra borettslaget (borett)

Rettsendringer = Påtegninger på andre rettsstiftelser

Anmerkninger = Påtegninger på person eller andel av matrikkelenhet/borettslagsandel

Personkoblingsendringer = Endring av id på person (vises ikke på grunnboksutskrift)

Et dokument kan ha flere rettsstiftelser. Dokumentet kan finnes ved zk_dokumentId i fact_rettsstiftelse. Dersom rettsstiftelsen innebærer en omsetning kan omsetningen i dim_omsetning_encrypted finnes ved zk_omsetningId i fact_rettsstiftelse.

Rettsstiftelser er delt i dim_rettsstiftelse og fact_rettsstiftelse. Begge har primærnøkkel rettsstiftelseId.

**Schema:**

| Column                       | Type      | Comment                                                                                  |
| ---------------------------- | --------- | ---------------------------------------------------------------------------------------- |
| rettsstiftelseId             | bigint    | Primærnøkkel                                                                             |
| zk_dokumentId                | bigint    | Fremmednøkkel til dim_dokument                                                           |
| zk_omsetningId               | bigint    | Fremmednøkkel til dim_omsetning_encrypted for rettsstiftelser som innebærer en omsetning |
| zk_rettsstiftelsestypeKodeId | bigint    | Fremmednøkkel til dim_rettsstiftelsestypekode                                            |
| zk_periodekodeId             | bigint    | Fremmednøkkel til dim_periodekode                                                        |
| zk_aarsaksparagrafkodeId     | bigint    | Fremmednøkkel til dim_aarsaksparagrafkode                                                |
| zk_aarsaksgebyrfritakkodeId  | bigint    | Fremmednøkkel til dim_aarsaksgebyrfritakkode                                             |
| zk_anketypekodeId            | bigint    | Fremmednøkkel til dim_anketypekode                                                       |
| leietid                      | int       |
| festetid_antall_aar          | int       |
| leiefradato                  | timestamp |
| oversendtlagmannsretten      | timestamp |
| nektet                       | timestamp |
| festefradato                 | timestamp |
| notifikasjonsdato            | timestamp |
| dato_for_avgj_anken_gjelder  | timestamp |
| paaberopt_prioritet_fra      | timestamp |
| fristforendeligregistrering  | timestamp |
| avholdt_dato                 | date      |
| avholdt_klokkeslett          | string    |
| oppdateringsdato             | timestamp |
| zx_ingest_timestamp          | timestamp |

---

### fact_rettsstiftelse_beloep

**Description:**

Denne tabellen inneholder pengebeløp knyttet til en rettsstiftelse/heftelse. Det gjelder rettsstiftelser av kategoriene "HeftelseIRettighet", "Nedkvittering", "NotertPant", "NotertTvangspant", "NyeVilkaarIFestekontrakt", "Pant", "PrioritetsbestemmelserForDokumentnummer", "PrioritetsbestemmelserForIkkeTinglystDokument", "Tvangsforretning", "TvangsforretningIRettighet" og "VilkaarIFestekontrakt". For "EierskifteMatrikkelenhet" og lignende se Omsetning.

Pengebeløpet er oppgitt som et heltall uten desimaler.

**Schema:**

| Column                       | Type      | Comment                              |
| ---------------------------- | --------- | ------------------------------------ |
| rettsstiftelseBeloepId       | bigint    | Primærnøkkel                         |
| zk_rettsstiftelseId          | bigint    | Fremmednøkkel til dim_rettsstiftelse |
| zk_valutakodeKodeId          | bigint    | Fremmednøkkel til dim_valutakodekode |
| rettsstiftelseBeloepKategori | string    |
| beloepsverdi                 | int       |
| beloepstekst                 | string    |
| oppdateringsdato             | timestamp |
| zx_ingest_timestamp          | timestamp |

---

### fact_rettsstiftelse_beloepforperiode

**Description:**

Denne tabellen inneholder pengebeløp knyttet til en rettsstiftelse/heftelse som gjelder for en periode. Det gjelder rettsstiftelser av kategoriene "Fremleieavtale", "Leieavtale" og "NyeVilkaarILeieavtale". zk_periodekodeid angir perioden beløpet gjelder for, for eksempel om det er et årlig eller månedlig beløp.

Pengebeløpet er oppgitt som et heltall uten desimaler.

**Schema:**

| Column                                 | Type      | Comment                              |
| -------------------------------------- | --------- | ------------------------------------ |
| rettsstiftelseBeloepId                 | bigint    | Primærnøkkel                         |
| zk_rettsstiftelseId                    | bigint    | Fremmednøkkel til dim_rettsstiftelse |
| zk_valutakodeKodeId                    | bigint    | Fremmednøkkel til dim_valutakodekode |
| zk_periodeKodeId                       | bigint    | Fremmednøkkel til dim_periodekode    |
| rettsstiftelseBeloepforperiodeKategori | string    |
| beloepsverdi                           | int       |
| beloepstekst                           | string    |
| oppdateringsdato                       | timestamp |
| zx_ingest_timestamp                    | timestamp |

---
