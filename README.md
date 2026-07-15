# Analiza projekta: Rich - Rich text and beautiful formatting in the terminal

**Autor:** Jovan Ranđelović
**Broj indeksa:** 1088/2023
**Kurs:** Verifikacija Softvera

## O projektu

**Analizirani projekat:** Rich

Rich je Python biblioteka otvorenog koda za rad sa formatiranim tekstom i lepim prikazom u terminalu — bojama, stilovima, tabelama, progress barovima, markdown-om, sintaksnim isticanjem i drugim. Razvijena od strane Textualize tima.

**Osnovne informacije:**

* Repository: https://github.com/Textualize/rich
* Jezik: Python
* Analizirana grana: master
* Commit hash: f82a399d584092f0195d0f68add0c03531e02c84
* Datum commita: 2025-12-02

## Korišćeni alati

Projekat koristi 6 različitih alata za sveobuhvatnu analizu kvaliteta koda:

| # | Alat | Kategorija | Opis |
|---|------|------------|------|
| 1 | Pytest / Coverage | Testiranje | Jedinični testovi i pokrivenost koda |
| 2 | Pylint | Statička analiza | Kvalitet koda |
| 3 | MyPy | Type checking | Type safety |
| 4 | Radon | Kompleksnost | Ciklomatska kompleksnost |
| 5 | Vulture | Mrtav kod | Detekcija nekorišćenog koda |
| 6 | Interrogate | Dokumentacija | Pokrivenost docstring-ova |

## Rezultati analize

### 1. Pytest i Coverage - Testiranje i pokrivenost koda

**Napisano testova:** 25 novih testova

**Distribucija:**

* test za `traceback.py`: 9 testova
* test za `progress.py`: 6 testova
* test za `live.py`: 5 testova
* test za `panel.py`: 3 testa
* test za `table.py`: 2 testa

**Pokriveni scenariji:**

* Konstrukcija traceback objekata i dataclass default vrednosti
* Rukovanje ExceptionGroup-om (Python 3.11+)
* Robustnost sa objektima čiji `__str__` baca izuzetak
* Filtriranje lokalnih promenljivih (dunder/sunder)
* Progress barovi, taskovi i pozadinsko ažuriranje
* Životni ciklus Live displeja i ugnežden prikaz
* Kreiranje panela, fit režim i naslovi
* Kreiranje tabela i grid režim

**Status:** Svi testovi prolaze (100% pass rate)

**Komanda:**

```bash
pytest tests/ -v
```

**Pokrivenost koda (Coverage):**

```
Baseline:  95% (postojeći Rich testovi)
Final:     95% (Rich + naši testovi)
Change:    +27 pokrivenih linija (429 → 402 nepokrivenih)
```

**Napredak po modulima:**

* `traceback.py`: 88% → 93% (+5%)
* `live.py`: 93% → 96% (+3%)
* `progress.py`: 92% → 93% (+1%)

**Analiza:** Rich već ima izuzetno visoku baseline pokrivenost (95%), pa je prostor za rast ograničen. Naši testovi su ipak pokrili 24 dodatne linije, sa najvećim doprinosom u `traceback` modulu (+5%).

**Komanda:**

```bash
pytest tests/ ~/Desktop/2024_Analysis_rich/tests --cov=rich --cov-report=html
```

### 2. Pylint - Statička analiza

**Rezultati:**

Pylint Score: 8.26/10

Problemi po kategoriji:

| Kategorija | Broj | Procenat |
|------------|------|----------|
| Convention | 666 | 44.3% |
| Refactor | 418 | 27.8% |
| Warning | 403 | 26.8% |
| Error | 16 | 1.1% |
| Ukupno | 1503 | 100% |

**Najčešći problemi:**

* `line-too-long` (409) - Linije duže od 100 karaktera
* `redefined-outer-name` (169) - Preklapanje imena parametra i spoljnog opsega
* `cyclic-import` (117) - Ciklične zavisnosti između modula
* `protected-access` (102) - Pristup zaštićenim članovima (framework pattern)
* `missing-module-docstring` (73) - Moduli bez docstring-a

**Analiza:** Visok kvalitet koda. Većina problema je stilske prirode (`line-too-long`) ili framework-specifični obrasci (ciklične zavisnosti rešene lazy import-ima, pristup zaštićenim članovima unutar modula). 16 „Error" poruka su false-positive-i (dinamički atributi, Jupyter-only promenljive).

**Komanda:**

```bash
pylint rich/ --output-format=text --reports=y
```

### 3. MyPy - Type checking

**Rezultati:**

```
Type Precision: 96.56%
Imprecision:    3.44%
Type Errors:    1 (postojeći redundant-cast)
Lines Analyzed: 26.696 LOC
Modules:        78
```

**Analiza po modulima (najbolji/najgori):**

Najbolji (0% imprecision):

* `_emoji_codes.py`, `_spinners.py`, `_palettes.py`, `terminal_theme.py`

Za poboljšanje (najviša imprecision):

* `_inspect.py`, `pretty.py`, `repr.py` - runtime introspekcija (rade sa `Any`)
* `prompt.py` - dinamička konverzija korisničkog ulaza
* `syntax.py` - integracija sa Pygments lexerima

**Analiza:** Rich demonstrira odličnu type safety sa 96.56% type precision. Nepreciznost je logično koncentrisana u modulima koji po prirodi rade sa dinamičkim ili introspektivnim tipovima. Jedina prijavljena greška je suvišan `cast` u postojećem kodu.

