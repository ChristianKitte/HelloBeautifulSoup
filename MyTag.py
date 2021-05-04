from __future__ import division

import bs4.element


class MyTag:
    """
    Die Klasse MyTag Wrapped eine Instanz der Klasse bs4.element.Tag und macht einige seiner
    Methoden auf einfache Weise verfügbar. Hierbei fungiert sie als Container für die übergebene
    Instanz.
    """
    __currentTag = None
    """
    Private Eigenschaft __currentTag, hält die Instanz des übergebenen bs4.element.Tag       
    """

    def __init__(self, source: bs4.element.Tag):
        """
        Der Konstruktor der Klasse.

        :param source:
            Als Parameter wird das Element Tag übergeben, für welcher dieser Wrapper erzeugt wird
        """
        self.__currentTag = source

    def get_raw_tag(self) -> bs4.element.Tag:
        """
        Gibt das originale Tag Element von bs4 zurück, auf dem diese instanz basiert.

        :return:
            Das originale Tag Element als: bs4.element.Tag
        """
        return self.__currentTag

    def get_text(self) -> str:
        """
        Gibt den Textinhalt des zugrunde liegenden Tag Elementes zurück.

        :return:
            Der Textinhalt als String
        """
        currentText = ""

        if self.__currentTag != None:
            currentText = self.__currentTag.text

        return currentText
