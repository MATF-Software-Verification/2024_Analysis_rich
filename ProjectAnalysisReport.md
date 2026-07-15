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

### 2.11 Pytest - Jedinični testovi

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


### 2.12 Coverage.py - Pokrivenost koda

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

**Napredak pokrivenosti po modulima:**

| Modul | Baseline | Final | Promena |
|-------|:--------:|:-----:|:-------:|
| traceback.py | 88% | 93% | +5% |
| progress.py | 92% | 93% | +1% |
| live.py | 96% | 98% | +2% |

**Analiza rezultata:**

Dodavanjem 25 testova pokriveno je 24 novih linija koda (nepokrivene statements pale sa 435 na 411), pri čemu ukupna pokrivenost projekta ostaje na visokih 95%. Najznačajniji napredak je u modulu `traceback.py` koji je porastao sa 88% na 93% (+5 procentnih poena), što direktno odražava nove testove koji pokrivaju konstrukciju traceback objekata i filtriranje lokalnih promenljivih. Modul `live.py` porastao je sa 96% na 98% (+2 poena), a `progress.py` sa 92% na 93% (+1 poen).


### 2.2 MyPy - Type checking

**Opis:** Statički type checker za Python koji proverava type hints i detektuje type safety probleme.

**Korišćenje:**

```bash
mypy rich/ --ignore-missing-imports --html-report reports/mypy --txt-report reports/mypy
```

**Rezultati:**

Type Coverage: 96.56% precise

Overall metrics:

| Metrika | Vrednost |
|---------|----------|
| Total lines analyzed | 26.696 LOC |
| Type precision | 96.56% |
| Imprecision | 3.44% |
| Modules analyzed | 78 |
| Type errors | 1 |

**Analiza po modulima:**

Moduli sa najboljom type coverage (0% imprecision):

* `_emoji_codes.py` (3.610 LOC)
* `_spinners.py` (482 LOC)
* `_palettes.py` (309 LOC)
* `terminal_theme.py` (153 LOC)
* `_ratio.py` (153 LOC)
* `spinner.py` (132 LOC)
* `theme.py` (115 LOC)
* `live_render.py` (106 LOC)

Moduli sa najvišom imprecision:

* `_loop.py` - 46.51% (43 LOC, interne iteracijske petlje)
* `_stack.py` - 25.00% (16 LOC, generički stack helper)
* `repr.py` - 23.49% (149 LOC, dinamički `__repr__` generatori)
* `_inspect.py` - 16.04% (268 LOC, runtime introspekcija objekata)
* `prompt.py` - 16.00% (400 LOC, dinamička konverzija korisničkog ulaza)
* `pretty.py` - 15.85% (1.016 LOC, rekurzivni pretty-printing proizvoljnih objekata)
* `syntax.py` - 15.43% (985 LOC, integracija sa Pygments lexerima)

Testirani moduli:

* `traceback.py` - 8.23% imprecision (899 LOC)
* `live.py` - 4.75% imprecision (400 LOC)
* `progress.py` - 1.81% imprecision (1.715 LOC)
* `table.py` - 0.99% imprecision (1.006 LOC)
* `panel.py` - 0.32% imprecision (317 LOC)

Core moduli:

* `console.py` - 2.57% imprecision (2.680 LOC)
* `text.py` - 1.40% imprecision (1.361 LOC)
* `style.py` - 3.16% imprecision (792 LOC)
* `segment.py` - 1.33% imprecision (752 LOC)

**Interpretacija rezultata:**

96.56% type precision znači da 96.56% koda ima potpune, precizne type hints, dok 3.44% koda ima neprecizne ili nedostajuće type hints (missing annotations, generičke tipove poput `Any`, nepotpune type hints).

Većina nepreciznosti je koncentrisana u:

* Runtime introspekciji i pretty-printing-u proizvoljnih objekata (`_inspect.py`, `pretty.py`, `repr.py`) — po prirodi rade sa `Any` tipovima jer obrađuju objekte nepoznate strukture
* Dinamičkoj konverziji korisničkog ulaza (`prompt.py`)
* Integraciji sa eksternim bibliotekama (`syntax.py` / Pygments)
* Internim helper-ima male veličine (`_loop.py`, `_stack.py`) gde visok procenat potiče od malog broja linija

Detektovana je 1 type greška — `redundant-cast` u `console.py` (linija 1540), suvišan `cast` na već poznati `Literal` tip. Reč je o postojećem kodu projekta, ne o unetim izmenama.

**Analiza:**

