"""
Repülőjegy Foglalási Rendszer - Osztályok

Ez a modul tartalmazza a repülőjegy foglalási rendszer összes osztályát.
"""

from abc import ABC, abstractmethod
from datetime import datetime

class Járat(ABC):
    """
    Absztrakt osztály a járatok alapvető attribútumaira.

    Attribútumok:
        járatszám (str): A járat egyedi azonosítója
        célállomás (str): A járat célállomása
        jegyár (int): A jegy ára forintban
        indulás_idő (datetime): A járat indulási ideje
        kapacitás (int): A járat maximális férőhelye
    """
    def __init__(self, járatszám, célállomás, jegyár, indulás_idő, kapacitás):
        self._járatszám = járatszám
        self._célállomás = célállomás
        self._jegyár = jegyár
        self._indulás_idő = indulás_idő
        self._kapacitás = kapacitás

    @property
    def járatszám(self):
        """Visszaadja a járatszámot."""
        return self._járatszám

    @property
    def célállomás(self):
        """Visszaadja a célállomást."""
        return self._célállomás

    @property
    def jegyár(self):
        """Visszaadja a jegyárat."""
        return self._jegyár

    @property
    def indulás_idő(self):
        """Visszaadja az indulás időpontját."""
        return self._indulás_idő

    @property
    def kapacitás(self):
        """Visszaadja a járat kapacitását."""
        return self._kapacitás

class BelföldiJarat(Járat):
    """
    Belföldi járatok osztálya. Olcsóbb és általában rövidebb járatok.
    """
    def __init__(self, járatszám, célállomás, jegyár, indulás_idő, kapacitás):
        super().__init__(járatszám, célállomás, jegyár, indulás_idő, kapacitás)

class NemzetkoziJarat(Járat):
    """
    Nemzetközi járatok osztálya. Magasabb jegyárakkal.
    """
    def __init__(self, járatszám, célállomás, jegyár, indulás_idő, kapacitás):
        super().__init__(járatszám, célállomás, jegyár, indulás_idő, kapacitás)

class Légitársaság:
    """
    Légitársaság osztály, amely kezeli a járatokat és foglalásokat.

    Attribútumok:
        név (str): A légitársaság neve
        járatok (list): A légitársaság járatai
        foglalások (list): Az aktív foglalások
    """
    def __init__(self, név):
        self._név = név
        self._járatok = []
        self._foglalások = []

    @property
    def név(self):
        """Visszaadja a légitársaság nevét."""
        return self._név

    @property
    def járatok(self):
        """Visszaadja a járatok listáját."""
        return self._járatok

    @property
    def foglalások(self):
        """Visszaadja a foglalások listáját."""
        return self._foglalások

    def add_járat(self, járat):
        """Hozzáad egy járatot a légitársasághoz."""
        self._járatok.append(járat)

    def jegy_foglalása(self, járatszám, utazó_név):
        """
        Foglal egy jegyet a megadott járatra.

        Args:
            járatszám (str): A járat azonosítója
            utazó_név (str): Az utazó neve

        Returns:
            int: A foglalás ára

        Raises:
            ValueError: Ha a járat nem található, nem elérhető vagy a foglalás időpontja érvénytelen
        """
        járat = next((j for j in self._járatok if j.járatszám == járatszám), None)
        if not járat:
            raise ValueError("Járat nem található")
        if járat.indulás_idő <= datetime.now():
            raise ValueError("Foglalás csak jövőbeli járatokra lehetséges")
        booked_count = sum(1 for f in self._foglalások if f.járat.járatszám == járatszám)
        if booked_count >= járat.kapacitás:
            raise ValueError("Járat megtelt")
        foglalás = JegyFoglalás(járat, utazó_név)
        self._foglalások.append(foglalás)
        return foglalás.jegyár

    def foglalás_lemondása(self, foglalás_id):
        """
        Lemond egy foglalást.

        Args:
            foglalás_id (int): A foglalás azonosítója

        Raises:
            ValueError: Ha a foglalás nem található
        """
        foglalás = next((f for f in self._foglalások if f.foglalás_id == foglalás_id), None)
        if not foglalás:
            raise ValueError("Foglalás nem található")
        self._foglalások.remove(foglalás)

    def foglalások_listázása(self):
        """
        Visszaadja az összes aktív foglalást.

        Returns:
            list: A foglalások listája
        """
        return self._foglalások

class JegyFoglalás:
    """
    Jegyfoglalás osztály, amely egy utazásra szóló jegy foglalását tárolja.

    Attribútumok:
        járat (Járat): A foglalt járat
        utazó_név (str): Az utazó neve
        foglalás_id (int): Egyedi foglalás azonosító
    """
    _next_id = 1

    def __init__(self, járat, utazó_név):
        self._járat = járat
        self._utazó_név = utazó_név
        self._foglalás_id = JegyFoglalás._next_id
        JegyFoglalás._next_id += 1

    @property
    def járat(self):
        """Visszaadja a foglalt járatot."""
        return self._járat

    @property
    def utazó_név(self):
        """Visszaadja az utazó nevét."""
        return self._utazó_név

    @property
    def foglalás_id(self):
        """Visszaadja a foglalás azonosítóját."""
        return self._foglalás_id

    @property
    def jegyár(self):
        """Visszaadja a jegy árát."""
        return self._járat.jegyár