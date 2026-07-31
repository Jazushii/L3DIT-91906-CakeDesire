import tkinter as tk
from calculations import *

def open_calendar(content):
    create_title(content)
    create_calendar(content)

def create_title(content):
    frm_title = tk.Frame(content, width=850, height=50)
    frm_title.place(x=0, y=0)
    frm_title.pack_propagate(False)

    lbl_title = tk.Label(frm_title, text=f'{current_mth_name} {current_yr}', font=('Segoe Print', 16, 'bold'), bg='#FFB253')
    lbl_title.pack(fill='both', expand=True)

    title_border = tk.Frame(content, width=850, height=1, bd=1, relief='solid', bg='black')
    title_border.place(x=0, y=50)

def create_calendar(content):
    # week days
    for w in range(7):
        frame = tk.Frame(content, width=120, height=40, bd=1.5, relief='groove')
        frame.place(x=5+120*w, y=51)
        frame.pack_propagate(False)

        label = tk.Label(frame, text=weekday_lbls[w], font=('Segoe Print', 12, 'bold'))
        label.pack(fill='both', expand=True)

    # weeks
    for r in range(num_of_weeks):
        # week days
        for c in range(7):
            frame = tk.Frame(content, width=120, height=frm_height, bd=1.5, relief='groove')
            frame.place(x=5+120*c, y=91+frm_height*r)
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
                calculations.day_track += 1

            day.pack()
            calculations.day_num += 1