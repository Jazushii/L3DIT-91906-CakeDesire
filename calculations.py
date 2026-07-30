import json
import datetime
import calendar

today = datetime.date.today()

current_yr = today.year
current_mth = today.month
current_day = today.day

first_day, num_days = calendar.monthrange(current_yr, current_mth)