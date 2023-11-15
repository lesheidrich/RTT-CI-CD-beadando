"""
Modul: EKKE - Multiparadigmas programozas
Szuperhos letrehozo es karakterizalo modul.
"""


class Szuperhos:
    """
    Szuperhos peldanyositasra osztaly. Lehet varialni kepessegekkel, propertikkel, etc.
    """

    def __init__(self, nev: str, szuperero: int = 50):
        self.__nev = nev
        self.__szuperero = szuperero
        self.__kepessegek = []
        print("Szuperhos letrehozva!")

    def udvozles(self) -> None:
        """
        Visszakoszon a csavoka.
        :return: None
        """
        print(f"Az en nevem: {self.__nev}")

    @property
    def nev(self) -> str:
        """
        Hos nev getter.
        :return: string: szuperhos nev
        """
        return self.__nev

    @property
    def szuperero(self) -> int:
        """
        Szuperero getter.
        :return: int: szuerhos ereje.
        """
        return self.__szuperero

    @property
    def kepessegek(self) -> [str]:
        """
        Kepessegek getter.
        :return: [str]: kepessegek
        """
        return self.__kepessegek

    @nev.setter
    def nev(self, ujnev: str) -> None:
        """
        Szuperhos str nev setter.
        :param ujnev: str: Hos uj neve
        :return: None
        """
        self.__nev = ujnev

    @szuperero.setter
    def szuperero(self, ertek: int) -> None:
        """
        Szuperero setter int ertek alapjan.
        :param ertek: int: Hos uj ero szamerteke.
        :return: None
        """
        self.__szuperero = ertek

    @kepessegek.setter
    def kepessegek(self, lista: list) -> None:
        """
        beallitja a szuperhos kepessegeit string, vagy string lista alapjan
        :param lista: str lista
        :return: None
        """
        if type(lista) == str:
            self.__kepessegek.append(lista)
        else:
            for i in lista:
                self.__kepessegek.append(i)

    def __str__(self) -> str:
        """
        Bemutatkozik a hos egy stringgel.
        :return: str: bemutatkozas info
        """
        return f"A nevem: {self.__nev} es a szupererom erteke {str(self.__szuperero)}."

    def __eq__(self, masik_hos: object) -> bool:
        """
        osszehasonlit ket host
        :param masik_hos: object: masik hos
        :return: bool: egyforma
        """
        return self.nev == masik_hos.nev and self.szuperero == masik_hos.szuperero

    def __add__(self, uj_kepesseg) -> None:
        """
        Eljaras kiegesziti argumentumul megadott kepesseggel a kepesseg propertyt
        :param uj_kepesseg: str vagy str alapu list-et var argumentkent
        :return: None
        """
        if isinstance(uj_kepesseg, str):
            self.__kepessegek.append(uj_kepesseg)
        elif isinstance(uj_kepesseg, list):
            for kepessegek in uj_kepesseg:
                if isinstance(kepessegek, str):
                    self.__kepessegek.append(kepessegek)
                else:
                    raise TypeError("Az uj kepesseg str, vagy str lista kell legyen")
        else:
            raise TypeError("Az uj kepesseg str, vagy str lista kell legyen")

    def __iadd__(self, masik_hos: object, nev: str = "uj_hos", ero: int = 80) -> object:
        """
        ket szuperhos peldanyt ad ossze, egy ujat meg egy regit
        :param masik_hos: object: regi hos
        :param nev: str: uj hos nev
        :param ero: int: uj hos ero
        :return: uj szuperhos peldany
        """
        if isinstance(masik_hos, Szuperhos):
            uj_hos = Szuperhos(nev, ero)
            uj_hos.kepessegek = self.kepessegek + masik_hos.kepessegek
            return uj_hos
        raise TypeError("Szuperhos parameter arg-ja nem megfelelo tipusu")
