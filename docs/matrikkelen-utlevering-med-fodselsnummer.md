# Tabelldokumentasjon

_Generert 2026-09-25T09:57:26+00:00_

## Tabeller

- `bridge_adresse_krets_v1`
- `bridge_krets_kommune_v1`
- `code_adressetilleggsnavnkildekode_v1`
- `code_anleggstypekode_v1`
- `code_annenmatrikkelenhetskode_v1`
- `code_arealkildekode_v1`
- `code_atkomsttypekode_v1`
- `code_bruksenhetstypekode_v1`
- `code_etasjeplankode_v1`
- `code_formalseksjonkode_v1`
- `code_generellkretstypekode_v1`
- `code_kjokkentilgangkode_v1`
- `code_kommunalkretstypekode_v1`
- `code_koordinatsystemkode_v1`
- `dim_adresse_v1`
- `dim_atkomst_v1`
- `dim_bruksenhet_v1`
- `dim_fylke_v1`
- `dim_kommune_v1`
- `dim_krets_v1`
- `dim_matrikkelenhet_v1`
- `dim_veg_v1`
# `bridge_adresse_krets_v1`

Nåtidskoblinger mellom adresser og kretser. Én rad per adresse og krets.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `adresse_id` | bigint |  |
| `krets_id` | bigint |  |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```

# `bridge_krets_kommune_v1`

Nåtidskoblinger mellom kretser og kommuner. Én rad per krets og kommune.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `krets_id` | bigint |  |
| `kommune_id` | bigint |  |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```

# `code_adressetilleggsnavnkildekode_v1`

Opphav til adressetilleggsnavn og årsaken til at navnet er registrert i Matrikkelen. Se Geonorge objektkatalog.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_anleggstypekode_v1`

Type anlegg som anleggseiendommen representerer, for eksempel tunnel, bro, parkering eller bolig.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_annenmatrikkelenhetskode_v1`

Typer annen matrikkelenhet, blant annet ikke oppgitt og bestående registrert bruksrett.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_arealkildekode_v1`

Hvordan arealet er framkommet, for eksempel målebrev, registreringsbrev eller areal hentet fra eiendomsbase.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_atkomsttypekode_v1`

Type atkomst, for eksempel sommer-, vinter-, nødetat- eller øyatkomst.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_bruksenhetstypekode_v1`

Typer bruksenheter i en bygning, for eksempel bolig, fritidsbolig og ikke godkjent bolig.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_etasjeplankode_v1`

Etasjeplanbetegnelse som viser hovedetasje, kjelleretasje, loft eller underetasje.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_formalseksjonkode_v1`

Lovlige formål for seksjoner, blant annet boligseksjon, næringsseksjon og samleseksjon.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_generellkretstypekode_v1`

Generelle kretstyper for grunnkrets, valgkrets, kirkesogn, postnummerområde og tettsted.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_kjokkentilgangkode_v1`

Tilknytning til kjøkken i bruksenheten: kjøkken, felles kjøkken eller ikke kjøkken.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_kommunalkretstypekode_v1`

Kretstyper som bare er gyldige i én kommune, blant annet skolekrets.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `kommune_id` | bigint | Kommunen kretstypen gjelder for. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `code_koordinatsystemkode_v1`

