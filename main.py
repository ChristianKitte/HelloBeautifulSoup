from __future__ import division

import bs4.element
import requests
import re
from bs4 import BeautifulSoup

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    page = requests.get("https://www.web.de")
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")

        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            x= link.get("href")
            print(x)

