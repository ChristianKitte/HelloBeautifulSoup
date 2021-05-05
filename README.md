# EA 03 - Python for Data Science Exercise
### Data Science SS 21
### Christian Kitte 

Bei diesem Code handelt es sich um eine Bibliothek, um den Einsatz der Bibliothek “**BeautifulSoup**” alias “[**bs4**](https://pypi.org/project/beautifulsoup4/)" 
zu vereinfachen und den Einstieg leichter zu gestalten.

Bei der sporadischen Beschäftigung mit **bs4** fiel mir immer wieder auf, dass deren Syntax gerade zu Anfang, wenn die Quelle selbst 
geladen werden muss, etwas umständlich ist. Dies verbessert auch nicht wirklich den Einstieg.

Daher habe ich gerade für den Einstieg und hier speziell für ***Webseiten, lokale Seite und Texte*** den Anfang einer kleinen **DSL** als 
**Floating API** geschrieben. Bei den Umfang von **bs4** und den Möglichkeiten deckt sie natürlich bei weitem nicht das gesamte Spektrum, 
sondern halt nur das einfache Laden und wenige Funktionen ab. Es handelt sich hier also um ein absolutes **Grundgerüst**.

In dem zugehörigen Pythonprojekt habe ich in der **Main** Methode meine kleine Bibliothek getestet und etwas Mustercode geschrieben, der 
zeigt, wie sie verwendet werden kann. Ein Beispiel, mit dem eine Seite geöffnet und der Inhalt aller div-Tags der Klasse “QmrVtf” 
ausgegeben wird, ist hier beispielsweise:

 xx = MyBeautifulSoup.instance().get_soup_by_page("trump_verschwörung.html").get_div_by_class("g")
    for x in xx.items():
        print("Start - KLASSEN basiert")
        print(x.get_text())
        print("End - KLASSEN basiert")

    # Umwandeln in ein DataFrame und Ausgabe als .csv Datei
    dfx = xx.getDataFrame("Inhalt XX")
    dfx.to_csv("xx.csv")

Dies Beispiel liest eine gespeicherte Seite aus und extrahiert alle DIV-Blöcke mit dem Klassenattribut “g” und gibt diese in die 
Konsole aus. Anschließend wird ein Panda DataFrame erzeugt und dessen Inhalt als CSV Datei exportiert (siehe hierzu die CSV-Dateien xx, yy 
sowie zz).

Durch die Möglichkeit, sich einfach ein Panda DataFrame zurückgeben zu lassen, stehen alle Möglichkeiten dieses Objektes einfach 
zur Verfügung.

Die restliche Funktionalität und deren Umsetzung sollte sich aus der im Code eingefügten Dokumentierung ergeben. Die zur Ausführung 
benötigten Bibliotheken sind in der **requirements.txt** verfügbar. Als Basis diente **Python 3.9**.