Koordinatsystem som angir geografisk koordinatsystem eller kartplan, sone og akse. Inneholder SOSI- og EPSG-kode.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `sosi_kode` | int | SOSI-kode for koordinatsystemet. |
| `epsg_kode` | int | EPSG-kode for koordinatsystemet. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
```

# `dim_adresse_v1`

Adresser i matrikkelen — nåtidsbilde med én rad per adresse. Vegadresse og Matrikkeladresse er samlet med `adressetype` som diskriminator. Type-spesifikke felt er NULL for den andre adressetypen. adresse_id er teknisk/API-identitet. Vegadresse har logisk identitet bestående av kommuneident, adressekode, nummer og eventuell bokstav. Matrikkeladresse har logisk identitet bestående av kommuneident, matrikkelnummer (gårdsnummer, bruksnummer og festenummer) og undernummer; seksjonsnummer inngår ikke. Matrikkeladresse kan ikke knyttes til Veg, og nummer og bokstav er derfor ikke utfylt. Historiske versjoner eksponeres ikke.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `adresse_id` | bigint | Teknisk/API-identitet for adressen. |
| `adressetype` | string | Adressetype. Verdier: vegadresse og matrikkeladresse. Matrikkeladresse kan ikke knyttes til Veg. |
| `representasjonspunkt_x` | double | Posisjonen i kartet i nord- og østkoordinater. Kan også inneholde høyde på representasjonspunkt for adresse. For andre representasjonspunkt brukes ikke høyden. Må være gitt. |
| `representasjonspunkt_y` | double | Posisjonen i kartet i nord- og østkoordinater. Kan også inneholde høyde på representasjonspunkt for adresse. For andre representasjonspunkt brukes ikke høyden. Må være gitt. |
| `representasjonspunkt_z` | double | Posisjonen i kartet i nord- og østkoordinater. Kan også inneholde høyde på representasjonspunkt for adresse. For andre representasjonspunkt brukes ikke høyden. Må være gitt. |
| `representasjonspunkt_koordinatsystem_kode_id` | bigint | Koordinatsystem som posisjonen er oppgitt i. |
| `representasjonspunkt_original_koordinatsystem_kode_id` | bigint | Verdi for orginalt koordinatsystem. Dette blir kun satt dersom representasjonspunktet blir transformert ved henting! |
| `representasjonspunkt_stedfesting_verifisert` | boolean | Angir omrepresentasjonspunktet for adresse og bygning er stedfestingVerifisert. |
| `adressetilleggsnavn` | string | Nedarvet bruksnavn, navn på en institusjon eller bygning eller grend brukt som del av den offisielle adressen. Merknad: Eier kan kreve og kommunen kan tildele adressetilleggsnavn til en offisiell adresse etter vilkår i matrikkelforskriften § 54 og § 55. Hvilken regel den er tildelt etter skal registreres i matrikkelen (adressetilleggsnavnkilde). |
| `kortnavn` | string | En forkortelse av matrikkeladressenavnet dersom dette er på over 25 tegn. Hvis adressetilleggsnavnet er på 25 tegn eller mindre vil kortAdressetilleggsnavn inneholde det samme navnet. Merknad: Skal alltid brukes ved utveksling av data med andre systemer. |
| `matrikkelenhet_id` | bigint | Matrikkelenheten adressen ligger på. For matrikkeladresse brukes matrikkelnummeret fra matrikkelenheten i den logiske adressidentiteten. |
| `tilleggsnavn_kilde_kode_id` | bigint | Opprinnelsen til adressetilleggsnavnet. (§§ 54 og 55 i matrikkelforskriften). |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `veg_id` | bigint | Vegen adressen er knyttet til. NULL for matrikkeladresse, som ikke kan knyttes til Veg. |
| `nummer` | int | Del av adressenummer for vegadresse. Skal være NULL for matrikkeladresse. |
| `bokstav` | string | Eventuell bokstav som inngår i adressenummeret for vegadresse. Skal være NULL for matrikkeladresse. |
| `undernummer` | int | Fortløpende nummerering av matrikkeladresser med samme gårds-, bruks- og festenummer. Inngår i den logiske identiteten til matrikkeladresse. Nummer og bokstav er ikke utfylt for matrikkeladresse. |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```

# `dim_atkomst_v1`

