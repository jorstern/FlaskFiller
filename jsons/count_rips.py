import json
import re
from fractions import Fraction
        
with open('clean_data_fractions.json', 'r') as fr:
    data_dict = json.load(fr)
    
counter = 0


for drink in data_dict:
    rip = False
    drink_name = drink
    drink_ings_list = data_dict[drink]
    for ingredient in drink_ings_list:
        ing_name = ingredient[0]
        ing_amt = ingredient[1]
        if "" is ing_amt:
            rip = True
           
    if rip:
        counter += 1
print (counter)
