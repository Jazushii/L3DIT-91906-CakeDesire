import tkinter as tk
import json
import os

# Task 2.2
def open_orderlist(content):
    create_details(content)
    create_decor(content)
    load_order(content, 'Jae')
    create_confirm_btn(content)
    create_new_order_btn(content)
    create_order_list(content)
    check_files()

dd_placeholders = ['dd', 'mm', 'yyyy']

def delete_placeholder(event, d, error):
    if error == False:
        if detail_ents[d].get() == dd_placeholders[d-2]:
            detail_ents[d].delete(0, 'end')
            detail_ents[d].config(fg='black')
    elif error == True:
        if detail_ents[d].get() == dd_placeholders[d-2]:
            detail_ents[d].delete(0, 'end')
            detail_ents[d].config(fg='black')

def create_placeholder(event, d):
    if detail_ents[d].get() == '':
        detail_ents[d].insert(0, dd_placeholders[d-2])
        detail_ents[d].config(fg='gray')

# Task 2.2
def create_details(content):
    # Task 2.2 Details & Entry Boxes
    detail_ent_lbls = [
        'Customer Name:',
        'Cake Flavour:',
        'Due Date:',
        '',
        '',
        'Cake Colour/s:',
        'Cake Type:',
        'Cake Shape:'
    ]

    global detail_ents
    detail_ents = []

    detail_num = 0

    for dr in range(3):
        for dc in range(2):
            frame = tk.Frame(content, width=265, height=62, bd=1.5, relief='groove')
            frame.grid(row=dr, column=dc)
            frame.place(x=20+(dc*275), y=20+(dr*70))
            frame.pack_propagate(False)
            label = tk.Label(frame, text=detail_ent_lbls[detail_num], font=('Segoe Print', 12))
            label.place(x=5, y=-1)
            if detail_num == 2:
                frm_dd = tk.Frame(frame, width=200, height=30)
                frm_dd.place(x=5, y=30)

                for dd in range(3):
                    detail_ents.append(tk.Entry(frm_dd, width=6, font=('Arial', 12), bg='white'))
                    detail_ents[detail_num].pack(side='left')
                    detail_ents[detail_num].bind('<FocusIn>', lambda event,
                                                 d=detail_num: delete_placeholder(event, d, False))
                    detail_ents[detail_num].bind('<FocusOut>', lambda event,
                                                 d=detail_num: create_placeholder(event, d))
                    detail_num += 1

                frm_icon = tk.Frame(frame, width=21, height=21, bg='#FEF8A0')
                frm_icon.place(x=167, y=30)
                frm_icon.pack_propagate(False)
                icon = tk.PhotoImage(file='date-icon.png')
                img_icon = tk.Label(frm_icon, image=icon, bg='#FEF8A0')
                img_icon.image = icon
                img_icon.pack(fill="both", expand=True)
            else:
                detail_ents.append(tk.Entry(frame, width=20, font=('Arial', 12), bg='#FEF8A0'))
                detail_ents[detail_num].place(x=5, y=30)
                detail_num += 1

