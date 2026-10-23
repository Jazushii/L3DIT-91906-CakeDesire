import json
import os
import math
import datetime
import calendar

# Colours
MAIN = '#FFD333'
SUB = '#FFC957'
PARA = '#FEF8A0'
ORANGE = '#FFB253'
RED = '#FF5D55'
GREEN = '#72BB53'

# File Scanning
path = os.getcwd()
files = []
def scan_files():
    files.clear()
    for f in os.listdir(path):
        if f.endswith('.json'):
            if f != 'inventory_stock.json':
                if f != '.json':
                    with open(f, 'r') as file:
                        order = json.load(file)
                    
                    files.append((f, order))

    files.sort(key=lambda x:(int(x[1]['due_year']),
                             int(x[1]['due_month']),
                             int(x[1]['due_day'])))

    if len(files) == 0:
        for f in os.listdir(path):
            if f == '.json':
                with open(f, 'r') as file:
                    order = json.load(file)
                                    
                    files.append((f, order))

# INVENTORY INTERFACE
update_inventory = 0

with open('inventory_stock.json', 'r') as file:
    stock = json.load(file)

# INVENTORY INTERFACE
ratio_formula = {'eggs': 4, 'milk': 160, 'oil': 80, 'butter': 80, 'flour': 200, 'sugar': 200,
                       'baking_powder': 1.5, 'vanilla_extract': 1, 'cocoa_powder': 40, 'ube_extract': 2}

stock_lbls = ['Eggs:', 'Milk (ml):', 'Oil (ml):', 'Butter (g):', 'Flour (g):', 'Sugar (g):', 
              'Baking\nPowder (tsp):', 'Vanilla\nExtract (tsp):', 'Cocoa\nPowder (tsp):', 'Ube\nExtract (tsp):']
stock_ents = []
stock_frame = None
stock_save_lbls = ['eggs', 'milk', 'oil', 'butter', 'flour', 'sugar',
                    'baking_powder', 'vanilla_extract', 'cocoa_powder', 'ube_extract']

# ORDERLIST INTERFACE
update_orderlist = 0

dd_placeholders = ['dd', 'mm', 'yyyy']

detail_save_lbls = ['customer_name', 'cake_flavour', 'due_day', 'due_month',
                   'due_year', 'cake_colours', 'cake_type','cake_shape']

tier_save_lbls = ['layer', 'size_a', 'size_b']

months = ['', 'January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# CALENDAR INTERFACE
update_calendar = 0
today = datetime.date.today()

current_yr = today.year
current_mth = today.month
current_day = today.day

current_mth_name = calendar.month_name[current_mth]

weekday_lbls = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

order_date = today + datetime.timedelta(weeks=2)
order_yr = order_date.year
order_mth = order_date.month
order_day = order_date.day

def get_incoming_order():
    global incoming_order
    scan_files()
    if files[0][0] == '.json':
        incoming_order = files[0][0].removesuffix('.json')

    else:
        for i in range(len(files)):
            if int(files[i][1]['due_year']) >= current_yr:
                if int(files[i][1]['due_month']) >= current_mth:
                    if int(files[i][1]['due_month']) == current_mth:
                        if int(files[i][1]['due_day']) >= current_day:
                            if files[i][1]['completed'] == False:
                                print('completed check')
                                incoming_order = files[i][0].removesuffix('.json')

                                break
                    else:
                        if int(files[i][1]['due_day']) >= 1:
                            if files[i][1]['completed'] == False:
                                print('completed check')
                                incoming_order = files[i][0].removesuffix('.json')
                        
                                break
