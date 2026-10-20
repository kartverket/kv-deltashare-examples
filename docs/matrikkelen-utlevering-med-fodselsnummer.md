# Tabelldokumentasjon

_Generert 2026-10-20T06:51:03+00:00_

## Tabeller

- `bridge_adresse_krets_v1`
- `bridge_forretning_teig_v1`
- `bridge_forretning_teiggrense_v1`
- `bridge_forretning_teiggrensepunkt_v1`
- `bridge_krets_kommune_v1`
- `bridge_matrikkelenhet_teig_v1`
- `bridge_teig_teiggrense_v1`
- `bridge_teiggrense_teiggrensepunkt_v1`
- `code_administrativgrensekode_v1`
- `code_adressetilleggsnavnkildekode_v1`
- `code_anleggstypekode_v1`
- `code_annenmatrikkelenhetskode_v1`
- `code_arealkildekode_v1`
- `code_arealmerknadkode_v1`
- `code_arsaktilfeilrettingkode_v1`
- `code_arsaktilforingkode_v1`
- `code_atkomsttypekode_v1`
- `code_avlopskode_v1`
- `code_bruksenhetstypekode_v1`
- `code_bygningsendringskode_v1`
- `code_bygningsstatuskode_v1`
- `code_bygningstypekode_v1`
- `code_energikildekode_v1`
- `code_etasjeplankode_v1`
- `code_formalseksjonkode_v1`
- `code_forretningsklassekode_v1`
- `code_forretningstypekode_v1`
- `code_generellkretstypekode_v1`
- `code_grensemerkenedsattikode_v1`
- `code_grensepunkttypekode_v1`
- `code_hjelpelinjetypekode_v1`
- `code_kjokkentilgangkode_v1`
- `code_kommunalkretstypekode_v1`
- `code_koordinatsystemkode_v1`
- `code_malemetodekode_v1`
- `code_naringsgruppekode_v1`
- `code_noyaktighetsklassekode_v1`
- `code_opprinnelseskode_v1`
- `code_oppvarmingskode_v1`
- `code_rolleiforretningkode_v1`
- `code_terrengdetaljkode_v1`
- `code_tinglysingsstatuskode_v1`
- `code_vannforsyningskode_v1`
- `dim_adresse_v1`
- `dim_atkomst_v1`
- `dim_bruksenhet_v1`
- `dim_bygning_v1`
- `dim_bygningsendring_v1`
- `dim_etasje_v1`
- `dim_fylke_v1`
- `dim_kommune_v1`
- `dim_krets_v1`
- `dim_matrikkelenhet_v1`
- `dim_teig_v1`
- `dim_teiggrense_v1`
- `dim_teiggrensepunkt_v1`
- `dim_veg_v1`
- `fact_areal_i_forretning_v1`
- `fact_bygning_statushistorikk_v1`
- `fact_bygningsendring_statushistorikk_v1`
- `fact_forretning_v1`
# `bridge_adresse_krets_v1`

Nåtidskoblinger mellom adresser og kretser. Én rad per adresse og krets.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `adresse_id` | bigint |  |
| `krets_id` | bigint |  |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `bridge_forretning_teig_v1`

Nåtidskoblinger mellom forretninger og teiger. Én rad per forretning og teig. Eldre forretninger kan vise til teiger som ikke lenger finnes i nåtidsdimensjonen.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `forretning_id` | bigint | ID til forretningen teigen er knyttet til. |
| `teig_id` | bigint | ID til teigen som er knyttet til forretningen. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `bridge_forretning_teiggrense_v1`

Nåtidskoblinger mellom forretninger og teiggrenser. Én rad per forretning og teiggrense. Eldre forretninger kan vise til teiggrenser som ikke lenger finnes i nåtidsdimensjonen.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `forretning_id` | bigint | ID til forretningen teiggrensen er knyttet til. |
| `teiggrense_id` | bigint | ID til teiggrensen som er knyttet til forretningen. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `bridge_forretning_teiggrensepunkt_v1`

Nåtidskoblinger mellom forretninger og teiggrensepunkter. Én rad per forretning og teiggrensepunkt. Eldre forretninger kan vise til teiggrensepunkter som ikke lenger finnes i nåtidsdimensjonen.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `forretning_id` | bigint | ID til forretningen teiggrensepunktet er knyttet til. |
| `teiggrensepunkt_id` | bigint | ID til teiggrensepunktet som er knyttet til forretningen. |

## Egenskaper

```yaml
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
medallion: gold
scd: type-1
```

# `bridge_matrikkelenhet_teig_v1`

Nåtidskoblinger mellom matrikkelenheter og teiger. Én rad per matrikkelenhet og teig; TeigForMatrikkelenhet-ID-en beholdes for sporbarhet.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `matrikkelenhet_id` | bigint | Matrikkelenheten som er knyttet til teigen. |
| `teig_id` | bigint | Teigen som er knyttet til matrikkelenheten. |
| `teig_for_matrikkelenhet_id` | bigint | Intern nøkkel for forekomsten. |
| `hovedteig` | boolean | Alle matrikkelenheter har en hovedteig. Dersom matrikkelenheten kun har en teig, så er denne hovedteigen. Dersom matrikkelenheten har flere teiger, velges normalt den teigen der bygningen(e) står, som hovedteig. Hovedteig velges ellers skjønnsmessig, der hovedkriteriet vil være hvilken av teigene som fremstår som den mest sentrale. Hovedteigens representasjonspunkt vil også være matrikkelenhetens representasjonspunkt. Foreslås automatisk slik: hvis én teig så settes den til hovedteig; hvis flere teiger og en eller flere har boligbygg foreslås den største teigen; hvis flere teiger og en eller flere har andre bygg foreslås den største teigen; hvis flere teiger uten bygg foreslås den største teigen. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Når koblingen sist ble oppdatert i matrikkelen. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `bridge_teig_teiggrense_v1`

