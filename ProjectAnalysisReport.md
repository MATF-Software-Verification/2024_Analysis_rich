# Analiza projekta Rich

## 1. Uvod


## 2. Cilj analize


## 3. Testiranje i pokrivenost koda
Ukupna pokrivenost koda iznosi 95%, pri čemu su moduli `_win32_console.py` i `_windows_renderer.py` platform-specific i nisu pokriveni na Linux okruženju. Većina ključnih funkcionalnosti ima pokrivenost preko 98%.

Dodatno:
- Najslabije pokriveni moduli: `traceback.py`, `progress.py`, `live.py`, `pretty.py`
- Plan za dopunu testova: napisati 2–3 unit testa i 1 integration test

## 4. Alati korišćeni za analizu
- pytest + coverage
  

## 5. Zaključci

