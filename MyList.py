import pandas as pd

from MyTag import MyTag


class MyList():
    """
    Die Klasse dient als Container für eine Liste von MyTag. Sie ist übersichtlicher und
    einfacher zu warten als eine von List vererbte und erweiterte Klasse.

    Sie bietet Fuktionalität für die gehaltene Liste als Ganzes an.
    """
    __myList: list[MyTag] = []
    """
    Die interne Liste mit Instanzen von MyTag
    """

    def __init__(self):
        """
        Der Konstruktor.
        """

        # Es ist wichtig, hier die interne Liste wirklich neu zu belegen
        # und self zu gebrauchen.
        self.__myList = []

    def items(self) -> list:
        """
        Die Funktion liefert die aktuell hinterlegte Liste mit Instanzen vom Typ MyTag. Sie
        kann mit for durchlaufen werden:

            for x in xx.items():
                print(x.get_text())

        zurück.

        :return:
            Eine Liste mit den aktuellen Instanzen von MyTag
        """
        return self.__myList

    def append(self, item: MyTag):
        """
        Fügt der internen Liste die übergebene Instanz von MyTag an

        :param item:
            Eine Instanz von MyTag, welche der Liste angefügt werden soll
        """
        self.__myList.append(item)

    def getDataFrame(self, header: str) -> pd.DataFrame:
        """
        Erstellt auf Basis der internen Liste von MyTag ein Pandas DataFrame und verwendet hierfür
        den Textcontent der MyTag Instanzen (x.get_text()).

        :param header:
            Ein String, welcher als Überschrift der Spalte des DataFrames verwendet wird.

        :return:
            Ein DataFrame mit den Textcontent aller MyTag Instanzen der internen Liste
        """
        tmpListe = []
        for itemX in self.__myList:
            tmpListe.append(itemX.get_text())

        dataFrame = pd.DataFrame(tmpListe, columns=[header])

        return dataFrame