Nåtidskoblinger mellom teiger og teiggrenser, hentet fra teigens flategeometri.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `teig_id` | bigint | Teigen som teiggrensen avgrenser. Relasjonen er avledet fra geometrien og finnes ikke direkte i databasen: Teig har flate og Teiggrense har forløp. |
| `teiggrense_id` | bigint | Grenselinjen som CurveDirection definerer med retning for et Boundary. |
| `boundary_id` | bigint | Unik ID for Boundary-komponenten. |
| `grense_rolle` | string | Om Boundary inngår som ytre avgrensning (exterior) eller som et hull (interior) i ComplexSurface. |
| `curve_direction_rekkefolge` | int |  |
| `retning` | boolean | Angir om grenselinjen går fra startpunkt til endepunkt (true), eller omvendt. |
| `curve_direction_id` | bigint | Unik ID for CurveDirection-komponenten. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `bridge_teiggrense_teiggrensepunkt_v1`

Nåtidskoblinger mellom teiggrenser og start-/endepunktene deres.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `teiggrense_id` | bigint | Teiggrensen punktet avgrenser. |
| `teiggrensepunkt_id` | bigint | Teiggrensepunktet som er start- eller endepunkt. |
| `punkt_rolle` | string | Punktets rolle på teiggrensen: start eller endepunkt. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `code_administrativgrensekode_v1`

Angir når en teiggrense også er administrativ grense: kommune-, fylkes-, riks- eller territorialgrense.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `kodeverdi_sosi45` | string | SOSI 4.5-verdi for koden. |

## Egenskaper

```yaml
medallion: gold
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
medallion: gold
```

# `code_arealmerknadkode_v1`

Mulige merknader til teigareal, generert blant annet fra hjelpelinjetypen på teigens teiggrenser.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
medallion: gold
```

# `code_arsaktilfeilrettingkode_v1`

Kodeliste for årsak til feilretting i Matrikkelen.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
medallion: gold
```

# `code_arsaktilforingkode_v1`

Årsaker til føring av bygningsstatus.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
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
medallion: gold
```

# `code_avlopskode_v1`

Avløpsordninger som bygg benytter.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
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
medallion: gold
```

# `code_bygningsendringskode_v1`

Hvordan en bygningsendring er bygget i forhold til hovedbygningen.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
medallion: gold
```

# `code_bygningsstatuskode_v1`

Gjeldende og historiske statuser for bygg, med ordnede lovlige årsaker til føring.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `lovlige_arsaker_til_foring_ids` | array<bigint> | Liste av lovlige årsaker for føring som bygningstatuskoden kan ha. Rekkefølgen er vesentlig. Om systemet skal velge skal første årsak benyttes. |

## Egenskaper

```yaml
medallion: gold
```

# `code_bygningstypekode_v1`

Hva en bygning er brukt til.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
medallion: gold
```

# `code_energikildekode_v1`

Energikilder som et bygg baserer seg på.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
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
medallion: gold
```

# `code_forretningsklassekode_v1`

Kodeliste for forretningsklasser i Matrikkelen.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `lovlige_forretningstype_ids` | array<bigint> |  |
| `utgatte_forretningstype_ids` | array<bigint> |  |
| `mulige_arsaker_til_feilretting_ids` | array<bigint> |  |
| `mulige_forretningsklasse_ids_for_grunnlag` | array<bigint> |  |

## Egenskaper

```yaml
medallion: gold
```

# `code_forretningstypekode_v1`

Grunnlaget for en endring av matrikkelinformasjon. Merknad: Hvis et punkt er oppdatert får hele grensa eller teigen punktets forretningstype (grensa/teigen er berørt av forretningen).

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
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
medallion: gold
```

# `code_grensemerkenedsattikode_v1`

Hva grensemerket er nedsatt i, for eksempel jord, fjell, mur, vann eller annen terrengdetalj.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `kodeverdi_sosi45` | string | SOSI 4.5-verdi for koden. |

## Egenskaper

```yaml
medallion: gold
```

# `code_grensepunkttypekode_v1`

Hvordan et grensepunkt er merket eller bestemt, for eksempel bolt, kors, rør, vegkant eller fastmerke.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `sosi_kode` | int | SOSI-kode for grensepunkttypen. |
| `kodeverdi_sosi45` | string | SOSI 4.5-verdi for koden. |

## Egenskaper

```yaml
medallion: gold
```

# `code_hjelpelinjetypekode_v1`

Typer hjelpelinjer som brukes når teiggrensen er ukjent eller ikke registrert, for eksempel vannkant, vegkant og punktfeste.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `sosi_kode` | string | SOSI-kode for hjelpelinjetypen. |
| `obj_type` | string | SOSI-objekttype for hjelpelinjen. |
| `kodeverdi_sosi45` | string | SOSI 4.5-verdi for koden. |

## Egenskaper

```yaml
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
medallion: gold
```

# `code_malemetodekode_v1`

Metoden som ligger til grunn for registrering av en posisjon. Se Geonorge SOSI-kodeliste.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `sosi_kode` | int | SOSI-kode for målemetoden. |

## Egenskaper

```yaml
medallion: gold
```

# `code_naringsgruppekode_v1`

Næringsgruppen som opptar størst andel av samlet areal i et bygg.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
medallion: gold
```

# `code_noyaktighetsklassekode_v1`

Klassifikasjon av stedfestingsnøyaktighet for teiggrensepunkt og grenser.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `sosi_navn` | string | SOSI-navn for nøyaktighetsklassen. |

## Egenskaper

```yaml
medallion: gold
```

# `code_opprinnelseskode_v1`

Hvordan et bygg opprinnelig ble registrert.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
medallion: gold
```

# `code_oppvarmingskode_v1`