Za terminal rendering biblioteku koja mora da rukuje ANSI escape sekvencama, cross-platform konzolnim izlazom (Windows/Unix), dinamičkim pretty-printing-om proizvoljnih Python objekata i integracijom sa eksternim lexerima, rezultat od 96.56% type precision je izvanredan i pokazuje production-grade type safety. Preostala nepreciznost je logično locirana u modulima koji po svojoj prirodi rade sa dinamičkim ili introspektivnim tipovima.

### 2.3 Radon - Code complexity

**Opis:** Alat za analizu ciklomatske kompleksnosti i indeksa održivosti (maintainability index) Python koda.

**Korišćenje:**

```bash
radon cc rich/ -a -s
radon mi rich/ -s
radon raw rich/ -s
```

**Rezultati:**

**Ciklomatska kompleksnost:**

Prosečna kompleksnost: A (3.24) — analizirano 1027 blokova (klase, funkcije, metode)

Ocene kompleksnosti:

* A (1-5): Nizak rizik
* B (6-10): Umeren rizik
* C (11-20): Visok rizik
* D (21-30): Vrlo visok rizik
* E (31-40): Ekstremno visok rizik
* F (>40): Kritičan rizik

Distribucija kompleksnosti:

| Grade | Range | Count | Percent |
|-------|-------|-------|---------|
| A | 1-5 | 882 | 85.9% |
| B | 6-10 | 93 | 9.1% |
| C | 11-20 | 37 | 3.6% |
| D | 21-30 | 9 | 0.9% |
| E | 31-40 | 4 | 0.4% |
| F | >40 | 2 | 0.2% |

Top 10 najkompleksnijih funkcija:

* `Style.__init__` - F (49) - style.py
* `Table._render` - F (49) - table.py
* `Style.__str__` - E (35) - style.py
* `Traceback.extract` - E (34) - traceback.py
* `Markdown.__rich_console__` - E (33) - markdown.py
* `Console.__init__` - E (32) - console.py
* `Table._calculate_column_widths` - D (29) - table.py
* `Inspect._render` - D (28) - _inspect.py
* `Syntax._get_syntax` - D (26) - syntax.py
* `Tree.__rich_console__` - D (23) - tree.py

**Indeks održivosti po modulima:**

Najbolji moduli (MI = 100.00, A):

* `_emoji_codes.py`, `_spinners.py`, `_palettes.py`, `_cell_widths.py` (veliki data moduli)
* `errors.py`, `region.py`, `themes.py`, `_loop.py`, `_pick.py`, `_extension.py`

Za poboljšanje (najniži MI):

* `console.py` - 0.00 (C) - artefakt velikog fajla (2.680 LOC)
* `text.py` - 6.43 (C) - veliki modul (1.361 LOC)
* `progress.py` - 8.90 (C) - veliki modul (1.715 LOC)
* `markdown.py` - 19.92 (A)
* `syntax.py` - 27.16 (A)

Testirani moduli:

* `panel.py` - MI 48.10 (A)
* `live.py` - MI 36.71 (A)
* `traceback.py` - MI 29.93 (A)
* `table.py` - MI 14.80 (B)
* `progress.py` - MI 8.90 (C)

**Raw metrike:**

| Metrika | Vrednost |
|---------|----------|
| LOC (ukupno linija) | 26.696 |
| SLOC (linije koda) | 19.999 |
| LLOC (logičke linije) | 10.655 |
| Komentari + docstring-ovi | 12% linija |

**Analiza:**

Rich demonstrira odličan balans između funkcionalnosti i održivosti sa prosečnom kompleksnošću od 3.24 i 85.9% funkcija sa ocenom A (nizak rizik). Preostala kompleksnost je koncentrisana u očekivanim mestima za rendering biblioteku — u `__rich_console__` render metodama, konstruktorima velikih klasa (`Style`, `Console`, `Table`) i logici za parsiranje (markup, ANSI, sintaksa).

Niži indeks održivosti kod `console.py`, `text.py` i `progress.py` nije posledica lošeg koda već veličine fajlova — maintainability index oštro kažnjava velike module, a ta tri fajla su najveća u projektu (2.680, 1.361 i 1.715 LOC). Udeo komentara i docstring-ova od 12% pokazuje da je kod dokumentovan prevashodno kroz docstring-ove (2.896 linija), a ne kroz inline komentare.

### 2.4 Pylint - Statička analiza

**Opis:** Alat za analizu kvaliteta koda, detekciju code smells i proveru imenovanja i kompleksnosti.

**Korišćenje:**

```bash
pylint rich/ --output-format=text --reports=y
```

