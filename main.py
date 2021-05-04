from __future__ import division

from MyBeautifulSoup import MyBeautifulSoup

if __name__ == '__main__':
    """
    Die Einstiegsroutine zum Testprogramm, sofern sie direkt aufgerufen wird. Sie dient nur dem Test
    der Hilfsklassen MyBeautifulSoup und MyTag  
    """

    # Beispiel für die Verwendung der Klasse auf Basis einer übergebenen URL. Die hier verwendete
    # News Seite verwendet die Klasse QmrVtf.
    yy: MyBeautifulSoup = MyBeautifulSoup.instance().get_soup_by_url("https://news.google.com").get_div_by_class(
        "QmrVtf")
    for y in yy:
        print("Start")
        print(y.get_text())
        print("End")

    # Beispiel für die Verwendung anhand einer übergebenen Datei, hier einer Googlesuche.
    # Google verwendet die Klasse g für ihre Ergebnisse.
    xx = MyBeautifulSoup.instance().get_soup_by_page("trump_verschwörung.html").get_div_by_class("g")
    for x in xx:
        print("Start")
        print(x.get_text())
        print("End")