Fyringssystem som utgjør hovedoppvarmingen i et bygg.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
medallion: gold
```

# `code_rolleiforretningkode_v1`

matrikkelenhetens rolle i forretning (f.eks om den er avgiver eller mottaker av areal, -eller bare er berørt)

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
medallion: gold
```

# `code_terrengdetaljkode_v1`

Terrengdetaljen som teiggrensen fulgte ved registrering, for eksempel elv, bygning, veg, vannskille eller steingjerde.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |
| `sosi_34` | string | SOSI 3.4-verdi for terrengdetaljen. |
| `kodeverdi_sosi45` | string | SOSI 4.5-verdi for koden. |

## Egenskaper

```yaml
medallion: gold
```

# `code_tinglysingsstatuskode_v1`

status i forhold til tinglysing av forretninger

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
medallion: gold
```

# `code_vannforsyningskode_v1`

Typer vannforsyning for bygg.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `kode_id` | bigint | Unik identifikator for kodeobjektet. |
| `kodeverdi` | string | Kildens kodeverdi. |
| `navn_bokmaal` | string | Navn på bokmål. |
| `navn_nynorsk` | string | Navn på nynorsk. |

## Egenskaper

```yaml
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
medallion: gold
scd: type-1
```

# `dim_bygning_v1`

Gjeldende bygninger i Matrikkelen. Én rad per bygning.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `bygg_id` | bigint | Id for Bygg. |
| `bygningsnummer` | bigint | En entydig identifikasjon av bygningen. Bygningsnumrene er unike på landsbasis, og tildeles automatisk. |
| `lopenummer` | int | Løpende nummerering av bygningsendringer til en bygning. Del av logisk ident som sammen med bygningsnr er unik på landsbasis. |
| `kommune_id` | bigint | Id til kommunen som bygningen ligger i. Bygningen må ha kommune. |
| `representasjonspunkt_x` | double | Representasjonspunkt for bygget. Skal plasseres innenfor bygingens omriss. Punkt registreres også uten at en har omrisset, men da settes ikke kvalitetsmerket for at den er verifisert mot bygningens omriss. |
| `representasjonspunkt_y` | double | Representasjonspunkt for bygget. Skal plasseres innenfor bygingens omriss. Punkt registreres også uten at en har omrisset, men da settes ikke kvalitetsmerket for at den er verifisert mot bygningens omriss. |
| `representasjonspunkt_z` | double | Representasjonspunkt for bygget. Skal plasseres innenfor bygingens omriss. Punkt registreres også uten at en har omrisset, men da settes ikke kvalitetsmerket for at den er verifisert mot bygningens omriss. |
| `representasjonspunkt_koordinatsystem_kode_id` | bigint | Koordinatsystem som posisjonen er oppgitt i. |
| `representasjonspunkt_original_koordinatsystem_kode_id` | bigint | Verdi for orginalt koordinatsystem. Dette blir kun satt dersom representasjonspunktet blir transformert ved henting! |
| `representasjonspunkt_stedfesting_verifisert` | boolean | Angir omrepresentasjonspunktet for adresse og bygning er stedfestingVerifisert. |
| `har_sefrakminne` | boolean | Flagg som angir om bygget er registrert i SEFRAK-registeret. SEFRAK inneholder bygninger bygd før 1900 eventuelt 1945 i deler av Nord-Norge. |
| `har_kulturminne` | boolean | Angir om bygget har registrert kulturminner fra Askeladden eller ikke. |
| `har_heis` | boolean | Flagg for å indikere om det er en heis i bygningen. |
| `skjermingsverdig` | boolean |  |
| `bebygd_areal` | double | Grunnflaten av bygget. Det vil si det arealet bygget tar av eiendommen det står på. Merknad: Bebygd arealer er påkrevd å registrere for bygninger under oppføring eller som er ferdigstilt etter 14.09.2010, men ikke for bygningsendringer. |
| `uten_bebygd_areal` | boolean | Flagg som angir at bygget faktisk ikke har bebygd areal. Når dette er satt er det korrekt at bebygd areal ikke er fyllt inn. Det er ikke mangelfull registrering. |
| `tidligere_bygg_id` | bigint | Id til evt tidligere bygg, dersom flyttet. |
| `oppvarmings_kode_ids` | array<bigint> | Kode for hvilket fyringssystem som utgjør hovedoppvarmingen.Flere kodeverdier kan angis, men bare dersom to fyringssystemer er likeverdige. |
| `energikilde_kode_ids` | array<bigint> | Hvilke energikilder bygget baserer seg på. |
| `bygningsstatus_kode_id` | bigint | Viser bygningens nåværende status. Merknad: I spesielle tilfeller kan et bygg få igangsettingstillatelse og ferdigattest for en del av bygget, og så igangsettingstillatelse for en annen del. |
| `avlops_kode_id` | bigint | Hvilken avløpsordning bygget benytter seg av. |
| `vannforsynings_kode_id` | bigint | Kode for type vannforsyning. Privat vannverk defineres som nett som forsyner mer enn 100 personer eller 20 husstander. |
| `naringsgruppe_kode_id` | bigint | Hvilken næringsgruppe som opptar størst andel av samlet areal i bygget. Unntak: Dersom bolig er kombinert med annen næring skal bygget ikke gis næringsgruppe bolig. |
| `opprinnelses_kode_id` | bigint | Angir hvordan bygget opprinnelig ble registrert. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |
| `bygningstype_kode_id` | bigint | Bygningstypen sier hva bygningen er brukt til. |
| `ufullstendig_areal` | boolean | Om arealopplysninger på bygget/bruksnheter/etasjer er fullstendig, dvs om bygget inneholder mer enn dets tilbygg. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `dim_bygningsendring_v1`

Gjeldende bygningsendringer i Matrikkelen. Én rad per bygningsendring.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `bygg_id` | bigint | Id for Bygg. |
| `bygningsnummer` | bigint | En entydig identifikasjon av bygningen. Bygningsnumrene er unike på landsbasis, og tildeles automatisk. |
| `lopenummer` | int | Løpende nummerering av bygningsendringer til en bygning. Del av logisk ident som sammen med bygningsnr er unik på landsbasis. |
| `kommune_id` | bigint | Id til kommunen som bygningen ligger i. Bygningen må ha kommune. |
| `representasjonspunkt_x` | double | Representasjonspunkt for bygget. Skal plasseres innenfor bygingens omriss. Punkt registreres også uten at en har omrisset, men da settes ikke kvalitetsmerket for at den er verifisert mot bygningens omriss. |
| `representasjonspunkt_y` | double | Representasjonspunkt for bygget. Skal plasseres innenfor bygingens omriss. Punkt registreres også uten at en har omrisset, men da settes ikke kvalitetsmerket for at den er verifisert mot bygningens omriss. |
| `representasjonspunkt_z` | double | Representasjonspunkt for bygget. Skal plasseres innenfor bygingens omriss. Punkt registreres også uten at en har omrisset, men da settes ikke kvalitetsmerket for at den er verifisert mot bygningens omriss. |
| `representasjonspunkt_koordinatsystem_kode_id` | bigint | Koordinatsystem som posisjonen er oppgitt i. |
| `representasjonspunkt_original_koordinatsystem_kode_id` | bigint | Verdi for orginalt koordinatsystem. Dette blir kun satt dersom representasjonspunktet blir transformert ved henting! |
| `representasjonspunkt_stedfesting_verifisert` | boolean | Angir omrepresentasjonspunktet for adresse og bygning er stedfestingVerifisert. |
| `har_sefrakminne` | boolean | Flagg som angir om bygget er registrert i SEFRAK-registeret. SEFRAK inneholder bygninger bygd før 1900 eventuelt 1945 i deler av Nord-Norge. |
| `har_kulturminne` | boolean | Angir om bygget har registrert kulturminner fra Askeladden eller ikke. |
| `har_heis` | boolean | Flagg for å indikere om det er en heis i bygningen. |
| `skjermingsverdig` | boolean |  |
| `bebygd_areal` | double | Grunnflaten av bygget. Det vil si det arealet bygget tar av eiendommen det står på. Merknad: Bebygd arealer er påkrevd å registrere for bygninger under oppføring eller som er ferdigstilt etter 14.09.2010, men ikke for bygningsendringer. |
| `uten_bebygd_areal` | boolean | Flagg som angir at bygget faktisk ikke har bebygd areal. Når dette er satt er det korrekt at bebygd areal ikke er fyllt inn. Det er ikke mangelfull registrering. |
| `tidligere_bygg_id` | bigint | Id til evt tidligere bygg, dersom flyttet. |
| `oppvarmings_kode_ids` | array<bigint> | Kode for hvilket fyringssystem som utgjør hovedoppvarmingen.Flere kodeverdier kan angis, men bare dersom to fyringssystemer er likeverdige. |
| `energikilde_kode_ids` | array<bigint> | Hvilke energikilder bygget baserer seg på. |
| `bygningsstatus_kode_id` | bigint | Viser bygningens nåværende status. Merknad: I spesielle tilfeller kan et bygg få igangsettingstillatelse og ferdigattest for en del av bygget, og så igangsettingstillatelse for en annen del. |
| `avlops_kode_id` | bigint | Hvilken avløpsordning bygget benytter seg av. |
| `vannforsynings_kode_id` | bigint | Kode for type vannforsyning. Privat vannverk defineres som nett som forsyner mer enn 100 personer eller 20 husstander. |
| `naringsgruppe_kode_id` | bigint | Hvilken næringsgruppe som opptar størst andel av samlet areal i bygget. Unntak: Dersom bolig er kombinert med annen næring skal bygget ikke gis næringsgruppe bolig. |
| `opprinnelses_kode_id` | bigint | Angir hvordan bygget opprinnelig ble registrert. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |
| `hovedbygg_id` | bigint | Bygningsendringens tilhørende bygning, kan ikke være null. |
| `bygningsendrings_kode_id` | bigint | Hvordan bygningsendringen er bygget i forhold til bygningen. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `dim_etasje_v1`

Gjeldende etasjer for bygg. Én rad per bygg og etasje.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `bygg_id` | bigint | Id for Bygg. |
| `byggobjekttype` | string | Type matrikkelobjekt som bygg_id viser til. Verdier: bygning og bygningsendring. |
| `etasje_id` | bigint | Etasjens faktiske id. |
| `etasjeplan_kode_id` | bigint | Hvilket plan etasje ligger i, f.eks. om det er en underetasje eller loftsetasje. Er en av gitte, lovlige typer. |
| `etasjenummer` | int | Fortløpende nummerering av etasjer som har samme type. Kjeller- og underetasjer nummereres fra terrengnivå og nedover, dvs. har nummer 1 øverst. Hoved- og loftsetasjer nummereres fra terrengnivå og oppover, dvs. har nummer 1 nederst. |
| `antall_boenheter` | int | Antall boenheter i etasjen. Beregnes automatisk av systemet etter bruksenheter av type bolig på etasjen. En bruksenhet regnes bare med i den etasjen den har sin inngang. |
| `bruksareal_til_bolig` | double | Etasjens samlede brukareal til boligformål. |
| `bruksareal_til_annet` | double | Bruksareal til annet enn bolig i henhold til NS 3940 med diverse unntak. |
| `bruksareal_totalt` | double | Totalt bruksareal er sum av bruksareal til bolig og bruksareal til annet. |
| `alternativt_areal` | double | Alternativt areal i etasjen. Kommunene bestemmer hva de vil legge i feltet, f.eks. leieareal. |
| `alternativt_areal_2` | double | Feltet er til fri disposisjon for kommunene. |
| `bruttoareal_til_bolig` | double | Bruttoareal for bolig. |
| `bruttoareal_til_annet` | double | Bruttoareal for annet enn bolig. |
| `bruttoareal_totalt` | double | Bruttoareal totalt. |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
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
medallion: gold
scd: type-1
```

