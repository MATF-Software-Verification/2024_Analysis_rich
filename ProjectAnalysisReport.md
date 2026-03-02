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

**Opis**: Framework za pisanje i pokretanje unit testova u Python-u.  

**Korišćenje**: Napisana su 2 jednostavna testa koji pokrivaju osnovne funkcionalnosti Rich biblioteke:

#### test_json_custom.py (1 test)

**Cilj**: Testiranje osnovnog renderovanja JSON objekata

**Pokriveni scenariji**:

- Renderovanje validnog JSON stringa  
- Provera prisustva ključnih vrednosti (`string`, `number`, `list`) u terminal output-u  
- Integracija `JSON` objekta sa `Console` klasom

#### test_progress_unit.py (1 test)

**Cilj**: Testiranje osnovnog rada progress bar-a

**Pokriveni scenariji**:

- Kreiranje progress objekta i dodavanje taska  
- Ažuriranje taska i izračunavanje procenta završetka  
- Provera da logika progress bara pravilno računa completion procent  

**Komanda za pokretanje testova**:

```bash
pytest unit_tests/ -v
