# Izveštaj o analizi projekta: Rich

**Autor**: Jovan Ranđelović  1088/2023
**Kurs**: Verifikacija Softvera  

---

## 1. Uvod

### 1.1 Kontekst i motivacija

Rich je Python biblioteka za **renderovanje lepog terminal output-a**: boje, tabele, progress bar-ove, JSON, Markdown, logovanje i drugo.  

Razvoj robustnih CLI alata i vizuelno bogatih terminal aplikacija zahteva biblioteku koja apstrahuje složenost renderovanja i stilizovanja teksta. Rich se koristi u širokom spektru projekata – od development alata do monitoring skripti.

### 1.2 Ciljevi analize

Ovaj seminarski rad ima za cilj analizu kvaliteta Rich biblioteke kroz:

- Pokrivenost koda testovima
- Validaciju funkcionalnosti preko unit testova
- Analizu održivosti i kompleksnosti
- Proveru type safety i bezbednosti

**Primarne metrike**:

- Korektnost implementacije (unit testovi)
- Pokrivenost koda testovima
- Održavanje koda i kompleksnost

---

## 2. Korišćeni alati

### 2.1 Pytest – Jedinični testovi
**Opis**: Framework za pisanje i pokretanje jediničnih testova u Python-u.

**Korišćenje**: Napisano X novih unit testova koji pokrivaju:

**test_iter_syntax_lines_multiline.py** (1 test)
Cilj: Testiranje funkcije `_iter_syntax_lines` za slučaj kada greška obuhvata više linija koda.
Pokriveni scenariji:
- `test_iter_syntax_lines_multiline` - Provera ispravnog označavanja opsega greške kroz više linija (prva, srednja i poslednja linija)

