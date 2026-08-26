import json
import os
import math
import datetime
import calendar

path = os.getcwd()
files = []
def scan_files():
    files.clear()
    for f in os.listdir(path):
        if f.endswith('.json'):
            if f != 'inventory_stock.json':
                with open(f, 'r') as file:
                    order = json.load(file)
                
                files.append((f, order))

    files.sort(key=lambda x:(int(x[1]['due_year']),
                             int(x[1]['due_month']),
                             int(x[1]['due_day'])))

# INVENTORY INTERFACE
with open('inventory_stock.json', 'r') as file:
    stock = json.load(file)


# INVENTORY INTERFACE
ratio_formula = {'eggs': 4, 'milk': 160, 'oil': 80, 'butter': 80, 'flour': 200, 'sugar': 200, 'salt': 0.25,
                       'baking_powder': 1.5, 'vanilla_extract': 1, 'cocoa_powder': 40, 'ube_extract': 2}

ingredients_lbls = ['Eggs', 'ml of Milk', 'ml of Cooking Oil', 'g of Butter', 'g of Flour', 'g of Sugar', 'tsp of Salt',
                    'tsp of\nBaking Powder', 'tsp of\nVanilla Extract', 'g of\nCocoa Powder', 'tsp of\nUbe Extract']

stock_lbls = ['Eggs:', 'Milk (ml):', 'Oil (ml):', 'Butter (g):', 'Flour (g):', 'Sugar (g):', 'Salt (tsp):', 
              'Baking\nPowder (tsp):', 'Vanilla\nExtract (tsp):', 'Cocoa\nPowder (tsp):', 'Ube\nExtract (tsp):']
stock_ents = []
stock_frame = None
stock_save_lbls = ['eggs', 'milk', 'oil', 'butter', 'flour', 'sugar', 'salt',
                    'baking_powder', 'vanilla_extract', 'cocoa_powder', 'ube_extract']

# ORDERLIST INTERFACE
detail_save_lbls = ['customer_name', 'cake_flavour', 'due_day', 'due_month',
                   'due_year', 'cake_colours', 'cake_type','cake_shape']

tier_save_lbls = ['layer', 'size_a', 'size_b']

months = ['', 'January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# CALENDAR INTERFACE
today = datetime.date.today()

current_yr = today.year
current_mth = today.month
current_day = today.day

current_mth_name = calendar.month_name[current_mth]

first_day, total_days = calendar.monthrange(current_yr, current_mth)
prev_irst_day, prev_total_days = calendar.monthrange(current_yr, current_mth-1)

day_track = 1
day_num = 0
num_of_weeks = math.ceil((first_day + 1 + total_days) / 7)
frm_height = math.floor(390 / num_of_weeks)

weekday_lbls = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

scan_files()
for i in range(len(files)):
    if int(files[i][1]['due_year']) >= current_yr:
        if int(files[i][1]['due_month']) >= current_mth:
            if int(files[i][1]['due_day']) >= current_day:
                print('day check')
                if files[i][1]['completed'] == False:
                    print('completed check')
                    incoming_order = files[i][0].removesuffix('.json')
                    print(files[i][0])

                    break
