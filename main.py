from __future__ import division

from MyBeautifulSoup import MyBeautifulSoup

# https://www.codegrepper.com/code-examples/whatever/get+button+in+div+without+if+or+class+beautifulsoup
# https://www.python-lernen.de/bibliothek-urllib.htm
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html?highlight=findall#tag
# https://dev.to/joks84/playing-with-beautifulsoup-spiders-might-not-be-so-scary-after-all-4o81

if __name__ == '__main__':
    yy: MyBeautifulSoup = MyBeautifulSoup.instance().get_soup_by_url("https://news.google.com").get_div_by_class(
        "QmrVtf")
    for y in yy:
        print("Start")
        print(y.get_text())
        print("End")

    xx = MyBeautifulSoup.instance().get_soup_by_page("trump_verschwörung.html").get_div_by_class("g")
    for x in xx:
        print("Start")
        print(x.get_text())
        print("End")