# `dim_teig_v1`

Teiger i matrikkelen — nåtidsbilde med én rad per teig.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `teig_id` | bigint | Id for en teig. |
| `datafangstdato` | date | Datafangstdato. |
| `lagret_beregnet_areal` | double | Beregnet areal i kartplan, det vil si areal av teig som er avgrenset av teiggrenser og/eller hjelpelinjer. Hvis noen av teiggrensene til teigen er hjelpelinjer eller teigen er omtvistet (merket på teig eller teiggrense) skal teigarealmerknad alltid oppgis sammen med teigarealet. Merknad 1: For teiger tilhørende punktfester angis ikke teigareal, kun arealmerknad på teig. Teiger som inneholder punktfester (øyer avgrenset av hjelpelinje punktfeste), får ikke fratrekk for disse ved beregning av teigareal. Merknad 2: Det oppgis ikke kvalitet/nøyaktighet på det beregnede arealet. Informasjon om kvalitet kan avledes fra arealmerknad(er) på teig og fra antatt stedfestingsnøyaktighet på teiggrensepunkt eller teiggrenser. |
| `avklart_eiere` | boolean | Angir om det er avklart hvilke matrikkelenheter som har andel i det uregistrerte jordsameiet. Merknad: Denne kan bare være Ja/True hvis UregistrertJordsameie er Ja/true. |
| `teig_med_flere_matrikkelenheter` | boolean | Teig som er knyttet til flere matrikkelenheter, men hvor de interne grensene mellom matrikkelenhetene er ukjente (i hvert fall ikke registrert i matrikkelen). |
| `tvist` | boolean | Om det er tvil/tvist om eiendomsretten til teigen. Merknad: Kan også være brukt når teigen har omtvistede grenser eller grenser det er tvil om forløpet til, men der skal grensene være merket med 'omtvistet'. |
| `uregistrert_jordsameie` | boolean | Angir om teigen inngår i brukssameie mellom matrikkelenheter, hvor jordsameiet ikke har eget matrikkelnummer (dvs. ikke matrikkelenheten 'Jordsameie'). |
| `representasjonspunkt_x` | double | Punkt som representerer teigen. Punktet må ligge innenfor teigens avgrensing. Representasjonspunktet til en teig er vanligvis plassert i tyngdepunktet til flata. Posisjonen er oppgitt i nord- og østkoordinater. Kan også inneholde høyde på representasjonspunkt for adresse. For andre representasjonspunkt brukes ikke høyden. Må være gitt. |
| `representasjonspunkt_y` | double | Punkt som representerer teigen. Punktet må ligge innenfor teigens avgrensing. Representasjonspunktet til en teig er vanligvis plassert i tyngdepunktet til flata. Posisjonen er oppgitt i nord- og østkoordinater. Kan også inneholde høyde på representasjonspunkt for adresse. For andre representasjonspunkt brukes ikke høyden. Må være gitt. |
| `representasjonspunkt_z` | double | Punkt som representerer teigen. Punktet må ligge innenfor teigens avgrensing. Representasjonspunktet til en teig er vanligvis plassert i tyngdepunktet til flata. Posisjonen er oppgitt i nord- og østkoordinater. Kan også inneholde høyde på representasjonspunkt for adresse. For andre representasjonspunkt brukes ikke høyden. Må være gitt. |
| `representasjonspunkt_koordinatsystem_kode_id` | bigint | Koordinatsystem som posisjonen er oppgitt i. Må være gitt. |
| `representasjonspunkt_original_koordinatsystem_kode_id` | bigint | Verdi for orginalt koordinatsystem. Dette blir kun satt dersom representasjonspunktet blir transformert ved henting! |
| `representasjonspunkt_malemetode_id` | bigint | Beskrivelse av kvaliteten på representasjonspunktet. Kun aktuelt for punktfeste. Metode for måling av geometrien i grunnriss. |
| `representasjonspunkt_noyaktighet` | int | Beskrivelse av kvaliteten på representasjonspunktet. Kun aktuelt for punktfeste. Punktstandardavviket i grunnriss for punkter samt tverravvik for linjer. Oppgitt i cm. |
| `representasjonspunkt_stedfesting_verifisert` | boolean | Angir omrepresentasjonspunktet for adresse og bygning er stedfestingVerifisert. |
| `teigarealmerknad_ids` | array<bigint> |  |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `dim_teiggrense_v1`

