# Dokumentasjon for dekryptering av krypterte datasett

Dette scriptet kan benyttes dersom ett eller flere av datasettene deres inneholder krypterte felter.  

## Forutsetninger

- Du har en **privat nøkkel** (`consumer_private_key.pem`) tilgjengelig.
- Du har din delta_share_ref, f.eks. `abcd`
- Du har fått lastet ned:
  - Et **kryptert datasett**, f.eks. `dim_kulturminner_encrypted.csv`
  - Et tilhørende **sett med krypterte nøkler**, `keys_encrypted_{delta_share_ref}.csv`

---

## Oppsett

1. **Plassering av privat nøkkel**  
   Legg privatnøkkelen i:  

   ```
   crypto/consumer_private_key.pem
   ```

   Se eksempler på hvordan nøkler kan genereres i [kartverket/kv-dataplattform-consumer](https://github.com/kartverket/kv-dataplattform-consumer/blob/main/python/README.md#generer-en-egen-n%C3%B8kkel).

2. **Krypterte datafiler**  
   Sørg for at du har:
   - `dim_kulturminner_encrypted.csv` (eller tilsvarende datasett)
   - `keys_encrypted_{delta_share_ref}.csv` (nøklene dine, hvor `{delta_share_ref}` er id’en fra din deltashare)

3. **Angi `delta_share_ref` i scriptet**  
   I toppen av `crypto/decrypt.py`, sett `delta_share_ref` til den samme id’en som brukes i nøkkelfilen din.  

   Eksempel:  
   ```python
   delta_share_ref = "abcd"
   ```

   Da forventes det at du har en fil som heter:
   ```
   keys_encrypted_abcd.csv
   ```

---

## Kjøring

Fra rotmappen kjører du:

```bash
python crypto/decrypt.py
```

Scriptet vil da:

1. Lese privatnøkkelen
2. Dekryptere de symmetriske nøklene
3. Bruke disse til å dekryptere feltene i datasettet
4. Skrive resultatet til en ny fil:

```
decrypted_{delta_share_ref}_data.csv
```

---

## Output

- **`decrypted_{delta_share_ref}_data.csv`**: Dekryptert datassett.  
- Feltene `kulturminneId`, `keyId`, `versjon`, `versjonId`, `from_datetime`, `to_datetime` og `symmetric_key` blir ikke dekryptert, da de ikke er krypterte datafelter.

---

## Feil og feilsøking

- Dersom dekryptering av et felt feiler, logges det til konsollen med informasjon om feilen og en kort forhåndsvisning av feltets innhold.
- Dersom en nøkkel ikke kan dekrypteres, vil den bli satt til `None`, og tilhørende rader vil ikke bli dekryptert.
- Dette kan skje hvis nøkkelformatet ikke blir parset riktig for eksempel. Da vil man typisk få feilmelding sånn som: `Failed to decrypt key_id <ID>: <feil>` med informasjon om hvordan formatet er feil. 
