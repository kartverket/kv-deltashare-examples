# Tabelldokumentasjon

_Generert 2026-09-23T07:57:06+00:00_

## Tabeller

- `dim_fylke_v1`
- `dim_kommune_v1`
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
