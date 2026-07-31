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