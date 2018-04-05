import re
import requests 
from urllib.parse import urljoin
from bs4 import BeautifulSoup as BS

last_drink_number = 6217

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0', 'Accept-Encoding': 'identity'}
base_url = "https://www.webtender.com/db/drink/"

drinks_dict = {}

def getSoup(url):
    html = requests.post(url, headers=headers)
    soup = BS(html.content, "html.parser")
    return soup

def get_amts_ings(ings_list):
    final_list = list()
    for ing in ings:
        name = ing.get_text()
        try:
            final_list.append((name, ing.previous.strip()))
        except:
            final_list.append((name, "")) 
    return final_list

for i in range(last_drink_number):
    URL_new = base_url + str(i+1)
    soup = getSoup(URL_new)
    table = soup.find()
    ings = table.findAll("a", {"class": "ingr"})
    ingreds = get_amts_ings(ings)
    title_line = table.find("h1")
    title = title_line.get_text()
    drinks_dict[title] = ingreds
    print(i+1)
    
import json
data = json.dumps(drinks_dict, indent=4, separators=(',', ': '))
with open("alcoholic_cocktails_webtender_ingredients.json", "w") as f:
    f.write(data)
