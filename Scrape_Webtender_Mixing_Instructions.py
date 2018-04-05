import re
import requests 
from urllib.parse import urljoin
from bs4 import BeautifulSoup as BS

last_drink_number = 6217

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0', 'Accept-Encoding': 'identity'}
base_url = "https://www.webtender.com/cgi-bin/printdrink?"

drinks_dict = {}

def getSoup(url):
    html = requests.post(url, headers=headers)
    soup = BS(html.content, "html.parser")
    return soup

for i in range(last_drink_number):
    try:
        URL_new = base_url + str(i+1)
        soup = getSoup(URL_new)
        text = soup.findAll("p")[-1].get_text()
        title = soup.find("h1").get_text()
        drinks_dict[title] = text
        print(i+1)
    except:
        print("Failed on" + str(i+1))

import json
data = json.dumps(drinks_dict, indent=4, separators=(',', ': '))
with open("alcoholic_cocktails_webtender_mixing.json", "w") as f:
    f.write(data)
