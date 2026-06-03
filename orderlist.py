import tkinter as tk
import json

def OpenOrderList():
    # Task 1.1 & 1.2
    orderlist = tk.Tk()
    orderlist.title('Cake Desire')
    orderlist.geometry('960x540+195+75')
    orderlist.resizable(False, False)

    main = tk.Frame(orderlist, width=960, height=540)
    main.pack()
    main.pack_propagate(False)

    # Task 1.2
    title = tk.Frame(main, height=60, bg='#FFD333', bd=1, relief='solid')
    title.pack(fill=tk.X)
    title.pack_propagate(False)

    navbar = tk.Frame(main, width=110, height=480)
    navbar.place(x=0, y=60)
    navbar.pack_propagate(False)

    navbar_inven = tk.Frame(navbar, height=160, bg='#FEF67F')
    navbar_inven.pack(fill=tk.X)
    navbar_inven.pack_propagate(False)
    navbar_order = tk.Frame(navbar, height=160, bg='#FFC957')
    navbar_order.pack(fill=tk.X)
    navbar_order.pack_propagate(False)
    navbar_calen = tk.Frame(navbar, height=160, bg='#FEF67F')
    navbar_calen.pack(fill=tk.X)
    navbar_calen.pack_propagate(False)

    navbar_bd_left = tk.Frame(navbar, width=1, height=480, bg='black')
    navbar_bd_left.pack()

    # Task 1.3 & 1.4
    logo = tk.PhotoImage(file='cake-desire-logo.png')
    lbl_title = tk.Label(title, text='Cake Desire ', font=('Ink Free', 24, 'bold'), image=logo, compound='right', bg='#FFD333')
    lbl_title.pack(fill="both", expand=True)

    def switch_inventory():
        from inventory import OpenInventory
        orderlist.destroy()
        OpenInventory()
    
    def switch_calendar():
        from calendar import OpenCalendar
        orderlist.destroy()
        OpenCalendar()

    btn_inven = tk.Button(navbar_inven, text='Inventory', font=('Segoe Print', 14), bg='#FEF67F', activebackground='#FFC957', command=switch_inventory)
    btn_inven.pack(fill="both", expand=True)
    btn_order = tk.Button(navbar_order, text='Order\nList', font=('Segoe Print', 14, 'bold'), bg='#FFC957', activebackground='#FFC957')
    btn_order.pack(fill="both", expand=True)
    btn_calen = tk.Button(navbar_calen, text='Calendar', font=('Segoe Print', 14), bg='#FEF67F', activebackground='#FFC957', command=switch_calendar)
    btn_calen.pack(fill="both", expand=True)

    # Task 2.2
    content = tk.Frame(main, width=850, height=480)
    content.place(x=110, y=60)
    content.pack_propagate(False)

    labels = [
        'Customer Name:',
        'Cake Flavour:',
        'Due Date:',
        'Cake Colour/s:',
        'Cake Type:',
        'Cake Shape:'
    ]

    le = 0

    entries = []

    for re in range(3):
        for ce in range(2):
            frame = tk.Frame(content, width=265, height=62, bd=1.5, relief='groove')
            frame.grid(row=re, column=ce)
            frame.place(x=20+(ce*275), y=20+(re*70))
            frame.pack_propagate(False)
            label = tk.Label(frame, text=labels[le], font=('Segoe Print', 12))
            label.place(x=5, y=-1)
            if le == 2:
                entries.append(tk.Entry(frame, width=20, font=('Arial', 12), bg='white'))
                frm_icon = tk.Frame(frame, width=20, height=20, bg='#FEF8A0')
                frm_icon.place(x=168, y=31)
                frm_icon.pack_propagate(False)
                icon = tk.PhotoImage(file='date-icon.png')
                img_icon = tk.Label(frm_icon, image=icon, bg='#FEF8A0')
                img_icon.pack(fill="both", expand=True)
            else:
                entries.append(tk.Entry(frame, width=20, font=('Arial', 12), bg='#FEF8A0'))
            entries[le].place(x=5, y=30)
            le += 1
    
    # Task 2.3.1
    frm_tiers = None

    def tiers_table(rnum):
        global ent_tiers
        global tier_entries
        nonlocal frm_tiers
        if frm_tiers is not None:
            frm_tiers.destroy()

        frm_tiers = tk.Frame(content, width=265, height=106+(int(rnum)*25), bd=1.5, relief='groove')
        frm_tiers.place(x=20, y=230)
        frm_tiers.pack_propagate(False)
        lbl_tiers = tk.Label(frm_tiers, text='No. of Cake Tiers:', font=('Segoe Print', 12))
        lbl_tiers.place(x=5, y=-1)
        ent_tiers = tk.Entry(frm_tiers, width=2, font=('Arial', 12))
        ent_tiers.place(x=5, y=30)
        ent_tiers.insert(0, rnum)

        # Task 2.3.2
        tier_txt = [
            'Tier:',
            'Layers:',
            'Size (In.):'
        ]

        tier_entries = []

        tt = 0
        et = 0

        for rt in range(int(rnum)):
            tt = 0
            for ct in range(3):
                frame = tk.Frame(frm_tiers, width=84, height=38, bd=1.5, relief='groove', bg='#FEF8A0')
                frame.grid(row=0, column=ct)
                frame.place(x=4+(ct*84), y=60)
                frame.pack_propagate(False)
                label = tk.Label(frame, text=tier_txt[tt], font=('Segoe Print', 12), bg='#FEF8A0')
                label.place(x=0, y=-1)
                tt += 1

                frame = tk.Frame(frm_tiers, width=84, height=25)
                frame.grid(row=rt+1, column=ct)
                frame.place(x=4+(ct*84), y=98+((rt)*25))
                frame.pack_propagate(False)
                tier_entries.append(tk.Entry(frame, font=('Arial', 12), bd=1.5, relief='groove'))
                tier_entries[et].pack(fill='both', expand=True)
                et += 1

        # Task 2.3.1
        frm_btn_tiers = tk.Frame(frm_tiers, width=22, height=22, bg='#FEF8A0')
        frm_btn_tiers.place(x=27, y=30)
        frm_btn_tiers.pack_propagate(False)
        btn_tiers = tk.Button(frm_btn_tiers, text='▼', font=('Arial', 10, 'bold'), bg='#FEF8A0', activebackground='#FEF8A0', command=lambda: tiers_table(ent_tiers.get()))
        btn_tiers.pack(fill='both', expand=True)

    tiers_table(1)

    # Task 2.3.1
    # height=231
    frm_decor = tk.Frame(content, width=265, height=201, bd=1.5, relief='groove')
    frm_decor.place(x=295, y=230)
    frm_decor.pack_propagate(False)
    lbl_decor = tk.Label(frm_decor, text='Decorations/Toppings:', font=('Segoe Print', 12))
    lbl_decor.place(x=5, y=-1)

    # Task 2.3.3
    # height=190
    frm_txt_decor = tk.Frame(frm_decor, width=250, height=160, bd=1.5, relief='groove', bg='#FEF8A0')
    frm_txt_decor.place(x=5, y=30)
    frm_txt_decor.pack_propagate(False)
    txt_decor = tk.Text(frm_txt_decor, font=('Arial', 12), bg='#FEF8A0')
    txt_decor.pack(fill='both', expand=True)

    # Task 2.4.3
    def error_prev():
        global error
        global blank
        global digit
        error = 0
        blank = 0
        digit = 0
        for ep in range(6):
            if entries[ep].get() == '':
                error = 1
                blank = 1
            sum_digit = sum(a.isdigit() for a in entries[ep].get())
            if sum_digit != 0:
                error = 1
                digit = 1
        if blank == 1:
            print('blank error')
        if digit == 1:
            print('digit error')

    # Task 2.4.1
    def save_order():

        order_details = {
            'customer_details':entries[0].get(),
            'cake_flavour':entries[1].get(),
            'due_date':entries[2].get(),
            'cake_colour/s':entries[3].get(),
            'cake_type':entries[4].get(),
            'cake_shape':entries[5].get(),
            'decor':txt_decor.get("1.0", tk.END),
            'tiers':ent_tiers.get()
        }
        
        tier_labels = ['tier', 'layer', 'size']

        ts = 0

        for tn in range(int(ent_tiers.get())):
            for td in range(3):
                order_details[f'{tier_labels[td]} {tn+1}'] = tier_entries[ts].get()
                ts += 1

        with open(f'{entries[0].get()}.json', 'w') as f:
            json.dump(order_details, f, indent=4)

        print('Saving...')

    def save_button_pressed():
        error_prev()
        if error == 0:
            save_order()

    # Task 2.4.2
    frm_save = tk.Frame(content, width=150, height=30, bg='#FFB253')
    frm_save.place(x=410, y=440)
    frm_save.pack_propagate(False)
    btn_save = tk.Button(frm_save, text='Confirm Order', font=('Segoe Print', 11), bg='#FFB253', activebackground='#FFB253', command=save_button_pressed)
    btn_save.pack(fill='both', expand=True)

    # Task 1.1
    orderlist.mainloop()

if __name__ == "__main__":
    OpenOrderList()