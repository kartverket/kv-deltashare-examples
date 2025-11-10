# External Table Documentation - Grunnbok

### Generelt

Dimensjonstabeller er implementert med Slowly Changing Dimensions type 2 (SCD2)-historikk. Det innebærer at hver rad har et gyldighetsintervall angitt ved _from_datetime_ og _to_datetime_. Tidligste mulige _from_datetime_ er 2017-04-13.

Kolonner med prefiks zk\_ angir fremmednøkler. For eksempel er _zk_kommuneId_ fremmednøkkel til tabell _dim_kommune_ og kan joines på primærnøkkel _kommuneId_. Kolonner med prefiks zx\_ angir interne systemkolonner.

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
- [dim_aarsaksgebyrfritakkoder](#dim_aarsaksgebyrfritakkoder)
- [dim_aarsaksparagrafkoder](#dim_aarsaksparagrafkoder)
- [dim_anketypekoder](#dim_anketypekoder)
- [dim_boligtypekoder](#dim_boligtypekoder)
- [dim_borettslag](#dim_borettslag)
- [dim_brukstypekoder](#dim_brukstypekoder)
- [dim_dokument](#dim_dokument)
- [dim_dokumentstatuskoder](#dim_dokumentstatuskoder)
- [dim_dokavgiftsaarsakkoder](#dim_dokavgiftsaarsakkoder)
- [dim_embetekode](#dim_embetekode)
- [dim_fysisk_person_encrypted](#dim_fysisk_person_encrypted)
- [dim_identifikasjonsnummertypekoder](#dim_identifikasjonsnummertypekoder)
- [dim_juridisk_person](#dim_juridisk_person)
- [dim_kommune](#dim_kommune)
- [dim_omsetning_encrypted](#dim_omsetning_encrypted)
- [dim_omsetningstypekoder](#dim_omsetningstypekoder)
- [dim_omsattregisterenhetsrett_encrypted](#dim_omsattregisterenhetsrett_encrypted)
- [dim_overfoering_omfatter_encrypted](#dim_overfoering_omfatter_encrypted)
- [dim_periodekode](#dim_periodekode)
- [dim_registerenhet](#dim_registerenhet)
- [dim_registerenhetsrett](#dim_registerenhetsrett)
- [dim_registerenhetsrettsandel_encrypted](#dim_registerenhetsrettsandel_encrypted)
- [dim_registerenhetsrettstypekoder](#dim_registerenhetsrettstypekoder)
- [dim_registerenhettypekoder](#dim_registerenhettypekoder)
- [dim_rettsstiftelse](#dim_rettsstiftelse)
- [dim_saksinformasjon_encrypted](#dim_saksinformasjon_encrypted)
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
- [fact_saksinformasjon_encrypted](#fact_saksinformasjon_encrypted)

---

## DIMENSION TABLES

---

### dim_adresse_encrypted

**Description:**

Tabellen inneholder alle adresser lagret i Grunnboken. Tabellen inkluderer kategoriene UtenlandskAdresse, Vegadresse, Matrikkeladresser og KonvertertAdresse. Vegadresser og Matrikkeladresser har kilde i matrikkelen og kan knyttes til dim_adresse fra matrikkelen med zk_matrikkel_adresseId, zk_matrikkel_bruksenhetId eller kommunenummer, gaardsnummer, bruksnummer, festenummer og/eller undernummer.

**Schema:**

| Column                    | Type      | Comment                                    |
| ------------------------- | --------- | ------------------------------------------ |
| adresseId                 | bigint    | Primærnøkkel                               |
| zk_matrikkel_adresseId    | bigint    | Fremmednøkkel til adresse i matrikkelen    |
| zk_matrikkel_bruksenhetId | bigint    | Fremmednøkkel til bruksenhet i matrikkelen |
| zk_landkodekodeid         | bigint    | Fremmednøkkel til dim_landkodekoder        |
| zk_kommuneid              | bigint    | Fremmednøkkel dim dim_kommune              |
| adresseKategori           | string    |
| bolignummer               | int       |
| adressekode               | string    |
| adressenavn               | string    |
| husnummer                 | int       |
| bokstav                   | string    |
| gaardsnummer              | int       |
| bruksnummer               | int       |
| festenummer               | int       |
| undernummer               | int       |
| adressetekst              | string    |
| keyId                     | bigint    |
| oppdateringsdato          | timestamp |
| from_datetime             | timestamp |
| to_datetime               | timestamp |
| zx_ingest_timestamp       | timestamp |

---

### dim_aarsaksgebyrfritakkoder

**Description:**

**Schema:**

| Column                   | Type      | Comment      |
| ------------------------ | --------- | ------------ |
| aarsaksgebyrfritakkodeid | bigint    | Primærnøkkel |
| aarsaksgebyrfritak       | string    |
| oppdateringsdato         | timestamp |
| from_datetime            | timestamp |
| to_datetime              | timestamp |

---

### dim_aarsaksparagrafkoder

**Description:**

**Schema:**

| Column                | Type      | Comment      |
| --------------------- | --------- | ------------ |
| aarsaksparagrafkodeid | bigint    | Primærnøkkel |
| aarsaksparagraf       | string    |
| oppdateringsdato      | timestamp |
| from_datetime         | timestamp |
| to_datetime           | timestamp |

---

### dim_anketypekoder

**Description:**

**Schema:**

| Column           | Type      | Comment |
| ---------------- | --------- | ------- |
| anketypekodeid   | bigint    |
| anketype         | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_boligtypekoder

**Description:**

**Schema:**

| Column           | Type      |
| ---------------- | --------- |
| boligtypekodeid  | bigint    |
| boligtype        | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_borettslag

**Description:**

Borettslag er ”eit samvirkeføretak som har til føremål å gi andelseigarane bruksrett til eigen bustad i føretakets eigedom (burett)”, jf. burettslagslova § 1-1 første ledd. zk_personId knytter til dim_juridisk_person (for organisasjonsnummer) eller dim_fysisk_person_encrypted (for løpenummer) og angir Borettslagets organisasjons- eller løpenummer.

**Schema:**

| Column              | Type      |
| ------------------- | --------- |
| borettslagId        | bigint    |
| zk_personId         | bigint    |
| historisk           | boolean   |
| oppdateringsdato    | timestamp |
| from_datetime       | timestamp |
| to_datetime         | timestamp |
| zx_ingest_timestamp | timestamp |

---

### dim_brukstypekoder

**Description:**

**Schema:**

| Column           | Type      |
| ---------------- | --------- |
| brukstypekodeid  | bigint    |
| brukstype        | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_dokument

**Description:**

Det er dokumenter som tinglyses. Et dokument kan inneholde flere bestemmelser som skal tinglyses. Hver slik bestemmelse registreres inn som en _rettsstiftelse_ tilhørende dokumentet. En rettsstiftelse har altså hverken selvstendig dato eller tinglyststatus, det er dokumentets dato og status som gjelder. zk_dokumentId i fact_rettsstiftelse angir rettsstiftelsens dokument. registreringstidspunkt i fact_dokument angir dokumentets dato. zk_dokumentstatusKodeId i fact_dokument knyttes til dim_dokumentstatuskoder for å angi dokumentets status (f.eks. "tinglyst"). Dokument er delt i dim_dokument og fact_dokument, begge med primary key dokumentId.

**Schema:**

| Column              | Type      |
| ------------------- | --------- |
| dokumentId          | bigint    |
| dokumentaar         | int       |
| dokumentnummer      | int       |
| datoregistrert      | boolean   |
| historisk           | boolean   |
| oppdateringsdato    | timestamp |
| from_datetime       | timestamp |
| to_datetime         | timestamp |
| zx_ingest_timestamp | timestamp |

---

### dim_dokumentstatuskoder

**Description:**

Status til et dokument. For eksempel "Tinglyst" eller "Nektet".

**Schema:**

| Column               | Type      |
| -------------------- | --------- |
| dokumentstatuskodeid | bigint    |
| dokumentstatus       | string    |
| oppdateringsdato     | timestamp |
| from_datetime        | timestamp |
| to_datetime          | timestamp |

---

### dim_dokavgiftsaarsakkoder

**Description:**

**Schema:**

| Column                 | Type      |
| ---------------------- | --------- |
| dokavgiftsaarsakkodeid | bigint    |
| dokavgiftsaarsak       | string    |
| oppdateringsdato       | timestamp |
| from_datetime          | timestamp |
| to_datetime            | timestamp |

---

### dim_embetekoder

**Description:**

**Schema:**

| Column           | Type      |
| ---------------- | --------- |
| embetekodeid     | bigint    |
| embete           | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_fysisk_person_encrypted

**Description:**

Tabellen inneholder alle fysiske personer som er registrert i grunnboksdatabasen. Tabellen inneholder både personer med fødselsnummer og med løpenummer (sistnevne kan være både fysiske og juridiske personer).

**Schema:**

| Column                             | Type      |
| ---------------------------------- | --------- |
| fysiskPersonId                     | bigint    |
| zk_identifikasjonsnummerTypeKodeId | bigint    |
| identifikasjonsnummer              | string    |
| navn                               | string    |
| historisk                          | boolean   |
| keyId                              | bigint    |
| oppdateringsdato                   | timestamp |
| from_datetime                      | timestamp |
| to_datetime                        | timestamp |
| zx_ingest_timestamp                | timestamp |

---

### dim_identifikasjonsnummertypekoder

**Description:**

Type for et identifikasjonsnummer. Enten fødselsnummer, organisasjonsnummer eller løpenummer.

**Schema:**

| Column                          | Type      |
| ------------------------------- | --------- |
| identifikasjonsnummertypekodeid | bigint    |
| identifikasjonsnummertype       | string    |
| oppdateringsdato                | timestamp |
| from_datetime                   | timestamp |
| to_datetime                     | timestamp |

---

### dim_juridisk_person

**Description:**

Tabellen inneholder juridiske personer som er registrert i grunnboksdatabasen. Tabellen inneholder bare juridiske personer med organisasjonsnummer. Juridiske personer med løpenummer er inneholdt i dim_fysisk_person_encrypted.

**Schema:**

| Column                             | Type      |
| ---------------------------------- | --------- |
| juridiskPersonId                   | bigint    |
| zk_identifikasjonsnummerTypeKodeId | bigint    |
| identifikasjonsnummer              | string    |
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

| Column              | Type      |
| ------------------- | --------- |
| kommuneId           | bigint    |
| kommunenummer       | string    |
| navn                | string    |
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

Beløp knyttet til en omsetning ligger i fact_omsetning_beloep_encrypted, som knyttes til dim_omsetning/fact_omsetning ved zk_omsetningId. Hvilke registerenhetsretter som er omsatt kan finnes i dim_omsattregisterenhetsrett_encrypted.

**Schema:**

| Column                        | Type      |
| ----------------------------- | --------- |
| omsetningId                   | bigint    |
| omsetningKategori             | string    |
| utlysttilsalgpaadetfriemarked | boolean   |
| hardokumentavgift             | boolean   |
| keyId                         | bigint    |
| oppdateringsdato              | timestamp |
| from_datetime                 | timestamp |
| to_datetime                   | timestamp |
| zx_ingest_timestamp           | timestamp |

---

### dim_omsetningstypekoder

**Description:**

Tabellen inneholder liste over omsetningstyper, altså nærmere om hva som er årsaken til at registerenhetsretten skifter hjemmelshaver.

**Schema:**

| Column               | Type      |
| -------------------- | --------- |
| omsetningstypekodeid | bigint    |
| omsetningstype       | string    |
| oppdateringsdato     | timestamp |
| from_datetime        | timestamp |
| to_datetime          | timestamp |

---

### dim_omsattregisterenhetsrett_encrypted

**Description:**

Tabellen inneholder informasjon om de omsatt Registerenhetsrettene tilknyttet en omsetning. Kan knyttes til dim_omsetning_encrypted/fact_omsetning_encrypted med zk_omsetningId og til dim_registerenhetsrett med zk_registerenhetsrettId.

Boligtype angir hva partene selv har oppgitt om eventuell bebyggelse vedørerende registerenhetsretten. Brukstype angir hva partene selv har oppgitt er registerenhetsrettens brukstype.

**Schema:**

| Column                           | Type      |
| -------------------------------- | --------- |
| omsattRegisterenhetsrettId       | bigint    |
| zk_omsetningId                   | bigint    |
| zk_registerenhetsrettId          | bigint    |
| zk_boligtypekodeid               | bigint    |
| zk_brukstypekodeid               | bigint    |
| omsattRegisterenhetsrettKategori | string    |
| oppdateringsdato                 | timestamp |
| from_datetime                    | timestamp |
| to_datetime                      | timestamp |
| zx_ingest_timestamp              | timestamp |

---

### dim_overfoering_omfatter_encrypted

**Description:**

Tabellen inneholder hvilke registerenhetsretter eller registerenhetsrettsandel som en rettsstiftelse/heftelse er overført fra og overført til i forbindelse med en overføringen. Informasjon om overføringen ligger i fact_overfoering_encrypted, som kan knyttes til med zk_overfoeringId.

For hver oppføring vil ENTEN zk_fra_registerenhetsrettId og zk_til_registerenhetsrettId har verdier ELLER zk_fra_registerenhetsrettsandelId og zk_til_registerenhetsrettsandelId ha verdier. zk_fra_registerenhetsrettId angir registerenhetsretten en heftelse er overført fra, og zk_til_registerenhetsrettId angir registerenhetsretten den er overført til. zk_fra_registerenhetsrettsandelId angir registerenhetsrettsandelen en heftelse er overført fra, og zk_til_registerenhetsrettsandelId angir registerenhetsrettsandelen den er overført til.

**Schema:**

| Column                            | Type      |
| --------------------------------- | --------- |
| overfoeringOmfatterId             | bigint    |
| zk_overfoeringId                  | bigint    |
| zk_fra_registerenhetsrettId       | bigint    |
| zk_til_registerenhetsrettId       | bigint    |
| zk_fra_registerenhetsrettsandelId | bigint    |
| zk_til_registerenhetsrettsandelId | bigint    |
| keyId                             | bigint    |
| oppdateringsdato                  | timestamp |
| from_datetime                     | timestamp |
| to_datetime                       | timestamp |
| zx_ingest_timestamp               | timestamp |

---

### dim_periodekoder

**Description:**

**Schema:**

| Column           | Type      |
| ---------------- | --------- |
| periodekodeid    | bigint    |
| periode          | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

### dim_registerenhet

**Description:**

En registerenhet er enheten man registrerer en rettsstiftelse på. For en fast eiendom er registerenheten en matrikkelenhet, for borett er det en borettslagsandel. Dette angis i kolonnen _registerenhetKategori_. Registerenheter som er matrikkelenheter kan knyttes til matrikkelenheter i matrikkelen med kommunenummer, gaardsnummer, bruksnummer, festenummer og/eller seksjonsnummer. Verdi lik 0 i disse feltene tilsvarer en nullverdi. Kommunenummer er lagret i dim_kommune og kan knyttes til med fremmednøkkel zk_kommuneId i fact_registerenhet.

Registerenheter som er en borettslagsandel har fremmednøkkel zk_borettslagId til dim_borettslag og har et andelsnummer.

Registerenhet er delt i dim_registerenhet og fact_registerenhet. Fremmednøkler finnes i fact_registerenhet. Begge har primærnøkkel registerenhetId.

**Schema:**

| Column                        | Type      |
| ----------------------------- | --------- |
| registerenhetId               | bigint    |
| registerenhetKategori         | string    |
| utgaatt                       | boolean   |
| gaardsnummer                  | int       |
| bruksnummer                   | int       |
| festenummer                   | int       |
| seksjonsnummer                | int       |
| andelsnummer                  | int       |
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

| Column                      | Type      |
| --------------------------- | --------- |
| registerenhetsrettId        | bigint    |
| zk_registerenhetId          | bigint    |
| zk_registerenhetsrettKodeId | bigint    |
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

| Column                     | Type      |
| -------------------------- | --------- |
| registerenhetsrettsandelId | bigint    |
| lopenummer                 | int       |
| historisk                  | boolean   |
| keyId                      | bigint    |
| oppdateringsdato           | timestamp |
| from_datetime              | timestamp |
| to_datetime                | timestamp |
| zx_ingest_timestamp        | timestamp |

---

### dim_registerenhetsrettstypekoder

**Description:**

**Schema:**

| Column                        | Type      |
| ----------------------------- | --------- |
| registerenhetsrettstypekodeId | bigint    |
| registerenhetsrettstype       | string    |
| oppdateringsdato              | timestamp |
| from_datetime                 | timestamp |
| to_datetime                   | timestamp |

---

### dim_registerenhettypekoder

**Description:**

**Schema:**

| Column                  | Type      |
| ----------------------- | --------- |
| registerenhettypekodeId | bigint    |
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

| Column                 | Type      |
| ---------------------- | --------- |
| rettsstiftelseId       | bigint    |
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

### dim_saksinformasjon_encrypted

**Description:**

Denne tabellen inneholder saksinformasjon, som er informasjon om en _sak_. En sak oppretter et dokument, og flere dokumenter kan referere til samme sak.

Saksinformasjon og tilhørende dokumenter kan knyttes med fremmednøkkel zk_saksinformasjon i fact_dokument.

Saksinformasjon er knyttet til en til tre _sakspersoner_. Sakspersoner er lagret i dim_saksperson_encrypted, som inneholder fremmednøkkel zk_saksinformasjonId.

Saksinformasjon er delt i dim_saksinformasjon_encrypted og fact_saksinformasjon_encrypted.

**Schema:**

| Column              | Type      |
| ------------------- | --------- |
| saksinformasjonId   | bigint    |
| saksnummer          | int       |
| keyId               | bigint    |
| oppdateringsdato    | timestamp |
| from_datetime       | timestamp |
| to_datetime         | timestamp |
| zx_ingest_timestamp | timestamp |

---

### dim_saksperson_encrypted

**Description:**

Denne tabellen inneholder informasjon om sakspersoner. Personene kan både være norske eller utenlandske borgere eller organisasjoner.

Tabellen inneholder informasjon om personen slik den var da saken ble registrert og blir ikke oppdatert siden. Det betyr at for eksempel hvis en person har endret identifikasjonsnummer (f.eks. gått fra D-nummer til fødselsnummer) kan vedkommende ikke knyttes på tvers av dim_saksperson_encrypted og dim_fysisk_person_encrypted, siden kun sistnevnte vil bli oppdatert.

En oppføring i saksinformasjon har en til tre tilhørende sakspersoner. En saksinformasjon kan kun ha opptil én saksperson av hver sakspersonrolle: "innsender", "mottaker" og "fakturamottaker".

**Schema:**

| Column                             | Type      |
| ---------------------------------- | --------- |
| sakspersonId                       | bigint    |
| zk_saksinformasjonId               | bigint    |
| zk_identifikasjonsnummerTypeKodeId | bigint    |
| identifikasjonsnummer              | string    |
| sakspersonrolle                    | string    |
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

### dim_valutakode

**Description:**

**Schema:**

| Column           | Type      |
| ---------------- | --------- |
| valutakodeid     | bigint    |
| valutakode       | string    |
| oppdateringsdato | timestamp |
| from_datetime    | timestamp |
| to_datetime      | timestamp |

---

## FACT TABLES

---

### fact_dokument

**Description:**

Det er dokumenter som tinglyses. Et dokument kan inneholde flere bestemmelser som skal tinglyses. Hver slik bestemmelse registreres inn som en _rettsstiftelse_ tilhørende dokumentet. En rettsstiftelse har altså hverken selvstendig dato eller tinglyststatus, det er dokumentets dato og status som gjelder. zk_dokumentId i fact_rettsstiftelse angir rettsstiftelsens dokument. registreringstidspunkt i fact_dokument angir dokumentets dato. zk_dokumentstatusKodeId i fact_dokument knyttes til dim_dokumentstatuskoder for å angi dokumentets status (f.eks. "tinglyst"). Dokument er delt i dim_dokument og fact_dokument, begge med primary key dokumentId.

**Schema:**

| Column                      | Type      |
| --------------------------- | --------- |
| dokumentId                  | bigint    |
| zk_saksinformasjonId        | bigint    |
| zk_omdokulerttil_dokumentId | bigint    |
| zk_embetekodeId             | bigint    |
| zk_dokumentstatusKodeId     | bigint    |
| zk_valutaKodeId             | bigint    |
| gebyrbeloepsverdi           | int       |
| gebyrbeloepstekst           | string    |
| registreringstidspunkt      | timestamp |
| oppdateringsdato            | timestamp |
| zx_ingest_timestamp         | timestamp |

---

### fact_omsetning_beloep_encrypted

**Description:**

Denne tabellen inneholder pengebeløp knyttet til en omsetning. Beløp er oppgitt i et helt tall uten desimaler. Den tilhørende omsetningen kan finnes i dim_omsetning_encrypted / fact_omsetning_encrypted med fremmednøkkelen zk_omsetningId.

**Schema:**

| Column                  | Type      |
| ----------------------- | --------- |
| omsetningBeloepId       | bigint    |
| zk_omsetningId          | bigint    |
| zk_valutakodeId         | bigint    |
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

Beløp knyttet til en omsetning ligger i fact_omsetning_beloep_encrypted, som knyttes til dim_omsetning/fact_omsetning ved zk_omsetningId. Hvilke registerenhetsretter som er omsatt kan finnes i dim_omsattregisterenhetsrett_encrypted.

**Schema:**

| Column                    | Type      |
| ------------------------- | --------- |
| omsetningId               | bigint    |
| zk_omsetningstypeKodeId   | bigint    |
| zk_dokavgiftsaarsakKodeId | bigint    |
| keyId                     | bigint    |
| oppdateringsdato          | timestamp |
| zx_ingest_timestamp       | timestamp |

---

### fact_overfoering_encrypted

**Description:**

Tabellen inneholder overføringer av rettsstiftelser. Når heftelser overføres i forbindelse med fradeling, seksjonering med flere, logges hvilke heftelser som blir overført, hvilken rettsstiftelse som er årsak til overføringen, hvilke Registerenhetsretter heftelsene overføres fra og hvilke Registerenhetsretter (eller Registerenhetsrettsandeler) heftelsene overføres til.

zk_overfoert_rettstiftelseId angir rettstiftelseId til den overførte rettsstiftelsen (heftelsen). zk_overfoerende_rettstiftelseId angir rettstiftelseId til den rettsstiftelsen som er årsak til overføringen.

Registerenhetsrettene og/eller registerenhetsrettsandelene som rettsstiftelsene/heftelsene er overført fra og overført til er lagret i dim_overfoering_omfatter_encrypted, som kan knyttes til fact_overfoering_encrypted på zk_overfoeringId.

**Schema:**

| Column                          | Type      |
| ------------------------------- | --------- |
| overfoeringId                   | bigint    |
| zk_overfoert_rettstiftelseId    | bigint    |
| zk_overfoerende_rettstiftelseId | bigint    |
| oppdateringsdato                | timestamp |
| zx_ingest_timestamp             | timestamp |

---

### fact_registerenhet

**Description:**

En registerenhet er enheten man registrerer en rettsstiftelse på. For en fast eiendom er registerenheten en matrikkelenhet, for borett er det en borettslagsandel. Dette angis i kolonnen _registerenhetKategori_. Registerenheter som er matrikkelenheter kan knyttes til matrikkelenheter i matrikkelen med kommunenummer, gaardsnummer, bruksnummer, festenummer og/eller seksjonsnummer. Verdi lik 0 i disse feltene tilsvarer en nullverdi. Kommunenummer er lagret i dim_kommune og kan knyttes til med fremmednøkkel zk_kommuneId i fact_registerenhet.

Registerenheter som er en borettslagsandel har fremmednøkkel zk_borettslagId til dim_borettslag og har et andelsnummer.

Registerenhet er delt i dim_registerenhet og fact_registerenhet. Fremmednøkler finnes i fact_registerenhet. Begge har primærnøkkel registerenhetId.

**Schema:**

| Column                            | Type      |
| --------------------------------- | --------- |
| registerenhetId                   | bigint    |
| zk_kommuneId                      | bigint    |
| zk_borettslagId                   | bigint    |
| zk_adresseId                      | bigint    |
| zk_omnummererttil_registerenhetId | bigint    |
| oppdateringsdato                  | timestamp |
| zx_ingest_timestamp               | timestamp |

---

### fact_registerenhetsrettsandel_encrypted

**Description:**

En Registerenhetsrettsandel representerer andelen en person har i en Registerenhetsrett. Andelen er ikke lokalisert til en bestemt del av en registerenhet, men angir kun en brøk. Denne andelen kan være resultatet av en eller flere overdragelser, og representerer alltid summen av disse. Hvis andelen er historisk, angir den en tidligere slik summert andel.

Realsameier og jordsameier eies av registerenheter istedenfor personer (de eies indirekte av de personene som til enhver tid eier disse registerenhetene igjen). I dette tilfellet er eier angitt ved zk_realkobletTil_registerenhetId som fremmednøkkel til dim_registerenhet / fact_registerenhet.

Registerenhetsrettsandel er delt i dim_registerenhetsrettsandel og fact_registerenhetsrettsandel. Begge har primærnøkkel registerenhetsrettsandelId. Eierandelen er angitt med brøk og teller i fact_registerenhetsrettsandel.

**Schema:**

| Column                           | Type      |
| -------------------------------- | --------- |
| registerenhetsrettsandelId       | bigint    |
| zk_registerenhetsrettId          | bigint    |
| zk_rettighetshaver_personId      | bigint    |
| zk_realkobletTil_registerenhetId | bigint    |
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

| Column                       | Type      |
| ---------------------------- | --------- |
| rettsstiftelseId             | bigint    |
| zk_dokumentId                | bigint    |
| zk_omsetningId               | bigint    |
| zk_rettsstiftelsestypeKodeId | bigint    |
| zk_periodekodeId             | bigint    |
| zk_aarsaksparagrafkodeId     | bigint    |
| zk_aarsaksgebyrfritakkodeId  | bigint    |
| zk_anketypekodeId            | bigint    |
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

### fact_saksinformasjon_encrypted

**Description:**

Denne tabellen inneholder saksinformasjon, som er informasjon om en _sak_. En sak oppretter et dokument, og flere dokumenter kan referere til samme sak.

Saksinformasjon og tilhørende dokumenter kan knyttes med fremmednøkkel zk_saksinformasjon i fact_dokument.

Saksinformasjon er knyttet til en til tre _sakspersoner_. Sakspersoner er lagret i dim_saksperson_encrypted, som inneholder fremmednøkkel zk_saksinformasjonId.

Saksinformasjon er delt i dim_saksinformasjon_encrypted og fact_saksinformasjon_encrypted.

**Schema:**

| Column              | Type      |
| ------------------- | --------- |
| saksinformasjonId   | bigint    |
| behandlingsutfall   | string    |
| sakstatus           | string    |
| mottaksdato         | timestamp |
| foelgebrevsdato     | timestamp |
| keyId               | bigint    |
| oppdateringsdato    | timestamp |
| zx_ingest_timestamp | timestamp |

---