**Rezultati:**

Pylint score: 8.26/10

Problemi po kategoriji:

| Kategorija | Broj | Opis |
|------------|------|------|
| Convention | 666 | Stilske konvencije |
| Refactor | 418 | Preporuke za refaktorisanje |
| Warning | 403 | Upozorenja |
| Error | 16 | Greške (false positives) |
| **Ukupno** | **1503** | |

Top 10 najčešćih problema:

* `line-too-long` (409) - Linije duže od 100 karaktera
* `redefined-outer-name` (169) - Preklapanje imena parametra i imena iz spoljnog opsega
* `cyclic-import` (117) - Ciklične zavisnosti između modula
* `protected-access` (102) - Pristup zaštićenim članovima (framework pattern)
* `missing-module-docstring` (73) - Moduli bez docstring-a
* `too-many-arguments` (71) - Render metode prirodno imaju mnogo parametara
* `unused-argument` (49) - Standardizovani `__rich_console__` interfejs
* `too-many-locals` (46) - Kompleksne render metode
* `too-few-public-methods` (46) - Data/helper klase
* `missing-function-docstring` (40) - Interne funkcije bez docstring-a

Objašnjenje ključnih problema:

`cyclic-import` (117): Posledica arhitekture Rich-a gde su moduli međusobno tesno povezani (npr. `console` → `theme` → `style` → `color`). Rich to rešava lazy import-ima unutar funkcija, što pylint dodatno prijavljuje kao `import-outside-toplevel` (40).

`protected-access` (102): Neophodan u framework kodu — metode poput `Style._add` ili `Text._spans` pristupaju zaštićenim članovima drugih instanci iste klase radi performansi, što je legitiman obrazac unutar jednog modula.

`too-many-arguments` (71) i `too-many-positional-arguments` (20): Render metode i konstruktori (`Console.__init__` sa 27 parametara, `Table.__init__` sa 25) prirodno imaju mnogo konfiguracijskih opcija. Rich korisnicima preporučuje keyword argumente, što kod čini čitljivim uprkos kompleksnim potpisima.

`unused-argument` (49): Posledica standardizovanog `__rich_console__(self, console, options)` protokola — svaka renderable klasa mora održavati isti potpis čak i kada ne koristi sve parametre.

Broj grešaka (Error, 16): Radi se o false positive-ima — pylint prijavljuje `no-member` na dinamički dodeljenim atributima i `undefined-variable` za `get_ipython` (dostupan samo u Jupyter okruženju), što nisu stварne greške u izvršavanju.

**Analiza:**

Rich kod ima visok kvalitet sa ocenom 8.26/10. Većina pylint upozorenja su stilske prirode (`line-too-long` čini preko četvrtine svih poruka) ili framework-specifični obrasci koji su u kontekstu terminal rendering biblioteke opravdani (`protected-access`, `unused-argument`, `cyclic-import`, `too-many-arguments`). Dokumentovanost je visoka na nivou metoda (96%) i klasa (87%), dok je udeo docstring-ova u kodu 33%, što pokazuje dobro dokumentovan kod.


### 2.5 Vulture - Detekcija mrtvog koda

**Opis:** Alat za statičku detekciju nekorišćenog (mrtvog) koda — funkcija, klasa, metoda, importa i promenljivih koje se nigde ne referenciraju.

**Korišćenje:**

```bash
vulture rich/ --min-confidence 60
```

**Rezultati:**

Ukupno prijavljeno: 89 potencijalnih nalaza

Po tipu:

| Tip | Broj |
|-----|------|
| unused variable | 30 |
| unused method | 18 |
| unused class | 12 |
| unused attribute | 11 |
| unused property | 6 |
| unused function | 4 |
| unused import | 1 |

Nalazi visoke pouzdanosti (90-100%):

* `_null_file.py` - 12 nepovezanih argumenata (`__n`, `__limit`, `__hint`, `__offset`, `__whence`, `__size`, `__lines`, `__t`, `__value`, `__traceback`) — parametri metoda koje implementiraju `IO` interfejs ali su prazne (null objekat)
* `style.py:29` i `syntax.py:232` - `objtype` — parametar `__get__` descriptor protokola
* `progress.py:14` - nekorišćen import `PathLike` (90%)

Reprezentativni nalazi niske pouzdanosti (60%):

