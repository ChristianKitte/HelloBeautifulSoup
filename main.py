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
    for y in yy.items():
        print("Start - KLASSEN basiert")
        print(y.get_text())
        print("End - KLASSEN basiert")

    # Umwandeln in ein DataFrame und Ausgabe als .csv Datei
    dfy = yy.getDataFrame("Inhalt YY")
    dfy.to_csv("yy.csv")

    # Beispiel für die Verwendung der Klasse auf Basis anhand einer übergebenen Datei, hier einer Googlesuche.
    # Google verwendet die Klasse g für ihre Ergebnisse.
    xx = MyBeautifulSoup.instance().get_soup_by_page("trump_verschwörung.html").get_div_by_class("g")
    for x in xx.items():
        print("Start - KLASSEN basiert")
        print(x.get_text())
        print("End - KLASSEN basiert")

    # Umwandeln in ein DataFrame und Ausgabe als .csv Datei
    dfx = xx.getDataFrame("Inhalt XX")
    dfx.to_csv("xx.csv")

    # Beispiel für die Verwendung einer ID anhand einer übergebenen Datei, hier einer Googlesuche.
    # Google verwendet die Klasse g für ihre Ergebnisse.
    zz = MyBeautifulSoup.instance().get_soup_by_page("trump_verschwörung.html").get_div_by_id("pTwnEc")
    for z in zz.items():
        print("Start - ID basiert")
        print(z.get_text())
        print("End - ID basiert")

    # Umwandeln in ein DataFrame und Ausgabe als .csv Datei
    dfz = zz.getDataFrame("Inhalt ZZ")
    dfz.to_csv("zz.csv")
