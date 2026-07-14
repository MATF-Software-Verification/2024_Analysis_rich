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

#### progress.py (6 testova)

**Cilj:** Testiranje `rich.progress` modula — kreiranje progress barova, upravljanje taskovima, čitanje fajlova sa praćenjem napretka i pozadinsko ažuriranje

**Pokriveni scenariji:**

* `test_progress_creation` - kreiranje `Progress`-a sa custom kolonama (`TextColumn`, `BarColumn`, `TimeRemainingColumn`) i verifikacija default vrednosti (`finished=True` bez taskova, `disable=False`, `expand=False`)
* `test_add_task` - dodavanje taska preko `add_task()` i provera inicijalnog stanja (`description`, `total`, `completed=0`, `finished=False`)
* `test_task_defaults` - default vrednosti `Task` objekta (`finished=False`, `visible=True`)
* `test_task_percentage` - izračunavanje procenta napretka (`completed=50`, `total=100` → `percentage=50.0`)
* `test_reader_next` - `_Reader` wrapper čita fajl liniju po liniju i inkrementalno ažurira napredak taska
* `test_track_thread_advances` - `_TrackThread` pozadinska nit ažurira `completed` vrednost taska tokom vremena
#### live.py (5 testova)

**Cilj:** Testiranje `rich.live` modula — kreiranje i životni ciklus `Live` displeja, ažuriranje sadržaja, ugneždeni displeji i auto-refresh ponašanje

**Pokriveni scenariji:**

* `test_live_creation` - default vrednosti `Live` objekta (`is_started=False`, `auto_refresh=True`, `_nested=False`, `transient=False`)
* `test_live_is_started` - životni ciklus preko `start()` / `stop()` i praćenje `is_started` stanja
* `test_live_update` - ažuriranje sadržaja preko `update()`, string se konvertuje u `Text` objekat
* `test_live_auto_refresh_false` - sa `auto_refresh=False` ne kreira se refresh nit (`_refresh_thread is None`), context manager korektno gasi displej
* `test_live_nested` - ugnežden `Live` unutar drugog dobija `_nested=True`
#### panel.py (3 testa)

**Cilj:** Testiranje `rich.panel` modula — kreiranje panela, fit režim i rukovanje naslovom

**Pokriveni scenariji:**

* `test_panel_creation` - default vrednosti `Panel` objekta (`title=None`, `subtitle=None`, `expand=True`, `highlight=False`)
* `test_panel_fit` - `Panel.fit()` kreira panel koji se skuplja na sadržaj (`expand=False`) uz prosleđen naslov
* `test_panel_with_title` - panel sa naslovom, default poravnanje naslova je `center` (`title_align="center"`)
#### table.py (2 testa)

**Cilj:** Testiranje `rich.table` modula — kreiranje tabela sa kolonama i redovima, kao i grid režim

**Pokriveni scenariji:**

* `test_table_add_column_and_row` - kreiranje tabele sa 3 kolone, dodavanje reda preko `add_row()` i verifikacija `columns`/`row_count` i header vrednosti
* `test_table_grid` - `Table.grid()` kreira tabelu bez okvira i header-a (`show_header=False`, `show_footer=False`, `show_edge=False`, `box=None`)


**Korišćenje:** Testovi se pokreću iz korenskog direktorijuma projekta komandom:

​```bash
pytest tests/ -v
​```

**Rezultati:**

* Svi testovi prolaze: 100% pass rate


### 2.2 Coverage.py - Pokrivenost koda

**Opis:** Alat za merenje pokrivenosti koda testovima - procenat koda izvršen tokom testiranja.

**Rezultati:**

Baseline coverage (samo originalni Rich testovi):

```bash
pytest tests/ --cov=rich --cov-report=term-missing --cov-report=html
```

```bash
Total Statements:    8166
Missed Statements:    435
Overall Coverage:     94.67% (95%)
```

Final coverage (originalni + naši testovi):

```bash
pytest tests/ ~/Desktop/2024_Analysis_rich/tests \
  --cov=rich \
  --cov-report=term-missing \
  --cov-report=html
```

```bash
Total Statements:    8166
Missed Statements:    411
Overall Coverage:     94.97% (95%)
Change:               +24 pokrivenih linija (+0.3%)
```