Teiggrenser i matrikkelen — nåtidsbilde med én rad per teiggrense.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `teiggrense_id` | bigint | Id for en teiggrense. |
| `datafangstdato` | date | Dato for datainnsamling. |
| `omtvistet` | boolean | Angir om grensen er omtvistet, eller det er tvil om forløpet. |
| `administrativ_grense_kode_id` | bigint | Angir om teiggrensen samtidig representerer en administrativ grense. Standardverdi er AdministrativGrenseKode.IKKEADMGRENSE. Må være gitt. |
| `folger_terrengdetalj_id` | bigint | Angir hvilken terrengdetalj matrikkelenhetsgrensen/eiendomsgrensen eventuelt følger. Merknad: Egenskapen forteller hvilken terrengdetalj grenselinja fulgte på registreringstidspunktet. En må være oppmerksom på at dette kan ha endret seg. F.eks kan en strandlinje bli fylt ut, en elv kan få et nytt forløp eller en veg kan skifte trasé. Derfor må en vurdere nøye når en oppdaterer terrengdetaljer med bedre geometri etter f.eks en nykartlegging. |
| `hjelpelinjetype_id` | bigint | Avgrensing for teig som brukes når matrikkelenhetsgrense/eiendomsgrense ikke er kjent eller ikke er registrert i matrikkelen. Brukes i følgende tilfeller: - punktfeste - generert eiendomsgrense - avgrensing mellom to teiger hvor grenseforløp ikke er kjent - avgrensing mot innsjø, vassdrag eller sjø hvor grensene ikke er registrert i Matrikkelen - avgrensing mot fjellområder hvor grensene ikke er registrert i Matrikkelen For bruk mot vann: Brukes bare når de virkelige teiggrenser i eller langs vannet ikke er tilgjengelig eller er vanskelig tilgjengelig. En bør benytte den best kartlagte avgrensingen, fordi teigene ofte presenteres sammen med det beste kartgrunnlaget. |
| `kurve_koordinatsystem_kode_id` | bigint | Aktuelt koordinatsystem for koordinatene til denne grenselinjen. |
| `kurve_original_koordinatsystem_kode_id` | bigint | Verdi for orginalt koordinatsystem. Dette blir kun satt dersom representasjonspunktet blir transformert ved henting! |
| `kurvepunkter` | array<struct<x:double,<br>y:double,<br>z:double>> | Kurve, en kontinuerlig krum linje der det enkelte punktet i sekvensen ikke har noen spesiell betydning. Benyttes for å beskrive avgrensninger når disse følger naturlige terrengdetaljer. |
| `buepunkt_x` | double | Bue, sirkelbuen mellom to punkt. |
| `buepunkt_y` | double | Bue, sirkelbuen mellom to punkt. |
| `buepunkt_z` | double | Bue, sirkelbuen mellom to punkt. |
| `noyaktighet` | int | Brukes der teiggrensen har dårligere kvalitet enn dårligste teiggrensepunkt, og der den er kurvatur. Punktstandardavviket i grunnriss for punkter samt tverravvik for linjer. Oppgitt i cm. |
| `malemetode_id` | bigint | Brukes der teiggrensen har dårligere kvalitet enn dårligste teiggrensepunkt, og der den er kurvatur. Metode for måling av geometrien i grunnriss. |
| `lagret_noyaktighetsklasse_id` | bigint | Klassifikasjon av stedfestingsnøyaktighet på grenser basert på dårligste registrerte nøyaktighet til grensepunktene (endepunktene). Unntaksvis er klassifikasjonen basert på nøyaktighet registrert på selve grensen. Verdier: MaleNoyaktighetEuref = nøyaktige målinger med S <= 10 cm; MaleNoyaktighetNGO = middels nøyaktige eller gamle transformerte målinger med 10 < S <= 30 cm; TekniskKartNoyaktighet = mindre nøyaktige målinger og grenser fra tekniske kart med 30 < S < 200 cm; OkonomiskKartNoyaktighet = mindre nøyaktige grenser og grenser fra Økonomisk kartverk med 200 <= S < 500 cm; SkisseNoyaktighet = skisserte data med S >= 500 cm og målemetode 80, 81 eller 82, eller uten angitt målemetode; Norge1_50000 = lite nøyaktige grenser med S >= 500 cm og annen målemetode; IngenNoyaktighet = data uten registrert nøyaktighet. S er antatt standardavvik. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `dim_teiggrensepunkt_v1`