# Task 2.3
frm_tiers = None
def create_tiers_table(content, rnum):
    global frm_tiers
    if frm_tiers is not None:
        frm_tiers.destroy()

    frm_tiers = tk.Frame(content, width=265, height=106+(int(rnum)*25), bd=1.5, relief='groove')
    frm_tiers.place(x=20, y=230)
    frm_tiers.pack_propagate(False)
    lbl_tiers = tk.Label(frm_tiers, text='No. of Cake Tiers:', font=('Segoe Print', 12))
    lbl_tiers.place(x=5, y=-1)
    global ent_tiers
    ent_tiers = tk.Entry(frm_tiers, width=2, font=('Arial', 12))
    ent_tiers.place(x=5, y=30)
    ent_tiers.insert(0, rnum)

    # Task 2.3.2 Tiers Table
    # List of labels for the table
    tier_ent_lbls = [
        'Tier:',
        'Layers:',
        'Size (In.):',
        ''
    ]

    global tier_ents
    tier_ents = []

    tier_num = 0

    for tr in range(int(rnum)):
        for tc in range(3):
            if tr == 0:
                frm_lbl = tk.Frame(frm_tiers, width=84, height=38, bd=1.5, relief='groove', bg='#FEF8A0')
                frm_lbl.grid(row=0, column=tc)
                frm_lbl.place(x=4+(tc*84), y=60)
                frm_lbl.pack_propagate(False)
                lbl = tk.Label(frm_lbl, text=tier_ent_lbls[tc], font=('Segoe Print', 12), bg='#FEF8A0')
                lbl.place(x=0, y=-1)

            frame = tk.Frame(frm_tiers, width=84, height=25)
            frame.grid(row=tr+1, column=tc)
            frame.place(x=4+(tc*84), y=98+((tr)*25))
            frame.pack_propagate(False)
            if tc == 0:
                lbl_tier = tk.Label(frame, text=f'Tier {tr+1}', font=('Segoe Print', 12), bd=1.5, relief='groove')
                lbl_tier.pack(fill='both', expand=True)
            elif tc == 1: 
                tier_ents.append(tk.Entry(frame, font=('Arial', 12), bd=1.5, relief='groove'))
                tier_ents[tier_num].pack(fill='both', expand=True)
                tier_num += 1
            elif tc == 2:
                for s in range(2):
                    frm_size = tk.Frame(frame, width=42, height=25)
                    frm_size.place(x=42*s, y=0)
                    frm_size.pack_propagate(False)
                    tier_ents.append(tk.Entry(frm_size, font=('Arial', 12), bd=1.5, relief='groove'))
                    tier_ents[tier_num].pack(fill='both', expand=True)
                    tier_num += 1

    # Task 2.3.1
    frm_btn_tiers = tk.Frame(frm_tiers, width=22, height=22)
    frm_btn_tiers.place(x=27, y=30)
    frm_btn_tiers.pack_propagate(False)
    btn_tiers = tk.Button(frm_btn_tiers, text='▼', font=('Arial', 10, 'bold'), bg='#FEF8A0',
                          activebackground='#FEF8A0', command=lambda: create_tiers_table(content, ent_tiers.get()))
    btn_tiers.pack(fill='both', expand=True)

detail_save_lbls = ['customer_name',
                    'cake_flavour',
                    'due_day',
                   'due_month',
                   'due_year',
                   'cake_colours',
                   'cake_type',
                   'cake_shape'
                   ]

tier_save_lbls = ['layer', 'size_a', 'size_b']

def load_order(content, file_name):
    print(file_name)
    with open(f'{file_name}.json', 'r') as file:
        order = json.load(file)
        for dl in range(8):
            detail_ents[dl].delete(0, 'end')
            detail_ents[dl].insert(0, order[detail_save_lbls[dl]])

        create_tiers_table(content, int(order['tier_num']))

        tload = 0
        for tnum in range(int(order['tier_num'])):
            for tl in range(3):
                tier_ents[tload].insert(0, order[f'tier{tnum+1}_{tier_save_lbls[tl]}'])
                tload += 1
        
        txt_decor.delete(1.0, 'end')
        txt_decor.insert(1.0, order['decor'])

# Task 2.3.1 & 2.3.3 Decoration
def create_decor(content):
    # Task 2.3.1
    frm_decor = tk.Frame(content, width=265, height=201, bd=1.5, relief='groove')
    frm_decor.place(x=295, y=230)
    frm_decor.pack_propagate(False)
    lbl_decor = tk.Label(frm_decor, text='Decorations/Toppings:', font=('Segoe Print', 12))
    lbl_decor.place(x=5, y=-1)

    # Task 2.3.3
    frm_txt_decor = tk.Frame(frm_decor, width=250, height=160)
    frm_txt_decor.place(x=5, y=30)
    frm_txt_decor.pack_propagate(False)
    global txt_decor
    txt_decor = tk.Text(frm_txt_decor, font=('Arial', 12), bg='#FEF8A0')
    txt_decor.pack(fill='both', expand=True)

