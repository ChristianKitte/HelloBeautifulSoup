from __future__ import division

import sys
from urllib import request

import bs4.element
from bs4 import BeautifulSoup

from MyTag import MyTag


class MyBeautifulSoup(BeautifulSoup):
    """
    Bei dieser Klasse handelt es sich um eine Singleton, dessen Instanz nur über seine Klassenmethode
    instance() verfügbar ist.

    Die Klasse ermöglicht die einfache Erzeugung und Verwendung von Beautiful Soup. Hierfür wird über
    die Instanzmetheode eine Singletoninstanz erzeugt und über verschiedene Methoden die Verarbeitung
    von Quellen auf einfache Weise ermöglicht.

    Aktuell wird nur der Zugriff auf div Elemente unterstützt.
    """
    __currentBeautifulSoup = None
    """
    Private - Hält die intern verwendete Instanz der Klasse bs4.BeautifulSoup  
    """
    __instance = None
    """
    Private - hält die Instanz dieser (Singleton) Klasse  
    """

    def __init__(self):
        """
        Der Konstruktor dieser Klasse. Der direkte Aufruf dieser Methode führt zu einer Ausnahme vom Typ
        RuntimeError.
        """
        raise RuntimeError("Use classmethod instance()")

    @classmethod
    def instance(cls):
        """
        Liefert eine Instanz dieser (Singleton) Klasse zurück. Bei erstmaligen Aufruf wird eine neue Instanz
        erzeugt, ansonsten die vorhandene zurück gegeben.

        :return:
            Die einzige (Singleton) Instanz dieser Klasse
        """
        try:
            if cls.__instance is None:
                cls.__instance = cls.__new__(cls)
                cls.__currentBeautifulSoup = bs4.BeautifulSoup()
        except:
            return [].append(sys.exc_info()[0])

        return cls.__instance

    def get_soup_by_url(self, target_url: str, page_encoding="utf-8"):
        """
        Die Funktion erzeugt ein neues bs4.BeautifulSoup Objekt auf Basis der übergebenen URL und gibt
        sich selbst zurück. Ein zuvor erzeugtes Objekt wird hierdurch überschrieben.

        Das zurück gegebene Objekt ermöglicht Method Chain und somit die Umsetzung einer Fluent API.

        :param target_url:
            Die zu verwendende URL als String

        :param page_encoding:
            Optional die zu verwendende Encoding. Default ist utf-8

        :return:
            Die aktuelle Instanz dieser Klasse
        """
        try:
            target_request = request.urlopen(target_url)
            raw_page = target_request.read().decode(page_encoding)
            self.__currentBeautifulSoup = bs4.BeautifulSoup(raw_page, features="html.parser")
        except:
            return [].append(sys.exc_info()[0])

        return self

    def get_soup_by_page(self, raw_html_page: str, page_encoding="utf-8"):
        """
        Die Funktion erzeugt ein neues bs4.BeautifulSoup Objekt auf Basis einer übergebenen Datei mit validen HTML
        und gibt sich selbst zurück. Ein zuvor erzeugtes Objekt wird hierdurch überschrieben.

        Das zurück gegebene Objekt ermöglicht Method Chain und somit die Umsetzung einer Fluent API.

        :param raw_html_page:
            Der absolute Pfad zu einer Datei mit validen HTML, welche als Quelle verwendet werden soll

        :param page_encoding:
            Optional die zu verwendende Encoding. Default ist utf-8

        :return:
            Die aktuelle Instanz dieser Klasse
        """
        try:
            raw_page = open(raw_html_page, encoding=page_encoding, mode="r").read().strip()
            self.__currentBeautifulSoup = bs4.BeautifulSoup(raw_page, features="html.parser")
        except:
            return [].append(sys.exc_info()[0])

        return self

    def get_soup_by_string(self, raw_html_string: str):
        """
        Die Funktion erzeugt ein neues bs4.BeautifulSoup Objekt auf Basis eines übergebenen Textes mit validen HTML
        und gibt sich selbst zurück. Ein zuvor erzeugtes Objekt wird hierdurch überschrieben.

        Das zurück gegebene Objekt ermöglicht Method Chain und somit die Umsetzung einer Fluent API.

        :param raw_html_page:
            Der Text mit validen HTML, welcher als Quelle verwendet werden soll

        :param page_encoding:
            Optional die zu verwendende Encoding. Default ist utf-8

        :return:
            Die aktuelle Instanz dieser Klasse
        """
        try:
            self.__currentBeautifulSoup = bs4.BeautifulSoup(raw_html_string.strip(), features="html.parser")
        except:
            return [].append(sys.exc_info()[0])

        return self

    def get_div_by_class(self, div_class: str) -> list[MyTag]:
        """
        Extrahiert aus der zugrundeliegenden Quelle alle div Elemente anhand der übergebenen
        Klassenbezeichnung und liefert für jedes Ergebnis ein MyTag Element zurück.

        :param div_class:
            Ein String mit dem Namen der css Klasse, welche extrahiert werden soll

        :return:
            Eine Liste mit MyTag Instanzen
        """
        if self.__currentBeautifulSoup is not None:
            returnList: list[MyTag] = []

            try:
                for itemX in self.__currentBeautifulSoup.find_all("div", attrs={"class": div_class}):
                    # b = MyTag(itemX)
                    returnList.append(MyTag(itemX))
            except:
                return [].append(sys.exc_info()[0])

            return returnList
        else:
            return []

    def get_div_by_id(self, div_id: str) -> list[MyTag]:
        """
        Extrahiert aus der zugrundeliegenden Quelle ein div Elemente anhand der übergebenen
        ID und liefert hierfür ein MyTag Element zurück.

        :param div_class:
            Ein String mit der ID eines div Elementes, welches extrahiert werden soll

        :return:
            Eine Liste mit der MyTag Instanz
        """
        if self.__currentBeautifulSoup is not None:
            returnList: list[MyTag] = []

            try:
                for itemX in self.__currentBeautifulSoup.find_all("div", attrs={"id": div_id}):
                    returnList.append(MyTag(itemX))
            except:
                return [].append(sys.exc_info()[0])

            return returnList
        else:
            return []
