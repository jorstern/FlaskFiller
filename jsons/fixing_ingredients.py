import json
import re
from fractions import Fraction
        
with open('clean_data.json', 'r') as fr:
    data_dict = json.load(fr)

def go_through_list(drink_ings_list):
    for ingredient in drink_ings_list:
        ing_name = ingredient[0]
        ing_amt = ingredient[1]
        

for drink in data_dict:
    drink_name = drink
    drink_ings_list = data_dict[drink]
    try:
        go_through_list(drink_ings_list)
    except:
        print ("Failed on: " + drink)
        
data = json.dumps(data_dict, indent=4, separators=(',', ': '))
with open("clean_data_fractions.json", "w") as fw:
    fw.write(data)