# Task 2.4.1 File Set-up
def save_order():

    order_details = {}
        
    # Saving Details

    for dsave in range(8):
        if 1 < dsave < 4:
            if len(detail_ents[dsave].get()) == 1:
                    order_details[detail_save_lbls[dsave]] = f'0{detail_ents[dsave].get()}'
            else:
                order_details[detail_save_lbls[dsave]] = detail_ents[dsave].get()
        else: 
            order_details[detail_save_lbls[dsave]] = detail_ents[dsave].get()

    # Saving Tiers Table
    tsave = 0

    order_details['tier_num'] = ent_tiers.get()

    for tnum in range(int(ent_tiers.get())):
        for td in range(3):
            order_details[f'tier{tnum+1}_{tier_save_lbls[td]}'] = tier_ents[tsave].get()
            tsave += 1

    # Saving Decorations / Toppings
    order_details['decor'] = txt_decor.get("1.0", tk.END).rstrip('\n')

    order_details['completed'] = False

    with open(f'{detail_ents[0].get()}.json', 'w') as f:
        json.dump(order_details, f, indent=4)

    print('Saving...')
    root.destroy()

# Task 2.4.3 Error Prevention
def error_prev():
    global has_error
    global d_errors
    global t_errors

    has_error = False
    d_errors = {}
    t_errors = {}

    # searching for errors in details
    for de in range(8):
        # checking for blank entries
        if detail_ents[de].get() == '' or detail_ents[de].get() == '*':
            has_error = True
            d_errors[f'blank{de}'] = de

        # checking for digit entries for 0, 1, 5, 6, 7
        if de < 2 or de > 4:
            dsum_digit = sum(a.isdigit() for a in detail_ents[de].get())
            if dsum_digit != 0:
                has_error = True
                d_errors[f'digit{de}'] = de

        # checking for alpha entries for 2, 3, 4
        if 1 < de < 5:
            dsum_alpha = sum(a.isalpha() for a in detail_ents[de].get())
            if dsum_alpha != 0:
                has_error = True
                d_errors[f'alpha{de}'] = de

    # searching for errors in tiers
    t = 0
    for tnum in range(int(ent_tiers.get())):
        for te in range(3):
            # checking for blank entries
            if tier_ents[t].get() == '' or tier_ents[t].get() == '*':
                has_error = True
                t_errors[f'blank{t}'] = t
                
            # checking for alpha entires
            tsum_alpha = sum(a.isalpha() for a in tier_ents[t].get())
            if tsum_alpha != 0:
                has_error = True
                t_errors[f'alpha{t}'] = t
                
            t += 1

def resolve_error(content):
    def delete_required(event, type, num):
        if type == 'd':
            if detail_ents[num].get() == '*':
                detail_ents[num].delete(0, tk.END)
                detail_ents[num].config(fg='black')
                content.focus_set()

        if type == 't':
            if tier_ents[num].get() == '*':
                tier_ents[num].delete(0, tk.END)
                tier_ents[num].config(fg='black')
                content.focus_set()
        
    def make_black(event, type, num):
        if type == 'd':
            detail_ents[num].config(fg='black')
            content.focus_set()
        if type == 't':
            tier_ents[num].config(fg='black')
            content.focus_set()

    for type, num in d_errors.items():
        if type == f'blank{num}':
            detail_ents[num].delete(0, 'end')
            detail_ents[num].insert(0, '*')
            detail_ents[num].config(fg='red')
            detail_ents[num].bind('<FocusIn>', lambda event, num=num: delete_required(event, 'd', num))
        if type == f'digit{num}':
            detail_ents[num].config(fg='red')
            detail_ents[num].bind('<FocusIn>', lambda event, num=num: make_black(event, 'd', num))
        if type == f'alpha{num}':
            detail_ents[num].config(fg='red')
            detail_ents[num].bind('<FocusIn>', lambda event, d=num: delete_placeholder(event, d, True))
    for type, num in t_errors.items():
        if type == f'blank{num}':
            tier_ents[num].delete(0, 'end')
            tier_ents[num].insert(0, '*')
            tier_ents[num].config(fg='red')
            tier_ents[num].bind('<FocusIn>', lambda event, num=num: delete_required(event, 't', num))
        if type == f'alpha{num}':
            tier_ents[num].config(fg='red')
            tier_ents[num].bind('<FocusIn>', lambda event, num=num: make_black(event, 't', num))

