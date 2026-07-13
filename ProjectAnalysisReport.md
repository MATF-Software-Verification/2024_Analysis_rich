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

### 2.1 Pytest - Jedinični testovi

**Opis:** Framework za pisanje i pokretanje jediničnih testova u Python-u.

**Korišćenje:** Napisano 25 novih unit testova koji pokrivaju:

#### traceback.py (9 testova)

**Cilj:** Testiranje `rich.traceback` modula — konstrukcija traceback objekata, filtriranje lokalnih promenljivih i interne helper funkcije

**Pokriveni scenariji:**

* `test_frame_creation` - kreiranje `Frame`-a i verifikacija default vrednosti (`line=""`, `locals=None`, `last_instruction=None`)
* `test_stack_defaults` - default vrednosti `Stack`-a (`is_group=False`, prazne liste, `syntax_error=None`)
* `test_from_exception` - kreiranje traceback-a preko `Traceback.from_exception()` iz uhvaćenog izuzetka
* `test_exception_group_traceback` - rukovanje `ExceptionGroup`-om (Python 3.11+, sa `pytest.skip` na starijim verzijama)
* `test_safe_str_with_broken_str` - robustnost kada objekat ima `__str__` koji baca `RuntimeError`
* `test_get_locals_hide_dunder` - filtriranje dunder promenljivih (`locals_hide_dunder=True`)
* `test_get_locals_hide_sunder` - filtriranje sunder promenljivih (`locals_hide_sunder=True`)
* `test_get_locals_show_all` - prikaz svih lokalnih promenljivih (oba flaga `False`)
* `test_iter_syntax_lines_multiline` - `_iter_syntax_lines` vraća tačan niz tuple-ova za višelinijski opseg
