from __future__ import division

import bs4.element


class MyTag:
    __currentTag = None

    def __init__(self, source: bs4.element.Tag):
        self.__currentTag = source

    def get_raw_tag(self) -> bs4.element.Tag:
        return self.__currentTag

    def get_text(self) -> str:
        currentText = self.__currentTag.text
        return currentText

# https://dev.to/joks84/playing-with-beautifulsoup-spiders-might-not-be-so-scary-after-all-4o81
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html?highlight=findall#tag
# https://www.python-lernen.de/attribute-und-methoden-ueberschreiben.htm
# https://python-patterns.guide/gang-of-four/singleton/
# https://www.codegrepper.com/code-examples/whatever/get+button+in+div+without+if+or+class+beautifulsoup
# https://www.data-science-architect.de/methoden-in-python/#static
# https://docs.python.org/3/tutorial/errors.html