* Javne API klase: `Emoji`, `Bar`, `VerticalCenter`, `FloatPrompt`, `MofNCompleteColumn`, `TransferSpeedColumn`, `FileSizeColumn`
* Javne API metode: `Console.print_exception`, `Console.save_svg`, `Console.save_text`, `Table.add_section`, `Layout.unsplit`
* Javne properties: `Task.percentage`, `Progress.task_ids`, `ProgressBar.percentage_completed`

**Analiza:**

Vulture prijavljuje 89 potencijalnih nalaza, ali je ključno razlikovati stvarni mrtav kod od false-positive-a, koji su kod biblioteke inherentno česti. Za razliku od aplikacije (gde je sav kod pozvan interno), biblioteka izlaže javni API koji koriste spoljni korisnici — te funkcije i klase se nigde *unutar* projekta ne pozivaju, pa ih vulture pogrešno označava kao mrtve.

Nalazi visoke pouzdanosti (90-100%) su legitimni, ali bezopasni: parametri `_null_file.py` (`__n`, `__limit`...) postoje jer klasa `NullFile` mora da ispuni `IO` interfejs iako su metode prazne, a `objtype` je deo standardnog descriptor protokola (`__get__`). Jedini pravi nalaz je nekorišćen import `PathLike` u `progress.py` (90%).

Nalazi niske pouzdanosti (60%) su gotovo isključivo false-positive-i — javne klase (`Emoji`, `FloatPrompt`, kolone za progress bar), javne metode (`Console.save_svg`, `Table.add_section`) i properties koje čine deo API-ja koji Rich izlaže korisnicima. Njihovo uklanjanje bi razbilo biblioteku.

Zaključak: Rich nema značajan mrtav kod. Rezultat pre svega ilustruje ograničenje statičke analize mrtvog koda nad bibliotekama — potrebno je ručno tumačenje umesto slepog uklanjanja prijavljenih stavki.

### 2.6 Interrogate - Pokrivenost dokumentacije

**Opis:** Alat za merenje procenta docstring pokrivenosti — proverava koliko modula, klasa, funkcija i metoda ima docstring.

**Korišćenje:**

```bash
interrogate rich/ -v
```

**Rezultati:**

Docstring coverage: 59.1% (686 od 1160 objekata dokumentovano)

Rezultat: FAILED prema podrazumevanom pragu od 80%

Moduli sa najboljom pokrivenošću:

* `__init__.py` - 100%
* `_spinners.py` - 100%
* `_timer.py` - 100%
* `errors.py` - 90%
* `measure.py` - 89%
* `_win32_console.py` - 89%
* `cells.py` - 83%
* `segment.py` - 81%

Moduli sa najnižom pokrivenošću:

* `rule.py` - 14%
* `__main__.py` - 17%
* `bar.py` - 17%
* `constrain.py` - 20%
* `styled.py` - 20%
* `containers.py` - 24%
* `file_proxy.py` - 25%
* `screen.py` - 25%

Testirani moduli:

* `table.py` - 70%
* `progress.py` - 56%
* `live.py` - 58%
* `panel.py` - 33%
* `traceback.py` - 33%

**Analiza:**

Interrogate meri strožiju metriku od ostalih alata: broji apsolutno svaki objekat — modul, klasu, funkciju, metodu, uključujući privatne (`_`), dunder (`__init__`, `__rich_console__`) i ugnježdene funkcije. Zato je rezultat od 59.1% niži nego što bi se očekivalo na osnovu pylint izveštaja, koji je pokazao 96% dokumentovanih metoda — pylint prevashodno prati javne članove, dok interrogate ne pravi razliku.

Nizak procenat je najvećim delom posledica dizajna Rich-a, a ne nedostatka dokumentacije:

* Protokolske metode (`__rich_console__`, `__rich_measure__`, `__rich_repr__`) se ponavljaju u desetinama klasa i po konvenciji nemaju docstring jer im je značenje standardizovano
* Dunder metode (`__init__`, `__eq__`, `__len__`, `__enter__`) retko nose docstring
* Interni moduli (`_null_file.py`, `_log_render.py`, `_emoji_codes.py`) sa 0% su implementacioni detalji koji ne čine javni API

Nasuprot tome, javni API je dobro dokumentovan — glavne korisničke klase kao `Console` (76%), `Text` (75%), `Table` (70%) i `Syntax` (74%) imaju visoku pokrivenost, što se poklapa sa pylint metrikom o dokumentovanosti javnog interfejsa.

Zaključak: Ocena „FAILED" ne znači loše dokumentovan projekat, već da podrazumevani prag od 80% računa i interne/protokolske metode koje po konvenciji nemaju docstring. Realna dokumentovanost javnog API-ja je znatno viša od ukupnih 59.1%.