Gjeldende atkomster for adresser. Én rad per adresse og atkomst.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `adresse_id` | bigint | Id for en adresse. Original felt i API: id.value |
| `atkomst_id` | bigint |  |
| `atkomsttype_kode_id` | bigint |  |
| `punkt_x` | double | x-verdi(øst) for posisjonen. Kan ikke være 0. |
| `punkt_y` | double | y-verdi(nord) for posisjonen. Kan ikke være 0. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Når atkomsten sist ble oppdatert i matrikkelen. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```

# `dim_bruksenhet_v1`

Bruksenheter i matrikkelen med siste autoritative bruksenhetsnummer — nåtidsbilde med én rad per bruksenhet.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `bruksenhet_id` | bigint | Id for en bruksenhet. Original felt i API: id.value |
| `bruksenhetsnummer` | string | Autoritativt bruksenhetsnummer hentet fra BruksenhetService. |
| `bygg_id` | bigint | Bygningen denne bruksenheten er knyttet til, kan ikke være null. |
| `etasjeplan_kode_id` | bigint | Etasjeplanet bruksenheten ligger på. Kan for eksempel være hovedetasje eller underetasje. Standardverdi er EtasjeplanKode.IkkeOppgitt. |
| `etasjenummer` | int | Etasjenr innenfor etasjeplanet bruksenheten ligger på; del av logisk ident. |
| `lopenummer` | int | Løpenr innenfor etasjen bruksenheten ligger på; del av logisk ident. |
| `adresse_id` | bigint | Adressen til bruksenheten; del av logisk ident. |
| `matrikkelenhet_id` | bigint | Matrikkelenheten bruksenheten ligger på; del av logisk ident. Intern ID for Matrikkelenhet. |
| `bruksenhetstype_kode_id` | bigint | Hva bruksenheten brukes til. Er en av gitte, lovlige typer. |
| `antall_rom` | int | Antall rom for varig opphold, for eksempel stue, soverom, peisestue, kontor og lignende. For bygningsendringer kan det være negativt, for bygning må det være 0 eller større. |
| `antall_bad` | int | Antall bad i bruksenheten, inkludert rom med dusj. For bygningsendringer kan det være negativt, for bygning må det være 0 eller større. |
| `antall_wc` | int | Antall klosettskåler i bruksenheten. For bygningsendringer kan det være negativt, for bygning må det være 0 eller større. |
| `bruksareal` | double | Alt bruksareal som hører til bruksenheten, uansett etasje. Boder og rom i underetasje og kjeller i blokker o.l. skal tas med dersom de tydelig tilhører de enkelte bruksenhetene spesielt. Rom som er felles for flere bruksenheter, f.eks felles trapp, gangareal, fellesrom og boder som ikke kan spesifiseres på bruksenhet tas derimot ikke med. Måling av bruksareal følger NS 3940. Unntak er at arealene skal gis i hele kvm. Arealet for store piper og kanaler trekkes ikke fra. |
| `kjokkentilgang_id` | bigint | Bruksenhetens tilknytning til kjøkken. Er en av lovlige koder. |
| `skal_utga` | boolean | Om bruksenheten skal utgå ved ferdigstillelse av ombygging. Skal kun kunne være true for bruksenheter på Bygning. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp |  |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```

# `dim_fylke_v1`

Norske fylker — nåtidsbilde. Én rad per fylke, siste versjon fra matrikkelen. Historiske versjoner eksponeres ikke; utgåtte fylker er med og markert via `gyldig_til_dato` og `ny_fylke_id` for etterfølger.

