from __future__ import division

from urllib import request

from bs4 import BeautifulSoup


def get_soup_by_url(target_url: str, page_encoding="utf-8"):
    target_request = request.urlopen(target_url)
    raw_page = target_request.read().decode(page_encoding)
    return BeautifulSoup(raw_page, features="html.parser")


def get_soup_by_page(raw_html_page: str, page_encoding="utf-8"):
    raw_page = open(raw_html_page, encoding=page_encoding, mode="r").read().strip()
    return BeautifulSoup(raw_page, features="html.parser")

def get_div_by_class(source: BeautifulSoup, div_class: str):
    return source.find_all("div", attrs={"class": div_class})



# https://www.codegrepper.com/code-examples/whatever/get+button+in+div+without+if+or+class+beautifulsoup
# https://www.python-lernen.de/bibliothek-urllib.htm
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html?highlight=findall#tag
# https://dev.to/joks84/playing-with-beautifulsoup-spiders-might-not-be-so-scary-after-all-4o81


if __name__ == '__main__':
    # print(get_soup_by_url("https://news.google.com"))
    # print(get_soup_by_page("trump.txt"))

    # soup = get_soup_by_page("trump.txt")
    soup = get_soup_by_page("trump_verschwörung.html")
    #print(soup.prettify())

    #print( get_soup_by_page("trump_verschwörung.html"))

    #test= soup.find_all("div",attrs={"class":"g"})
    #test= soup.find_all("span",attrs={"class":"aCOpRe"})
    for x in get_div_by_class(soup, "g"):
        print("Start")
        print(x)
        print("End")



    #print(test)
    #g=0
    #class ="IsZvec"
    #print(soup.find_all("a"))
    # = soup.find_all("div")
    #print(r[0])
