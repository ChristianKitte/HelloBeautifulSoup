from __future__ import division

import sys
from urllib import request

import bs4.element
from bs4 import BeautifulSoup

from MyTag import MyTag


class MyBeautifulSoup(BeautifulSoup):
    __currentBeautifulSoup = None
    __instance = None

    def __init__(self):
        raise RuntimeError("Use classmethod instance()")

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
            cls.__currentBeautifulSoup = bs4.BeautifulSoup()
        return cls.__instance

    def get_soup_by_url(self, target_url: str, page_encoding="utf-8"):
        target_request = request.urlopen(target_url)
        raw_page = target_request.read().decode(page_encoding)
        self.__currentBeautifulSoup = bs4.BeautifulSoup(raw_page, features="html.parser")
        return self

    def get_soup_by_page(self, raw_html_page: str, page_encoding="utf-8"):
        raw_page = open(raw_html_page, encoding=page_encoding, mode="r").read().strip()
        self.__currentBeautifulSoup = bs4.BeautifulSoup(raw_page, features="html.parser")
        return self

    def get_soup_by_string(self, raw_html_string: str):
        self.__currentBeautifulSoup = bs4.BeautifulSoup(raw_html_string.strip(), features="html.parser")
        return self

    def get_div_by_class(self, div_class: str) -> list[MyTag]:
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
