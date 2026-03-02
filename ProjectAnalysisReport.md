# Analiza projekta Rich

## 1. Uvod


## 2. Cilj analize


## 3. Testiranje i pokrivenost koda
Analiza pokrivenosti testovima

Pokrivenost koda testovima analizirana je korišćenjem alata pytest i pytest-cov nad projektom Rich. Pokretanjem testova izvršeno je ukupno 978 testova, od čega je 953 uspešno prošlo, dok je 25 testova preskočeno.

Ukupna pokrivenost koda iznosi približno 95%, što ukazuje na to da projekat već poseduje razvijen skup automatskih testova.

Analiza izveštaja o pokrivenosti pokazuje da pojedini moduli imaju manju pokrivenost, kao što su json.py, jupyter.py i repr.py. Ovi moduli predstavljaju potencijalne kandidate za dodatno testiranje.

Takođe je uočeno da moduli koji implementiraju funkcionalnosti specifične za Windows operativni sistem imaju veoma malu pokrivenost testovima, što je očekivano jer je analiza projekta izvršena u Linux okruženju.

**Primer dodatnog testa:**

- **Testiranje progress.py**  
  Napisan je jednostavan unit test koji proverava procentualnu završetak task-a (50% i 100%).  
  Test se uspešno izvršava pomoću pytest i coverage alata, i pokriva osnovne linije funkcionalnosti modula `progress.py`.

## 4. Alati korišćeni za analizu
- pytest + coverage
  

## 5. Zaključci

