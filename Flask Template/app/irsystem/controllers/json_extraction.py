import json
import pickle
import numpy as np

with open('ingredients.json', 'r') as fr:
    ingr_list = json.load(fr)

with open('clean_data_revised_names.json', 'r') as fr:
    drink_list = json.load(fr)
ingr_list = [x.lower().encode('utf-8') for x in ingr_list]

#create helper methods and arrays
ingr_to_num = {}
i=0
for ingr in ingr_list:
    ingr_to_num[ingr] = i
    i=i+1

drink_to_num = {}
num_to_drink = {}
j=0
for k,v in drink_list.items():
    drink_to_num[k] = j
    num_to_drink[j] = k
    j=j+1

#let's make the drink by ingredients numpy array, so we can eventually pickle it
drink_ingr = np.zeros((len(drink_to_num), len(ingr_to_num)))
for i in range(len(drink_to_num)):
    curr_ingredients = drink_list[num_to_drink[i]]
    #for j in range(len(ingr_to_num)):
    for ingredient in curr_ingredients:
        num_ingredient = ingr_to_num[ingredient[0].lower().encode('utf-8')]
        drink_ingr[i][num_ingredient] = 1
print(drink_ingr)

def drink_to_index(dr):
    return drink_to_num[dr]
def index_to_drink(num):
    return num_to_drink[num]

def ingredient_to_index(ingredient_str):
    return ingr_to_num[ingredient_str.lower().encode('utf-8')]
def number_list_of_drinks(ing_str_lst):
    newlst = []
    for ingr in ing_str_lst:
        newlst.append(ingredient_to_index(ingr))
    return newlst

def get_ingredients_for_drink(drink_num, drink_lst):
    #print(drink_num)
    curr_ingredients = drink_lst[index_to_drink(drink_num).lower().encode('utf-8')]
    final = []
    for ing in curr_ingredients:
        final.append(ingredient_to_index(ing[0]))
    return final

#returns a numpy array of 1 by size of drink_list. each entry is the jaccard similarity between the user input and drink
def drink_jaccard_sim(user_ingredients_lst):
    #print(drink_lst)
    drink_lst = drink_list
    final_mat = np.zeros(len(drink_lst))
    #cat1 will be the user set. It should just have a list of numbers that correspond to drinks
    cat1 = set(number_list_of_drinks(user_ingredients_lst))
    for i in range(len(drink_lst)):
        #cat2 will be the ingredients of each individual drink
        cat2 = set(get_ingredients_for_drink(i, drink_lst))
        #do the jaccard
        intersect = len(set.intersection(cat1, cat2))
        union = len(set.union(cat1, cat2))
        final_mat[i] = intersect/(union+1)
    #print(np.sum(final_mat))
    return final_mat

def get_top_k_drinks(lst, k):
    #lst should have a list of ranked values, just need to do an argsort for the best ones
    sorted_lst = lst.argsort()[-k:][::-1]
    #print(sorted_lst)
    top_drinks = []
    for drink_num in sorted_lst:
        top_drinks.append((index_to_drink(drink_num), lst[drink_num]))
    #print(top_drinks)
    return top_drinks
