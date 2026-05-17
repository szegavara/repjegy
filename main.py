"""
Repülőjegy Foglalási Rendszer - Fő program

Ez a modul tartalmazza a fő programot, amely inicializálja a rendszert
és biztosítja a felhasználói interfészt.
"""

from classes import *
from datetime import datetime, timedelta

def main():
    """
    A fő függvény, amely inicializálja a rendszert és futtatja a felhasználói interfészt.
    """
    # Inicializálás
    légitársaság = Légitársaság("Magyar Légitársaság")

    # Járatok hozzáadása - 2 belföldi és 1 nemzetközi járat
    now = datetime.now()
    járat1 = BelföldiJarat("BH101", "Budapest", 50000, now + timedelta(days=1), 100)
    járat2 = BelföldiJarat("BH102", "Debrecen", 40000, now + timedelta(days=2), 50)
    járat3 = NemzetkoziJarat("NH201", "London", 150000, now + timedelta(days=3), 200)

    légitársaság.add_járat(járat1)
    légitársaság.add_járat(járat2)
    légitársaság.add_járat(járat3)

    # 6 foglalás előre betöltése a rendszer indulásakor
    légitársaság.jegy_foglalása("BH101", "Anna")
    légitársaság.jegy_foglalása("BH101", "Béla")
    légitársaság.jegy_foglalása("BH102", "Cili")
    légitársaság.jegy_foglalása("BH102", "Dani")
    légitársaság.jegy_foglalása("NH201", "Elek")
    légitársaság.jegy_foglalása("NH201", "Feri")

    # Felhasználói interfész - egyszerű menü alapú rendszer
    while True:
        print("\nRepülőjegy Foglalási Rendszer")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        choice = input("Válassz: ").strip()

        if choice == "1":
            # Jegy foglalása - járatlista megjelenítésével
            if not légitársaság.járatok:
                print("Hiba: Nincsenek elérhető járatok")
                continue
            
            print("\nElérhető járatok:")
            for idx, járat in enumerate(légitársaság.járatok, 1):
                booked_count = sum(1 for f in légitársaság.foglalások if f.járat.járatszám == járat.járatszám)
                szabad_helyek = járat.kapacitás - booked_count
                print(f"{idx}. {járat.járatszám} -> {járat.célállomás}, Ár: {járat.jegyár} Ft, Szabad helyek: {szabad_helyek}/{járat.kapacitás}")
            
            járat_index_input = input("Válassz járat számot: ").strip()
            try:
                járat_index = int(járat_index_input) - 1
                if járat_index < 0 or járat_index >= len(légitársaság.járatok):
                    print("Hiba: Érvénytelen járat választás")
                    continue
                kiválasztott_járat = légitársaság.járatok[járat_index]
            except ValueError:
                print("Hiba: Érvénytelen szám")
                continue
            
            utazó_név = input("Utazó neve: ").strip()
            if not utazó_név:
                print("Hiba: Utazó név kötelező")
                continue
            try:
                ár = légitársaság.jegy_foglalása(kiválasztott_járat.járatszám, utazó_név)
                print(f"Foglalás sikeres, ár: {ár} Ft")
            except ValueError as e:
                print(f"Hiba: {e}")
        elif choice == "2":
            # Foglalás lemondása - csak létező foglalásokra
            id_input = input("Foglalás ID: ").strip()
            try:
                foglalás_id = int(id_input)
            except ValueError:
                print("Hiba: Érvénytelen ID, számot adjon meg")
                continue
            try:
                légitársaság.foglalás_lemondása(foglalás_id)
                print("Foglalás lemondva")
            except ValueError as e:
                print(f"Hiba: {e}")
        elif choice == "3":
            # Foglalások listázása
            foglalások = légitársaság.foglalások_listázása()
            for f in foglalások:
                print(f"ID: {f.foglalás_id}, Utazó: {f.utazó_név}, Járat: {f.járat.járatszám} -> {f.járat.célállomás}, Ár: {f.jegyár} Ft")
        elif choice == "4":
            break
        else:
            print("Érvénytelen választás")

if __name__ == "__main__":
    main()