Teiggrensepunkter i matrikkelen — nåtidsbilde med én rad per teiggrensepunkt.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `teiggrensepunkt_id` | bigint | Id for et teiggrensepunkt. |
| `datafangstdato` | date | Dato når datainnsamling er skjedd.  Vil for eksempel være fotograferingsdato for data innsamlet via fotogrammetri, og måledato for data innsamlet i forbindelse med oppmålingsforretninger. |
| `posisjon_x` | double | Grensepunktets posisjon. Må være gitt. |
| `posisjon_y` | double | Grensepunktets posisjon. Må være gitt. |
| `posisjon_z` | double | Grensepunktets posisjon. Må være gitt. |
| `koordinatsystem_kode_id` | bigint | Angir koordinatsystemet som teiggrensepunktets koordinater er lagret i. Må være gitt. |
| `original_koordinatsystem_kode_id` | bigint | Verdi for orginalt koordinatsystem. Dette blir kun satt dersom representasjonspunktet blir transformert ved henting! |
| `grensemerke_nedsatt_i_id` | bigint | Beskriver i hvilket medium grensemerket er nedsatt. |
| `grensepunkttype_id` | bigint | Angir hva slags grensemerke som er brukt i terrenget. Sier også om grensepunktet er merket i terrenget, eller om det bare er et registreringsteknisk punkt. |
| `noyaktighet` | int | Målemetode og nøyaktighet for teiggrensepunktet. Punktstandardavviket i grunnriss for punkter samt tverravvik for linjer. Oppgitt i cm. |
| `malemetode_id` | bigint | Målemetode og nøyaktighet for teiggrensepunktet. |
| `uuid` | string | Type-5 uuid generert med SHA-1 fra navnerom og matrikkel-ID-verdi for objektet den hører til |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
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
medallion: gold
scd: type-1
```

# `fact_areal_i_forretning_v1`

Komponent brukt i forretning for å koble matrikkelenhet mot forretning og for å kunne angi matrikkelenhetens arealendring og rolle i forretningen. Nåtidsbilde med én rad per ArealIForretning-komponent.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `areal_i_forretning_id` | bigint | Persistent ID for ArealIForretning-komponenten. |
| `forretning_id` | bigint | ID til foreldreforretningen komponenten ble pakket ut fra. |
| `forretningstype_kode_id` | bigint | Forretningstypen kopiert fra foreldreforretningen. Slås opp i `code_forretningstypekode_v1`. |
| `forretningsdokumentdato` | date | Dato da foreldreforretningen ble avholdt. Kan være NULL for eldre data. |
| `matrikkelforingsdato` | date | Dato da foreldreforretningen ble ført i Matrikkelen. Kan være NULL for konverterte data. |
| `matrikkelenhet_id` | bigint | ID til matrikkelenheten som får eller avgir areal, eller er knyttet til forretningen på annen måte. |
| `lopenummer` | int | Lokalt løpenummer som knytter sammen avgiver og mottaker når forretningen har flere av dem. Dette er ikke forretningens globale `lopenummer`. |
| `rolle_id` | bigint | Matrikkelenhetens rolle i forretningen, for eksempel avgiver, mottaker, berørt eller jordskiftepart. Slås opp i `code_rolleiforretningkode_v1`. |
| `arealendring` | double | Endring i kartplanareal for matrikkelenheten; positiv verdi er tillegg og negativ verdi er fradrag. |
| `omnummerert_fra` | struct<metadata:array<string>,<br>kommune_id:bigint,<br>gardsnummer:int,<br>bruksnummer:int,<br>festenummer:int,<br>seksjonsnummer:int> | Matrikkelnummeret enheten hadde før omnummerering. |
| `omnummerert_til` | struct<metadata:array<string>,<br>kommune_id:bigint,<br>gardsnummer:int,<br>bruksnummer:int,<br>festenummer:int,<br>seksjonsnummer:int> | Matrikkelnummeret enheten fikk etter omnummerering. |
| `volumendring` | double | Endring i oppgitt volum for berørt anleggsprojeksjonsflate. Feltet ble innført i Matrikkel-API 3.16. |
| `uuid` | string | Deterministisk type-5-UUID generert fra Matrikkelens navnerom samt objektets klasse og ID. |
| `oppdateringsdato` | timestamp | Tidspunkt da kildeversjonen ble oppdatert i Matrikkelen. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `fact_bygning_statushistorikk_v1`

Bygningsstatushistorikk for gjeldende bygninger. Én rad per bygning og statusregistrering.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `bygg_id` | bigint | Bygget statusforløpet gjelder. |
| `bygningsstatushistorikk_id` | bigint | Intern nøkkel for forekomsten. Må være gitt. |
| `bygningsstatus_kode_id` | bigint | Hvilken status, f.eks. at ferdigattest er gitt. Er en av gitte, lovlige statuser. Må være gitt. |
| `arsak_til_foring_kode_id` | bigint |  |
| `referanse` | string |  |
| `dato` | date | Datoen hvor bygningen nådde statusen. Kan mangle. |
| `registrert_dato` | timestamp | Registrert dato legges automatisk på ved innlegging i matrikkelen. Kan mangle på gamle data. |
| `slettet_dato` | timestamp |  |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `fact_bygningsendring_statushistorikk_v1`

Bygningsstatushistorikk for gjeldende bygningsendringer. Én rad per bygningsendring og statusregistrering.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `bygg_id` | bigint | Bygget statusforløpet gjelder. |
| `bygningsstatushistorikk_id` | bigint | Intern nøkkel for forekomsten. Må være gitt. |
| `bygningsstatus_kode_id` | bigint | Hvilken status, f.eks. at ferdigattest er gitt. Er en av gitte, lovlige statuser. Må være gitt. |
| `arsak_til_foring_kode_id` | bigint |  |
| `referanse` | string |  |
| `dato` | date | Datoen hvor bygningen nådde statusen. Kan mangle. |
| `registrert_dato` | timestamp | Registrert dato legges automatisk på ved innlegging i matrikkelen. Kan mangle på gamle data. |
| `slettet_dato` | timestamp |  |
| `oppdateringsdato` | timestamp | Viser når boblen sist ble endret. Feltet er alltid satt dersom boblen har det. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```

