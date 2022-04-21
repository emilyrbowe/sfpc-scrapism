import requests
from bs4 import BeautifulSoup

urls = ["https://wiki.openstreetmap.org/wiki/Organised_Editing/Activities/Amazon"]

for url in urls:
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    print(soup.find_all("mw-headline"))
