# Repülőjegy Foglalási Rendszer

Ez a projekt egy egyszerű, Python alapú repülőjegy foglalási rendszert valósít meg.

## Funkciók

- Jegy foglalása járatokra
- Belföldi és nemzetközi járatok külön listázása
- Kapacitás és szabad helyek kezelése
- Indulási idő megjelenítése
- Foglalás lemondása
- Aktuális foglalások listázása
- Menüben visszalépés "back" parancs használatával

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

## Elvárások

- Python 3.x
- Standard könyvtárak használata