# `fact_forretning_v1`

Forretning dokumenterer ting som har skjedd med Matrikkelenheten opp gjennom tiden. Forretning dokumenterer også ting som har skjedd med nabo-enhet såfremt de har et felles punkt som inngår i forretningen. Nåtidsbilde med én rad per forretning.

## Kolonner

| Kolonne | Datatype | Kommentar |
| --- | --- | --- |
| `forretning_id` | bigint | Matrikkelens tekniske objekt-ID for forretningen. Det logiske løpenummeret ligger i `lopenummer`. |
| `forretningstype_kode_id` | bigint | Juridisk eller historisk grunnlag for en endring av matrikkelinformasjon. Lovlige og utgåtte typer avhenger av forretningsklassen. Hvis et punkt oppdateres får hele grensa eller teigen punktets forretningstype. Slås opp i `code_forretningstypekode_v1`. |
| `lopenummer` | bigint | Entydig logisk identifikator for forretningen i endringsloggen. Konvertert fra GAB og videreført i Matrikkelen. |
| `forretningsdokumentdato` | date | Dato da forretningen ble avholdt. Påkrevd for nye forretninger, kan ikke ligge i fremtiden og kan være NULL for eldre data. |
| `matrikkelforingsdato` | date | Dato for føringen av forretningen i Matrikkelen. Settes automatisk til dagens dato for nye forretninger og kan være NULL for konverterte data. |
| `kommunal_saksreferanse` | string | Forretningens referanse til kommunalt arkiv. Kalt protokoll-, journal- eller målebrevsnummer i GAB. Kan være maksimalt 30 tegn. |
| `annen_referanse` | string | Annen referanse enn kommunalt arkiv, blant annet eldre protokoll-, journal- eller målebrevsnummer. For jordskifte og tilkobling til jordskiftesak er feltet påkrevd og inneholder jordskifterettens saksnummer. Kan være maksimalt 30 tegn. |
| `signatur` | string | Signatur til brukeren som opprettet forretningen. Settes automatisk for Matrikkel-data, men kan mangle i GAB-data. |
| `forretningsklasse_kode_id` | bigint | Konkret domeneklasse eller brukstilfelle for forretningen. Feltet avgjør hvilke klassespesifikke kolonner som er relevante og slås opp i `code_forretningsklassekode_v1`. Gis ut av Matrikkel-API-et fra klientversjon 3.17. |
| `uuid` | string | Deterministisk type-5-UUID generert fra Matrikkelens navnerom samt objektets klasse og ID. |
| `kommunal_saksreferanse_url` | string | Lenke eller nettadresse til forretningens sak i kommunalt arkiv. Feltet ble innført i Matrikkel-API 4.1. |
| `landmalernummer` | string | Landmålernummer slik det er registrert i autorisert landmålerregister (AAL). Feltet ble innført i Matrikkel-API 4.1. |
| `landmalernavn` | string | Navn på registrert landmåler. Fra 1. januar 2027 er landmåler betinget påkrevd for relevante forretningstyper med geometriendringer. Feltet ble innført i Matrikkel-API 4.1. |
| `arsak_til_feilretting_kode_id` | bigint | Årsak til feilretting. Skal være `IkkeOppgitt` for andre forretningstyper og en lovlig konkret årsak ved feilretting. Slås opp i `code_arsaktilfeilrettingkode_v1`. |
| `tinglysingsstatus_kode_id` | bigint | Status i forhold til tinglysing. Bare forretninger som kan sendes til tinglysing kan ha annen verdi enn `IkkeOppgitt`. Slås opp i `code_tinglysingsstatuskode_v1`. |
| `tinglysingsstatus_endret_dato` | date | Dato for når forretningens tinglysingsstatus er endret sist. Settes til dagens dato av systemet når tinglysingsstatus endres og hver gang rapporten "Melding til tinglysing" genereres. Kun forretninger som kan sendes til tinglysing får en dato satt. |
| `melding_til_tinglysings_id` | string | Unik meldings-ID i innsendings-API-et for elektronisk tinglysing. Bare satt ved elektronisk innsending; papirinnsending gir NULL. En ny innsending får ny ID. |
| `teig_ids` | array<bigint> | ID-er til teiger knyttet til en geometri-forretning. |
| `teiggrense_ids` | array<bigint> | ID-er til teiggrenser knyttet til en geometri-forretning. |
| `teiggrensepunkt_ids` | array<bigint> | ID-er til teiggrensepunkter knyttet til en geometri-forretning. |
| `anleggsprojeksjonsflate_ids` | array<bigint> | ID-er til anleggsprojeksjonsflater knyttet til en geometri-forretning. |
| `anleggsprojeksjonsgrense_ids` | array<bigint> | ID-er til anleggsprojeksjonsgrenser knyttet til en geometri-forretning. |
| `anleggsprojeksjonspunkt_ids` | array<bigint> | ID-er til anleggsprojeksjonspunkter knyttet til en geometri-forretning. |
| `unntak_etter_ml9f` | boolean | Om arealoverføringen omfattes av unntaket i matrikkelloven § 9 første ledd bokstav f: overføring fra uregistrert jordsameie eller fra et område med flere bruksnumre og ukjente grenser. |
| `forretning_som_grunnlag_id` | bigint | ID til en forretning brukt som grunnlag for blant annet fullføring, feilretting eller reversering av omnummerering. |
| `eksisterende_matrikkelenhet_id` | bigint | ID til matrikkelenheten som en forretning over eksisterende matrikkelenhet føres over. Kan mangle i data før versjon 2.2 og i konverterte data. |
| `matrikkelenhet_for_omnummerering_id` | bigint | ID til matrikkelenheten som får nytt matrikkelnummer. Omnummereringen beholder matrikkelenhetens objekt-ID. |
| `tinglyst_dokument_ident` | struct<embete:int,<br>dokument_ar:int,<br>dokument_nummer:int,<br>dokument_rnummer:int> | Ident til tinglyst dokument for en sammenslåing. Brukes til å finne igjen sammenslåingen ved feilretting eller endring. |
| `sammensla_reseksjoneringer` | array<struct<metadata:array<string>,<br>sammensla_reseksjonering_id:bigint,<br>seksjon_id:bigint,<br>matrikkelnummer:struct<metadata:array<string>,<br>kommune_id:bigint,<br>gardsnummer:int,<br>bruksnummer:int,<br>festenummer:int,<br>seksjonsnummer:int>,<br>sameiebrok:struct<teller:bigint,<br>nevner:bigint>,<br>formal_seksjon_kode_id:bigint,<br>versjon_id:bigint,<br>oppdateringsdato:timestamp,<br>sluttdato:timestamp>> | Midlertidige reseksjoneringsdata for sammenslåing med seksjonerte, tinglyste matrikkelenheter. Brukes når sammenslåingen fullføres etter svar fra tinglysingen. |
| `sammensla_ommatrikulering_festegrunner` | array<struct<metadata:array<string>,<br>sammensla_ommatrikulering_festegrunn_id:bigint,<br>festegrunn_id:bigint,<br>matrikkelnummer:struct<metadata:array<string>,<br>kommune_id:bigint,<br>gardsnummer:int,<br>bruksnummer:int,<br>festenummer:int,<br>seksjonsnummer:int>,<br>versjon_id:bigint,<br>oppdateringsdato:timestamp,<br>sluttdato:timestamp>> | Midlertidige data for ommatrikulering av underliggende festegrunner ved sammenslåing. Omfatter også bestående festegrunner som ikke bytter matrikkelnummer. |
| `forretninger_i_forretning_ids` | array<bigint> | ID-er til forretninger som opprettes, endres eller slettes gjennom en rettings- eller endringsforretning. Relevant for forretningsklasse 45 og 53. |
| `jordskifte_krevd_id` | bigint | ID til det registrerte kravet om jordskiftesak som en `JordskifteForretning` fører. Jordskifterettens saksreferanse ligger i `annen_referanse`. |
| `oppdateringsdato` | timestamp | Tidspunkt da kildeversjonen ble oppdatert i Matrikkelen. Brukes som sekvensfelt for Silver-SCD2. |

## Egenskaper

```yaml
medallion: gold
scd: type-1
```
