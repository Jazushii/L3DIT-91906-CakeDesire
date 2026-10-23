import tkinter as tk
from calculations import *

def open_calendar(content):
    create_title(content, f'{current_mth_name} {current_yr}')
    create_buttons(content)
    create_calendar(content)

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
    create_calendar(content)

frm_calendar = None
def create_calendar(content):
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

    # weeks
    for r in range(num_of_weeks):
        # week days
        for c in range(7):
            frame = tk.Frame(frm_calendar, width=120, height=frm_height, bd=1.5, relief='groove')
            frame.place(x=5+120*c, y=41+frm_height*r)
            frame.pack_propagate(False)

            import calculations

            day = tk.Label(frame, font=('Arial', 12))

            # labeling the previous month's days
            if calculations.day_num < calculations.first_day:
                altered_prev_total_days = calculations.prev_total_days
                altered_prev_total_days -= ((calculations.first_day-1)-(1*calculations.day_num))

                day.config(text=altered_prev_total_days)

            # labelling the next month's days
            if calculations.day_track > calculations.total_days:
                day.config(text=calculations.day_track-calculations.total_days)
                calculations.day_track += 1

            # labeling the current month's days
            if calculations.day_num >= calculations.first_day and calculations.day_track <= calculations.total_days:
                day.config(text=calculations.day_track)

                # current day tracker
                if calculations.day_track == calculations.current_day:
                    frame.config(bg=PARA)
                    day.config(bg=PARA)

                calculations.day_track += 1

            day.pack()
            calculations.day_num += 1