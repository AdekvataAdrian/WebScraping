from bs4 import BeautifulSoup               #glöm inte bort att importera  "python Packages" nere till vänster i pycharm
import requests

source = requests.get("https://www.di.se/bors/large-cap/").text           #DI:s largecapsida

soup = BeautifulSoup(source, "html.parser")

# Hitta tabellen med aktieinformation genom att söka efter tbody-elementet
IN = soup.find("tbody")

# Hitta alla rader (<tr>) i tabellen
rader = IN.find_all("tr")

# Loopa igenom rader och plocka ut namn, kurs och procentuell förändring
for rad in rader:
    data = rad.find_all("td")
    namn_element = data[0].find("a", href=True)
    kurs_element = data[1]
    procent_element = data[3]

    namn = namn_element.text.strip()
    kurs = kurs_element.text.strip()
    procent = procent_element.text.strip()

    print(f" {namn}, {kurs} kr , {procent} %")