**Komanda:**

```bash
mypy rich/ --ignore-missing-imports --html-report reports/mypy
```

### 4. Radon - Code complexity

**Rezultati:**

Average Complexity: A (3.24)

Distribucija kompleksnosti:

| Grade | Range | Count | Procenat |
|-------|-------|-------|----------|
| A | 1-5 | 882 | 85.9% |
| B | 6-10 | 93 | 9.1% |
| C | 11-20 | 37 | 3.6% |
| D | 21-30 | 9 | 0.9% |
| E | 31-40 | 4 | 0.4% |
| F | >40 | 2 | 0.2% |

**Najkompleksnije funkcije:**

* `Style.__init__` - F (49) - style.py
* `Table._render` - F (49) - table.py
* `Style.__str__` - E (35) - style.py
* `Traceback.extract` - E (34) - traceback.py

**Dodatne metrike:**

* Komentari + docstring-ovi: 12% linija (docstring-ovi: 2896 linija)

**Analiza:** Izuzetno niska prosečna kompleksnost sa 85.9% funkcija ocene A. Kompleksnost je koncentrisana u render metodama i konstruktorima velikih klasa.

**Komanda:**

```bash
radon cc rich/ -a -s
radon mi rich/ -s
```

### 5. Vulture - Detekcija mrtvog koda

**Rezultati:**

```
Ukupno nalaza:  89
Stvaran mrtav kod: 1 (nekorišćen import PathLike)
```

**Analiza:** Od 89 prijavljenih nalaza, gotovo svi su false-positive-i tipični za biblioteku — javne API klase (`Emoji`, `FloatPrompt`), javne metode (`Console.save_svg`, `Table.add_section`) i protokolske metode koje se nigde ne pozivaju *unutar* projekta ali ih koriste spoljni korisnici. Jedini stvaran nalaz je nekorišćen import. Rezultat ilustruje ograničenje statičke analize mrtvog koda nad bibliotekama.

**Komanda:**

```bash
vulture rich/ --min-confidence 60
```

### 6. Interrogate - Pokrivenost dokumentacije

**Rezultati:**

```
Docstring coverage: 59.1% (686 / 1160 objekata)
Rezultat: FAILED (prag 80%)
```

**Analiza:** Interrogate broji sve objekte, uključujući dunder (`__init__`), protokolske (`__rich_console__`) i privatne metode koje po konvenciji nemaju docstring. Zato je ukupan procenat niži nego pylint metrika o dokumentovanosti javnih metoda (96%). Javni API je dobro dokumentovan — glavne klase `Console` (76%), `Text` (75%), `Table` (70%). Niska ukupna ocena ne znači loše dokumentovan projekat, već strog način brojanja.

**Komanda:**

```bash
interrogate rich/ -v
```

## Sveobuhvatni zaključak

### Pozitivni aspekti

* Visok kvalitet postojećeg koda
  * 95% test coverage
  * 8.26/10 Pylint score
  * 96.56% type precision
  * 3.24 prosečna kompleksnost (ocena A)
* Održivost
  * 85.9% funkcija sa niskom kompleksnošću (grade A)
  * Praktično nema mrtvog koda (1 nalaz)
  * Dobro dokumentovan javni API (glavne klase iznad 70%)

### Identifikovani problemi

* Velike datoteke - 3 modula prelaze 1000 linija (`console.py`, `progress.py`, `text.py`)
* Visoka kompleksnost - 15 funkcija (1.5%) sa ocenom C+ i više
* Ciklične zavisnosti - 117 `cyclic-import` upozorenja (rešeno lazy import-ima)
* Stilske nedoslednosti - 409 linija preko 100 karaktera

### Vrednost analize

Iako naši testovi nisu značajno povećali numerički coverage (Rich je već izuzetno pokriven), analiza je pružila:

* Validaciju kvaliteta postojećeg koda
* Potvrdu održivosti i type safety
* Demonstraciju multi-tool pristupa verifikaciji
* Razumevanje da coverage nije jedina metrika kvaliteta
* Uvid u ograničenja alata nad bibliotekama (vulture i interrogate)

## Struktura projekta

Svaki alat ima svoj direktorijum sa skriptom za pokretanje i rezultatima:

```
2024_Analysis_rich/
├── README.md
├── ProjectAnalysisReport.md
├── tests/                    # Jedinični testovi
├── run_all.sh                # Pokreće sve alate
├── pytest/
│   ├── run_pytest.sh
│   └── results/
├── coverage/
│   ├── run_coverage.sh
│   └── results/
├── pylint/
│   ├── run_pylint.sh
│   └── results/
├── mypy/
│   ├── run_mypy.sh
│   └── results/
├── radon/
│   ├── run_radon.sh
│   └── results/
├── vulture/
│   ├── run_vulture.sh
│   └── results/
└── interrogate/
    ├── run_interrogate.sh
    └── results/
```

## Pokretanje analiza

```bash
# Sve odjednom
./run_all.sh

# Pojedinačno - svaki alat iz svog direktorijuma
./pytest/run_pytest.sh
./coverage/run_coverage.sh
./pylint/run_pylint.sh
./mypy/run_mypy.sh
./radon/run_radon.sh
./vulture/run_vulture.sh
./interrogate/run_interrogate.sh
```