# Task 2.4.4 Confirmation Pop-up
def confirm(content, type):
    # type = save / change
    global root
    root = tk.Tk()
    root.title('Confirmation')

    root_w = 175
    root_h = 85
    center_x = int(root.winfo_screenwidth() / 2 - root_w / 2)
    center_y = int((root.winfo_screenheight() / 2 - root_h / 2) - 35)
    root.geometry(f'{root_w}x{root_h}+{center_x}+{center_y}')
    root.resizable(False, False)

    frame = tk.Frame(root, width=root_w, height=root_h)
    frame.pack()
    frame.pack_propagate(False)

    if type == 'save':
        label = tk.Label(frame, text='Confirm order?', font=('Segoe Print', 12))
    elif type == 'change':
        label = tk.Label(frame, text='Save order?', font=('Segoe Print', 12))
    label.place(x=(root_w/2)-65, y=5)

    btns = ['Cancel', 'Confirm']
    bg = ['#FFC957', '#FFB253']
    cmd = [root.destroy, save_order]

    for b in range(2):
        frm_btn = tk.Frame(frame, width=60, height=30, bg='red')
        frm_btn.grid(row=0, column=b)
        frm_btn.place(x=((root_w/2)-68)+(b*70), y=40)
        frm_btn.pack_propagate(False)

        btn = tk.Button(frm_btn, text=btns[b], font=('Segoe Print', 10), bg=bg[b],
                        activebackground=bg[b], command=lambda b=b: (cmd[b](), create_order_list(content)))
        btn.pack(fill='both', expand=True)

    root.mainloop()

def save_btn_pressed(content):
    content.focus_set()
    error_prev()
    if has_error == True:
        resolve_error(content)
    elif has_error == False:
        confirm(content, 'save')

def create_confirm_btn(content):
    # Task 2.4.2
    frm_save = tk.Frame(content, width=150, height=30, bg='#FFB253')
    frm_save.place(x=410, y=440)
    frm_save.pack_propagate(False)
    btn_save = tk.Button(frm_save, text='Confirm Order', font=('Segoe Print', 11), bg='#FFB253',
                         activebackground='#FFB253', command=lambda: save_btn_pressed(content))
    btn_save.pack(fill='both', expand=True)

# Task 2.5 New Order Button
def new_order(content):
    for i in range(8):
        detail_ents[i].delete(0, 'end')
    for i in range(3):
        if detail_ents[i+2].get() == '':
            detail_ents[i+2].insert(0, dd_placeholders[i])
            detail_ents[i+2].config(fg='gray')
    create_tiers_table(content, 1)
    txt_decor.delete(1.0, 'end')

def create_new_order_btn(content):
    # Task 2.5 New Order Button
    border_orderlist = tk.Frame(content, width=1, height=480, bg='black')
    border_orderlist.place(x=580, y=0)

    frm_new_order = tk.Frame(content, width=270, height=50)
    frm_new_order.place(x=581, y=0)
    frm_new_order.pack_propagate(False)

    border_new = tk.Frame(content, width=270, height=1, bg='black')
    border_new.place(x=580, y=50)

    frm_btn = tk.Frame(frm_new_order, width=200, height=30, bg='red')
    frm_btn.place(x=(270/2)-(200/2), y=(50/2)-(30/2))
    frm_btn.pack_propagate(False)

    icon = tk.PhotoImage(file='list.png')
    btn_new = tk.Button(frm_btn, text='Create New Order ', font=('Segoe Print', 12), image=icon, compound='right',
                        bg='#FFB253', command=lambda: new_order(content))
    btn_new.image = icon
    btn_new.pack(fill='both', expand=True)

# Task 2.6
path = os.getcwd()
files = []
def check_files():
    files.clear()
    for f in os.listdir(path):
        if f.endswith('.json'):
            with open(f, 'r') as file:
                order = json.load(file)
                
            files.append((f, order))

    files.sort(key=lambda x:(int(x[1]['due_year']),
                             int(x[1]['due_month']),
                             int(x[1]['due_day'])))

def update_status(i, status):
    files[i][1]['completed'] = status.get()
    with open(files[i][0], "w") as f:
        json.dump(files[i][1], f, indent=4)

