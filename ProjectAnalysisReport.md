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

**Korišćenje**: Napisano 9 novih unit testova koji pokrivaju modul `traceback.py`:

**test_iter_syntax_lines_multiline.py** (1 test)
Cilj: Testiranje funkcije `_iter_syntax_lines` za slučaj kada greška obuhvata više linija koda.
Pokriveni scenariji:
- `test_iter_syntax_lines_multiline` - Provera ispravnog označavanja opsega greške kroz više linija (prva, srednja i poslednja linija)

**test_exception_group_traceback.py** (1 test)
Cilj: Testiranje ekstrakcije traceback-a za `ExceptionGroup` (Python 3.11+).
Pokriveni scenariji:
- `test_exception_group_traceback` - Provera ispravnog rukovanja sa više exception-a bačenih odjednom kroz `ExceptionGroup`

**test_safe_str_with_broken_str.py** (1 test)
Cilj: Testiranje otpornosti `safe_str` funkcije kada `__str__` metoda objekta baca exception.
Pokriveni scenariji:
- `test_safe_str_with_broken_str` - Provera da `Traceback.extract` ne pada kada exception objekat ima pokvarenu `__str__` metodu

**test_stack_defaults.py** (1 test)
Cilj: Testiranje ispravnih default vrednosti `Stack` dataclass-a.
Pokriveni scenariji:
- `test_stack_defaults` - Provera da se `Stack` kreira sa ispravnim default vrednostima (`is_group=False`, `frames=[]`, `exceptions=[]`)

**test_frame_creation.py** (1 test)
Cilj: Testiranje ispravnog kreiranja `Frame` dataclass-a.
Pokriveni scenariji:
- `test_frame_creation` - Provera da se `Frame` kreira sa ispravnim default vrednostima (`locals=None`, `last_instruction=None`)

**test_from_exception.py** (1 test)
Cilj: Testiranje alternativnog načina kreiranja `Traceback` objekta.
Pokriveni scenariji:
- `test_from_exception` - Provera da `Traceback.from_exception()` ispravno kreira objekat iz exception informacija

**test_get_locals.py** (1 test)
Cilj: Testiranje filtriranja lokalnih promenljivih u traceback-u.
Pokriveni scenariji:
- `test_get_locals_hide_dunder` - Provera da se promenljive sa `__` prefiksom preskačaju kada je `locals_hide_dunder=True`

**test_get_locals_show_all.py** (1 test)
Cilj: Testiranje prikaza svih lokalnih promenljivih bez filtriranja.
Pokriveni scenariji:
- `test_get_locals_show_all` - Provera da se sve promenljive prikazuju kada su `locals_hide_dunder=False` i `locals_hide_sunder=False`

**test_get_locals_hide_sunder.py** (1 test)
Cilj: Testiranje filtriranja promenljivih sa `_` prefiksom.
Pokriveni scenariji:
- `test_get_locals_hide_sunder` - Provera da se promenljive sa `_` prefiksom preskačaju kada je `locals_hide_sunder=True`


