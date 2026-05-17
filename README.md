# Repülőjegy Foglalási Rendszer

Ez a projekt egy egyszerű, Python alapú repülőjegy foglalási rendszert valósít meg.

## Funkciók

- Jegy foglalása járatokra
- Belföldi és nemzetközi járatok külön listázása
- Kapacitás és szabad helyek kezelése
- Indulási idő megjelenítése
- Foglalás lemondása
- Aktuális foglalások listázása
- Menüben visszalépés `back` parancs használatával

## Használat

A program `main.py`-ben található menü alapú konzolos alkalmazás.

1. Indítsd el a programot:

```bash
python main.py
```

2. Válaszd a jegyfoglalást (`1`).
3. Válaszd a járattípust: `1` belföldi, `2` nemzetközi.
4. A rendszer megjeleníti az elérhető járatokat az indulási idővel, árral és szabad helyekkel.
5. Adj meg egy járatot sorszám alapján, majd az utazó nevét.
6. Ha bármely lépésnél vissza szeretnél térni a főmenübe, írd be: `back`.

## Kódrészek

- [Járat és járattípusok](./classes.py) – `Járat`, `BelföldiJarat`, `NemzetkoziJarat`
- [Légitársaság kezelés](./classes.py) – a `Légitársaság` osztály üzleti logikája, kapacitás- és időellenőrzés
- [Foglalási menü és használat](./main.py) – a menü alapú felhasználói felület és járatválasztás
- [Foglalás listázása](./main.py) – foglalások megjelenítése járat és indulási idő szerint

A fenti linkekre kattintva megnyithatod a kódfájlokat a megfelelő részekhez.

## Osztályok

- `Járat`: Absztrakt osztály a járatok alapvető attribútumaira, beleértve az indulási időt és kapacitást
- `BelföldiJarat`: Belföldi járatok
- `NemzetkoziJarat`: Nemzetközi járatok
- `Légitársaság`: Járatok és foglalások kezelése, kapacitás- és időellenőrzés
- `JegyFoglalás`: Jegyfoglalások tárolása egyedi azonosítóval

## Futtatás

Futtasd a `main.py` fájlt:

```bash
python main.py
```

## Benyújtás

A vizsgafeladathoz készítettem egy `NEPTUNKOD.docx` fájlt.
A fájlban található a GitHub repository linkje, amelyet cserélj ki a saját public repód URL-jére.

## Elvárások

- Python 3.x
- Standard könyvtárak használata