Innholder fylkesknytning for en en kommune slik en matrikkelenhet kan plasseres geografisk innefor en kommune og igjen innenfor et fylke. Dette gjør at feks Svalbard er med i dette datasettet selv om det ikke er en av Norges fylker, for å kunne definere matrikkelenheter på Svalbard. TESTFYLKE eksisterer ikke i dette datasettet, men finnes i tilsvarende tjenester i M22.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `fylke_id` | bigint | Id for et fylke. Original felt i API: id.value |
| `fylkesnummer` | string | Entydig tosifret nummer på fylke. Skal skrives med ledende nuller. |
| `fylkesnavn` | string | Entydig navn på fylket. |
| `gyldig_til_dato` | date | Eventuell dato for når fylket utgikk. Original felt i API: gyldigTilDato |
| `ny_fylke_id` | bigint | Hvis fylket er sammenslått, ligger peker til nytt fylke her. Original felt i API: nyFylkeId.value |
| `kommune_ids` | array<bigint> | Id-er for kommunene innenfor dette fylket. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```

# `dim_kommune_v1`

Norske kommuner — nåtidsbilde. Én rad per kommune, siste versjon fra matrikkelen. Historiske versjoner eksponeres ikke; utgåtte kommuner er med og markert via `gyldig_til_dato` og `ny_kommune_id` for etterfølger.

Inneholder kommuner slik at en matrikkelenhet kan plasseres geografisk innenfor en kommune, som igjen ligger innenfor et fylke. Dette gjør at det finnes kommuner på Svalbard i dette datasettet, selv om de ikke er en del av de offisielle kommunene i Norge. Dette er for å kunne plassere matrikkelenheter geografisk på Svalbard. TESTKOMMUNE eksisterer ikke i dette datasettet, men finnes i tilsvarende tjeneste i M22.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kommune_id` | bigint | Id for en kommune. Original felt i API: id.value |
| `kommunenummer` | string | Firesifret entydig kommunenr. Skal skrives med ledende nuller. |
| `kommunenavn` | string | Navn på kommune. Navnet er ikke entydig. |
| `fylke_id` | bigint | Id til fylket kommunen hører til. Original felt i API: fylkeId.value |
| `gyldig_til_dato` | date | Eventuell dato for når kommunen utgikk. Original felt i API: gyldigTilDato |
| `ny_kommune_id` | bigint | Hvis kommunen er sammenslått, ligger peker til ny kommune her. Hvis ny kommune er gitt, må utgatt også være gitt. Original felt i API: nyKommuneId.value |
| `representasjonspunkt_x` | double | Posisjonen i kartet i nord- og østkoordinater. Kan også inneholde høyde på representasjonspunkt for adresse. For andre representasjonspunkt brukes ikke høyden. Må være gitt. |
| `representasjonspunkt_y` | double | Posisjonen i kartet i nord- og østkoordinater. Kan også inneholde høyde på representasjonspunkt for adresse. For andre representasjonspunkt brukes ikke høyden. Må være gitt. |
| `representasjonspunkt_koordinatsystem_kode_id` | bigint | Koordinatsystem som posisjonen er oppgitt i. |
| `representasjonspunkt_original_koordinatsystem_kode_id` | bigint | Verdi for orginalt koordinatsystem. Dette blir kun satt dersom representasjonspunktet blir transformert ved henting! |
| `nabo_kommune_ids` | array<bigint> | Et sett med KommuneId for kommunens nabokommuner. Også kommuner som deler kun ett grensepunkt, skal være naboer. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```

# `dim_krets_v1`

Kretser i matrikkelen — nåtidsbilde med én rad per krets.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `krets_id` | bigint | Id for en krets. Original felt i API: id.value |
| `kretsnummer` | int | Kretsens nummer som er unikt innen en kommune og en kretstype. Må være gitt. |
| `kretsnavn` | string | Kretsens navn. Kan være blankt eller null. |
| `kretstype_kode_id` | bigint | Referanse til kretstype. Kodelisten kan også inneholde kommunalt definerte kretstyper. |
| `kretsflate_id` | bigint | Id for Kretsflate, som inneholder kretsens geometri. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `bispedomme` | int | Entydig nummer på bispedømmet som kirkesognet hører til. Gjelder Kirkesogn. |
| `prosti` | int | Nummer på prosti under bispedømmet. Gjelder Kirkesogn. |
| `prestegjeld` | int | Nummer på prestegjeld under prostiet. Gjelder Kirkesogn. |
| `sogn` | int | Organisasjonsnummer som etter hvert skal bli den offisielle identifikasjonen av kirkesogn. Gjelder Kirkesogn. |
| `oppdateringsdato` | timestamp | Viser når objektet sist ble endret. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```

# `dim_matrikkelenhet_v1`

