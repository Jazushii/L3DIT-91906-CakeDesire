import tkinter as tk
from calculations import *

def open_calendar(content):
    create_title(content, f'{current_mth_name} {current_yr}')
    create_buttons(content)
    create_calendar(content, current_mth, current_yr)

frm_title = None
def create_title(content, date):
    global frm_title
    if frm_title is not None:
        frm_title.destroy()

    frm_title = tk.Frame(content, width=750, height=50)
    frm_title.place(x=50, y=0)
    frm_title.pack_propagate(False)

    lbl_title = tk.Label(frm_title, text=date, font=('Segoe Print', 16, 'bold'), bg=ORANGE)
    lbl_title.pack(fill='both', expand=True)

    title_border = tk.Frame(content, width=850, height=1, bd=1, relief='solid', bg='black')
    title_border.place(x=0, y=50)

def create_buttons(content):
    frm_left = tk.Frame(content, width=50, height=50)
    frm_left.place(x=0, y=0)
    frm_left.pack_propagate(False)
    btn_left = tk.Button(frm_left, text='<', font=('Arial', 16, 'bold'),
                         bg=ORANGE, command=lambda: calen_change(content, 'left'))
    btn_left.pack(fill='both', expand=True)
    
    frm_right = tk.Frame(content, width=50, height=50)
    frm_right.place(x=800, y=0)
    frm_right.pack_propagate(False)
    btn_right = tk.Button(frm_right, text='>', font=('Arial', 16, 'bold'),
                         bg=ORANGE, command=lambda: calen_change(content, 'right'))
    btn_right.pack(fill='both', expand=True)

calen_mth = current_mth
calen_yr = current_yr
def calen_change(content, type):
    global calen_mth, calen_yr

    if type == 'left':
        calen_mth -= 1
        if calen_mth == 0:
            calen_yr -= 1
            calen_mth = 12

    if type == 'right':
        calen_mth += 1
        if calen_mth == 13:
            calen_yr += 1
            calen_mth = 1

    create_title(content, f'{calendar.month_name[calen_mth]} {calen_yr}')
    create_calendar(content, calen_mth, calen_yr)

frm_calendar = None
def create_calendar(content, calen_mth, calen_yr):
    global frm_calendar
    if frm_calendar is not None:
        frm_calendar.destroy()

    frm_calendar = tk.Frame(content, width=850, height=430)
    frm_calendar.place(x=0, y=51)
    frm_calendar.pack_propagate(False)

    # week days
    for w in range(7):
        frame = tk.Frame(frm_calendar, width=120, height=40, bd=1.5, relief='groove')
        frame.place(x=5+120*w, y=0)
        frame.pack_propagate(False)

        label = tk.Label(frame, text=weekday_lbls[w], font=('Segoe Print', 12, 'bold'))
        label.pack(fill='both', expand=True)

    # first_day = first week day
    first_day, total_days = calendar.monthrange(calen_yr, calen_mth)
    print(first_day)

    prev_mth = calen_mth - 1
    prev_yr = calen_yr
    if prev_mth == 0:
        prev_yr -= 1
        prev_mth = 12
    prev_first_day, prev_total_days = calendar.monthrange(prev_yr, prev_mth)

    next_mth = calen_mth + 1
    next_yr = calen_yr
    if next_mth == 13:
        next_yr += 1
        next_mth = 1

    # day_track = the actual day number
    day_track = 1
    # day_num = the boxes of calendar (loop range)
    day_num = 0
    num_of_weeks = math.ceil((first_day + 1 + total_days) / 7)
    frm_height = math.floor(390 / num_of_weeks)

    # weeks
    for r in range(num_of_weeks):
        # week days
        for c in range(7):
            global frm_day
            frm_day = tk.Frame(frm_calendar, width=120, height=frm_height, bd=1.5, relief='groove')
            frm_day.place(x=5+120*c, y=41+frm_height*r)
            frm_day.pack_propagate(False)

            lbl_day = tk.Label(frm_day, font=('Arial', 12))

            # labeling the previous month's days
            if day_num < first_day:
                altered_prev_total_days = prev_total_days
                altered_prev_total_days -= ((first_day-1)-(1*day_num))

                lbl_day.config(text=altered_prev_total_days)
                lbl_day.pack()

                for ot in range(len(files)):
                    if (prev_yr == int(files[ot][1]['due_year']) and 
                        prev_mth == int(files[ot][1]['due_month']) and
                        altered_prev_total_days == int(files[ot][1]['due_day'])):

                        lbl_order = tk.Label(frm_day, text=f' {files[ot][1]['customer_name']} ',
                                             font=('Arial', 8))

                        if files[ot][1]['completed'] == True:
                            lbl_order.config(bg=GREEN)

                        if files[ot][1]['completed'] == False:
                            lbl_order.config(bg=ORANGE)
                
                        lbl_order.pack()

            # labeling the current month's days
            elif day_track <= total_days:
                lbl_day.config(text=day_track)
                lbl_day.pack()

                # current day tracker
                if (calen_mth == current_mth and
                    calen_yr == current_yr and
                    day_track == current_day):
                    frm_day.config(bg=PARA)
                    lbl_day.config(bg=PARA)

                # order tracker
                for ot in range(len(files)):
                    if (calen_yr == int(files[ot][1]['due_year']) and 
                        calen_mth == int(files[ot][1]['due_month']) and
                        day_track == int(files[ot][1]['due_day'])):

                        lbl_order = tk.Label(frm_day, text=f' {files[ot][1]['customer_name']} ',
                                             font=('Arial', 8))

                        if files[ot][1]['completed'] == True:
                            lbl_order.config(bg=GREEN)

                        if files[ot][1]['completed'] == False:
                            lbl_order.config(bg=ORANGE)

                        lbl_order.pack()

                day_track += 1

            # labelling the next month's days
            else:
                lbl_day.config(text=day_track - total_days)
                lbl_day.pack()

                for ot in range(len(files)):
                    if (next_yr == int(files[ot][1]['due_year']) and 
                        next_mth == int(files[ot][1]['due_month']) and
                        (day_track - total_days) == int(files[ot][1]['due_day'])):
            
                        lbl_order = tk.Label(frm_day, text=f' {files[ot][1]['customer_name']} ',
                                             font=('Arial', 8))
                
                        if files[ot][1]['completed'] == True:
                            lbl_order.config(bg=GREEN)
                
                        if files[ot][1]['completed'] == False:
                            lbl_order.config(bg=ORANGE)
                
                        lbl_order.pack()

                day_track += 1

            day_num += 1