frm_orderlist = None
def create_order_list(content):
    global frm_orderlist
    if frm_orderlist is None:
        # Task 2.6.1
        frm_container = tk.Frame(content, width=270, height=429)
        frm_container.place(x=581, y=51)
        frm_container.pack_propagate(False)

        cvs_scroll = tk.Canvas(frm_container, width=270, height=430)
        cvs_scroll.place(x=0, y=0)

        # Task 2.6.2
        def mouse_scrollbar(event):
            cvs_scroll.yview_scroll(int(-event.delta / 120), "units")

        scrollbar = tk.Scrollbar(frm_container, orient='vertical', command=cvs_scroll.yview)
        scrollbar.pack(side='right', fill='y')

        cvs_scroll.configure(yscrollcommand=scrollbar.set)
        cvs_scroll.bind('<Enter>', lambda event: cvs_scroll.bind_all('<MouseWheel>', mouse_scrollbar))
        cvs_scroll.bind('<Leave>', lambda event: cvs_scroll.unbind_all('<MouseWheel>'))

        frm_orderlist = tk.Frame(cvs_scroll, width=270)
        frm_orderlist.bind('<Configure>', lambda event: cvs_scroll.configure
                        (scrollregion=cvs_scroll.bbox('all')))
        
        cvs_scroll.create_window((0, 0), window=frm_orderlist, anchor='nw')

    # Task 2.6.3
    check_files()

    for widget in frm_orderlist.winfo_children():
        widget.destroy()
    
    order_dates = []
    order_years = []
    for i in range(len(files)):
        if i == 0:
            order_years.append(files[i][1]['due_year'])
        elif i != 0:
            if files[i][1]['due_year'] != files[i-1][1]['due_year']:
                order_years.append(files[i][1]['due_year'])
    
    for i in range(len(order_years)):
        order_months = []

        for ii in range(len(files)):
            if files[ii][1]['due_year'] == order_years[i]:
                if ii == 0:
                    order_months.append(files[ii][1]['due_month'])
                elif ii != 0:
                    if files[ii][1]['due_month'] != files[ii-1][1]['due_month']:
                        order_months.append(files[ii][1]['due_month'])

        order_dates.append((order_years[i], order_months))

    print(order_dates)

    months = ['', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    for i in range(len(order_dates)):
        for a in range(len(order_dates[i][1])):
            if i+a != 0:
                frm_space = tk.Frame(frm_orderlist, width=270, height=10)
                frm_space.pack()

                frm_border = tk.Frame(frm_orderlist, width=270, height=1, bd=1, relief='solid', bg='black')
                frm_border.pack()

            frm_label = tk.Frame(frm_orderlist, width=270, height=25)
            frm_label.pack(padx=0, pady=5)

            lbl_order = tk.Label(frm_label, text=f'{months[int(order_dates[i][1][a])]} of {order_years[i]}',
                                font=('Segoe Print', 12))
            lbl_order.pack()

            for b in range(len(files)):
                if files[b][1]['due_year'] == order_dates[i][0]:
                    if files[b][1]['due_month'] == order_dates[i][1][a]:
                        frm_order = tk.Frame(frm_orderlist, width=150, height=25, bd=1.5, relief='groove')
                        frm_order.pack(padx=20, pady=5)
                        frm_order.pack_propagate(False)
                        
                        frm_chk = tk.Frame(frm_order, width=25, height=25)
                        frm_chk.place(x=-2, y=-2)
                        frm_chk.pack_propagate(False)

                        completed = tk.BooleanVar()
                        completed.set(files[b][1]['completed'])
                        check_box = tk.Checkbutton(frm_chk, variable=completed, width=25, height=25,
                                                   command=lambda b=b, status=completed: update_status(b, status))
                        check_box.pack(fill='both', expand=True)

                        frm_btn = tk.Frame(frm_order, width=125, height=25)
                        frm_btn.place(x=23, y=-2)
                        frm_btn.pack_propagate(False)

                        btn_order = tk.Button(frm_btn,
                                              text=f'{files[b][1]['due_day']} - {files[b][1]['customer_name']}',
                                              anchor='w', command=lambda b=b: 
                                              load_order(content, files[b][0].replace('.json', '')))
                        btn_order.pack(fill='both', expand=True)
    frm_space = tk.Frame(frm_orderlist, width=270, height=15)
    frm_space.pack()