Norske matrikkelenheter (grunneiendom, seksjon, festegrunn, jordsameie, anleggseiendom, annen_matrikkelenhet) — nåtidsbilde. Én rad per matrikkelenhet, siste versjon fra matrikkelen, med `matrikkelenhetstype`-diskriminator. Historiske versjoner eksponeres ikke; utgåtte enheter er med markert via `utgatt=true` (kildens boolean, ikke SCD-tid). Felt som gjelder kun enkelte matrikkelenhetstyper er NULL ellers. Teigtilknytning og eierforhold eksponeres i egne bridge- og fact-tabeller.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `matrikkelenhet_id` | bigint | Id for en matrikkelenhet. |
| `matrikkelenhetstype` | string | Matrikkelenhetstype. Verdier: grunneiendom (ordinær eiendom), seksjon (eierseksjon), festegrunn (areal festet bort), jordsameie (areal eid i fellesskap), anleggseiendom (anlegg under eller over bakken) og annen_matrikkelenhet (annen type matrikkelenhet). |
| `kommune_id` | bigint | Del av matrikkelenhetens identifikasjon. Matrikkelnummeret er unikt for hver matrikkelenhet innen en kommune. |
| `gardsnummer` | int | En kommune er delt inn i flere gårder, og alle matrikkelenheter ligger på en gårdsenhet. Gårdsnummer er nummeret på en gårdsenhet i matrikkelen og er unikt innenfor hver kommune. Forkortelsen er gnr. Gårdsnr må være større enn 0. |
| `bruksnummer` | int | Hver gård er delt opp i et eller flere bruk. Neste ledige bruksnummer innen et gårdsnummer tildeles automatisk. Forkortelsen er bnr. Bruksnr må være større enn 0. |
| `festenummer` | int | Fortløpende nummerering av fester under gårdsnummer/bruksnummer. Forkortelsen er fnr. Festenr må være større enn eller lik 0. |
| `seksjonsnummer` | int | Fortløpende nummerering av seksjoner under gårdsnummer/bruksnummer og eventuelt festenummer. Seksjonsnr må være større enn eller lik 0. |
| `stedsnummer` | string | Hentes fra Stedsnavn-applikasjonen. Nullable. |
| `etableringsdato` | date | For matrikkelenheter etablert etter ikrafttredelse av matrikkelloven § 24 (1.1.2010) inneholder feltet dato for oppretting i matrikkelen slik: -Dato for føring i matrikkelen, dersom matrikkelenheten ikke er tinglyst. -Dato for tinglysing av matrikkelenheten dersom den er tinglyst. For matrikkelenheter etablert etter innføring av matrikkelen, men før ikrafttredelse av matrikkelloven, inneholder feltet dato for føring i matrikkelen. For matrikkelenheter etablert etter 1980, men før innføring av matrikkelen, inneholder feltet dato for tildeling av registernummer. Unntak for seksjoner der feltet inneholder dato for tinglysing. For matrikkelenheter etablert før 1980 inneholder feltet dato for dagbokføring. Egenskapen etableringsdato oppdateres med tinglysingsdato når egenskapen tinglyst settes til Ja (ved mottatt melding fra tinglysingen). |
| `historisk_oppgitt_areal` | double | Arealet er konvertert fra GAB, og er et areal som framgår av ulike (eldre) dokumenter.  Er ikke nødvendigvis oppdatert, og det er ikke noe oppdateringsregime rundt dette i matrikkelen. |
| `historisk_arealkilde_id` | bigint | Kilde for historisk oppgitt areal. Standardverdi er ArealkildeKode.IkkeOppgitt. |
| `tinglyst` | boolean | Om matrikkelenheten er tinglyst eller ikke. At den er tinglyst kommer fra Tinglysingssystemet. |
| `skyld` | double | Skyld (historisk) er en eiendoms skatteevne (avkastningsevne) og sier noe om eiendommens størrelse. Frem til 1830 ble statsskatt skrevet ut på grunnlag av skyldverdien, og først i 1886 ble kommuneskatten lagt om til å bli beregnet på grunnlag av inntekt og formue. Etter 1886 fikk derfor skyldverdiene mindre betydning, men særlig skyldverdiene fra før 1838 kan fremdeles ha betydning for å fastsette en eiendoms andel i sameie, felles jakt o.l. |
| `bruksnavn` | string | Navn på matrikulert eiendom, jf. § 8 i lov om stadnamn. Jf. gårdsnavn. |
| `er_seksjonert` | boolean | Angir om matrikkelenheten er seksjonert eller ikke. |
| `har_aktive_festegrunner` | boolean | Flagg som angir om matrikkelenheten har aktive festegrunner eller ikke. Dvs. om det finnes minst en Festegrunn med status ikke utgått, som har denne som festet på. |
| `har_anmerket_klage` | boolean | Flagg som forteller om det er innkommet klage som angår matrikkelenheten. Detaljer om klagen finnes i egen klasse. |
| `har_registrert_grunnerverv` | boolean | Flagg som forteller om matrikkelenheten er involvert i grunnerverv til offentlig veg eller jernbane.  Detaljer om grunnerverv finnes i egen klasse. |
| `har_registrert_jordskifte_krevd` | boolean | Flagg som forteller om det er krevd jordskifte som involverer matrikkelenheten.  Detaljer om jordskiftet finnes i egen klasse. |
| `inngar_i_samla_fast_eiendom` | boolean | Flagg for å angi om matrikkelenheten inngår i samla fast eiendom eller ikke. Detaljer finnes i egen klasse. |
| `har_grunnforurensing` | boolean | Flagg som forteller om matrikkelenheten har registrert grunnforurensing, dvs om det finnes minst en Grunnforurensing som den er knyttet til. Detaljer om grunnforurensing finnes i egen klasse, og opphavet er Klifs register over grunnforurensing. Opplysningene vedlikeholdes fra Klifs register via koblinger. |
| `har_kulturminne` | boolean | Flagg som forteller om matrikkelenheten har registrert kulturminner fra Askeladden. Detaljer om kulturminner finnes i egen klasse, og opphavet er Riksantikvarens register over kulturminner (Askeladden). Opplysningene vedlikeholdes fra Askeladden via koblinger. |
| `har_avtale_grense_punktfeste` | boolean | Flagg som forteller om matrikkelenheten er koblet til en eller flere avtaler om eksisterende grense/punktfeste. Detaljer om avtalen finnes i egen klasse. |
| `har_avtale_stedbunden_rettighet` | boolean | Flagg som forteller om matrikkelenheten er koblet til en eller flere avtaler om stedbunden rettighet. Detaljer om avtalen finnes i egen klasse. |
| `utgatt` | boolean | Matrikkelenheten består ikke mer som registreringsenhet. Matrikkelenheten kan være utgått ved sammenslåing, når festegrunn blir omgjort til grunneiendom eller den kan utgå av andre årsaker. Merknad: Årsaken til at matrikkelenheten er utgått kan finnes i forretningshistorikken til matrikkelenheten. Utgått ved sammenslåing: Det vil finnes en forretning av typen 'Sammenslåing' hvor utgått matrikkelenhet har rollen 'Avgiver'. Feste gitt bruksnummer: Det vil finnes en forretning av typen 'Grunneiendom fra feste' hvor festegrunnen som utgår har rollen 'Tidligere festegrunn'. Utgått av andre årsaker: Det vil finnes en forretning av typen 'Annen forretningstype'. |
| `under_sammenslaing_bestar` | boolean | Om matrikkelenheten er under sammenslåing. Kommunen har registrert hvilke matrikkelenheter som skal sammenslås, og venter på transaksjon fra Tinglysingen som utfører sammenslåingen. Denne matrikkelenheten skal bestå etter at sammenslåingen er fullført. |
| `under_sammenslaing_utgar` | boolean | Om matrikkelenheten er under sammenslåing. Kommunen har registrert hvilke matrikkelenheter som skal sammenslås, og venter på transaksjon fra Tinglysingen som utfører sammenslåingen. Denne matrikkelenheten skal utgå etter at sammenslåingen er fullført. |
| `oppmaling_ikke_fullfort` | boolean | Om oppmålingsforretning ikke er fullfort for denne matrikkelenheten. § 6  i Matrikkellova. Hvis feltet er true, må også dato for fristOppmaling være satt. |
| `grensepunktmerking_mangler` | boolean | Om grensepunktmerking mangler for denne matrikkelenheten. § 6 i Matrikkellova. Hvis feltet er true, må også dato for fristGrensepunktmerking være satt. |
| `mangel_matrikkelforingskrav` | boolean | Om denne matrikkelenheten har mangler ved matrikkelføring.  § 22 i Matrikkellova. Hvis feltet er true, må også dato for fristMatrikkelforingsKrav være satt. |
| `nymatrikulert` | boolean | Om matrikkelenheten er nymatrikulert, dvs den har ingen avgiver. |
| `etter_ml9b_til_h` | boolean | Matrikkelenheten er opprettet med hjemmel i matrikkelloven (lov 2005-06-17 nr. 101) §9 b til h. Egenskapen skal være til hjelp for tinglysingsmyndighetene slik at de ser at matrikkelenheten er opprettet på særskilt grunnlag Merknad: gjelder i tilfeller der noen ved dom eller ekspropriasjon er tilkjent rett til å kreve at et bestemt grunnstykke eller anlegg blir opprettet som egen matrikkelenhet. Dette vil være tilstrekkelig grunnlag for å kreve matrikulering. Med hjemmel i § 9 b eller c kan det således kreves opprettet ny matrikkelenhet også i et uregistrert jordsameie, på teig med flere matrikkelenheter og på tvisteteig. Tilsvarende gjelder for festegrunn som er innløst etter bestemmelsene i tomtefesteloven, jf §9 h. |
| `frist_oppmaling` | date | Tidsfrist for fullføring av oppmåling av matrikkelenheten. Hvis datoen er satt må også feltet for oppmalingIkkeFullfort være true. |
| `frist_grensepunktmerking` | date | Tidsfrist for grensepunktmerking i marka. $25 i matrikkelforskriften. Hvis datoen er satt må også feltet for grensepunktmerkingMangler være true. |
| `frist_matrikkelforingskrav` | date | Tidsfrist for oppfylling av manglene i matrikkelføringskravet. Hvis datoen er satt må også feltet for mangelMatrikkelforingsKrav være true. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `sameiebrok_teller` | bigint | Teller i sameiebrøken for eierseksjonens andel av grunn på den matrikkelenheten den er seksjonert på. |
| `sameiebrok_nevner` | bigint | Nevner i sameiebrøken for eierseksjonens andel av grunn på den matrikkelenheten den er seksjonert på. |
| `formal_seksjon_kode_id` | bigint | Angir formålet med bruken av den enkelte seksjon, jf. eierseksjonslova § 6. Kan ikke være null. |
| `seksjonert_matrikkelenhet_ids` | array<bigint> | Sett med MatrikkelenhetId til matrikkelenheten eller matrikkelenhetene som er seksjonert på grunneiendom eller anleggseiendom. Som oftest er det bare én matrikkelenhet-id i settet, men det kan være flere, og settet kan også være tomt. |
| `tilleggsareal` | boolean | Tillegg til hoveddel, jf. eierseksjonslova § 6 første ledd. Med tilleggsareal menes boder i kjeller eller på loft, terrasser og uteareal. |
| `festet_matrikkelenhet_ids` | array<bigint> | Matrikkelenhet eller matrikkelenheter som er festet på en grunneiendom eller et jordsameie. |
| `punktfeste` | boolean | Punktfeste er feste der det i festeavtalen ikke er sagt noe om størrelsen på tomta. Hensikten med arealet som avgrensingen danner er ikke å angi eksakt areal som punktfestet disponerer, men at elementer som hører til punktfestet, for eksempel bygning og brønn, kommer innenfor flaten. Punktfester skal bare avgrenses av hjelpelinjetype Punktfeste. |
| `avklart_eiere` | boolean | Om det er fullstendig avklart hvilke matrikkelenheter som har andel i jordsameiet. |
| `avklart_andeler` | boolean | Om alle andeler i jordsameiet er avklart. Det vil si hvor stor eierandel hver enkelt matrikkelenhet har i jordsameiet. |
| `anleggstype_id` | bigint | Angir hvilken type anlegg anleggseiendommen omfatter. |
| `annen_matrikkelenhets_kode_id` | bigint | Annen type matrikkelenhet enn de som er nevnt spesielt. Er en av gitte, lovlige typer. Dette er som oftest bruksretter som er gitt eget matrikkelnummer og registrert i Grunnbok og GAB etter eldre lovverk. Standardverdi er AnnenMatrikkelenhetsKode.IkkeOppgitt. |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```

# `dim_veg_v1`

Veger i matrikkelen — nåtidsbilde med én rad per veg.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `veg_id` | bigint | Id for en veg. Original felt i API: id.value |
| `kommune_id` | bigint | Id til vegens Kommune. Vegen må ha knytning til en kommune. |
| `adressekode` | int | Et nummer som entydig identifiserer adresserbare gater, veger, stier, plasser og områder som er ført i matrikkelen. For hvert adressenavn skal det således foreligge en adressekode, jf. matrikkelforskriften § 51.2. Adressekode er unik innenfor kommunen. |
| `adressenavn` | string | Navn på gate, veg, sti, plass eller område som er ført i matrikkelen. (Matrikkelforskriften § 2e) |
| `kort_adressenavn` | string | En forkortelse av adressenavnet dersom dette er på mer enn 22 tegn. Hvis adressenavnet er på 22 tegn eller mindre vil kort adressenavn inneholde det samme navnet. Matrikkelforskriften § 51. Skal alltid brukes ved utveksling av data med andre systemer. |
| `stedsnummer` | string | Viser til referanse i sentralt stedsnavnregister (SSR) |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
delta.enableChangeDataFeed: true
delta.enableDeletionVectors: true
delta.enableRowTracking: true
delta.minReaderVersion: 3
delta.minWriterVersion: 7
delta.parquet.compression.codec: zstd
medallion: gold
scd: type-1
```
