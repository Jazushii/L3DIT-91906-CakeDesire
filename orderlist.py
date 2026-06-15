import tkinter as tk
import json

def open_orderlist(content):
    # Task 2.2 Details & Entry Boxes
    detail_lbls = [
        'Customer Name:',
        'Cake Flavour:',
        'Due Date:',
        '',
        '',
        'Cake Colour/s:',
        'Cake Type:',
        'Cake Shape:'
    ]

    detail_ents = []

    detail_num = 0

    for dr in range(3):
        for dc in range(2):
            frame = tk.Frame(content, width=265, height=62, bd=1.5, relief='groove')
            frame.grid(row=dr, column=dc)
            frame.place(x=20+(dc*275), y=20+(dr*70))
            frame.pack_propagate(False)
            label = tk.Label(frame, text=detail_lbls[detail_num], font=('Segoe Print', 12))
            label.place(x=5, y=-1)
            if detail_num == 2:
                frm_dd = tk.Frame(frame, width=200, height=30)
                frm_dd.place(x=5, y=30)
                dd_placeholders = ['DD', 'MM', 'YYYY']

                def create_placeholder(event, d):
                    if detail_ents[d].get() == dd_placeholders[d]:
                        detail_ents[d].delete(0, tk.END)
                        detail_ents[d].config(fg='black')

                def delete_placeholder(event, d):
                    if detail_ents[d].get() == '':
                        detail_ents[d].insert(0, dd_placeholders[d])
                        detail_ents[d].config(fg='gray')

                for dd in range(3):
                    detail_ents.append(tk.Entry(frm_dd, width=6, font=('Arial', 12), bg='white'))
                    detail_ents[detail_num].pack(side='left')
                    detail_ents[detail_num].insert(0, dd_placeholders[dd])
                    detail_ents[detail_num].config(fg='gray')

                    detail_ents[detail_num].bind('<FocusIn>', lambda event, d=dd: create_placeholder(event, d))
                    detail_ents[detail_num].bind('<FocusOut>', lambda event, d=dd: delete_placeholder(event, d))
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
    
    # Task 2.3.1
    frm_tiers = None

    def create_tiers_table(rnum):
        nonlocal frm_tiers
        global tier_ents
        global ent_tiers
        global size_ents
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

        # Task 2.3.2 Tiers Table
        # List of labels for the table
        tier_lbls = [
            'Tier:',
            'Layers:',
            'Size (In.):',
            ''
        ]

        tier_ents = []

        tier_num = 0

        for tr in range(int(rnum)):
            for tc in range(3):
                if tr == 0:
                    frm_lbl = tk.Frame(frm_tiers, width=84, height=38, bd=1.5, relief='groove', bg='#FEF8A0')
                    frm_lbl.grid(row=0, column=tc)
                    frm_lbl.place(x=4+(tc*84), y=60)
                    frm_lbl.pack_propagate(False)
                    lbl = tk.Label(frm_lbl, text=tier_lbls[tc], font=('Segoe Print', 12), bg='#FEF8A0')
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
        btn_tiers = tk.Button(frm_btn_tiers, text='▼', font=('Arial', 10, 'bold'), bg='#FEF8A0', activebackground='#FEF8A0', command=lambda: create_tiers_table(ent_tiers.get()))
        btn_tiers.pack(fill='both', expand=True)

    create_tiers_table(1)

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
    txt_decor = tk.Text(frm_txt_decor, font=('Arial', 12), bg='#FEF8A0')
    txt_decor.pack(fill='both', expand=True)

    # Task 2.4.1 File Set-up
    def save_order():

        order_details = {}
        
        # Saving Details
        detail_lbls = ['Customer_details', 'cake_flavour', 'due_date', 'cake_colours', 'cake_type', 'cake_shape']

        for dsave in range(6):
            order_details[detail_lbls[dsave]] = detail_ents[dsave].get

        # Saving Tiers Table
        tier_lbls = ['tier', 'layer', 'size']

        tsave = 0

        for tnum in range(int(ent_tiers.get())):
            for td in range(3):
                order_details[f'{tier_lbls[td]} {tnum+1}'] = detail_ents[tsave].get()
                tsave += 1

        # Saving Decorations / Toppings
        order_details['decor'] = txt_decor.get("1.0", tk.END)

        with open(f'{detail_ents[0].get()}.json', 'w') as f:
            json.dump(order_details, f, indent=4)

        print('Saving...')

    # Task 2.4.3 Error Prevention
    def error_prev():
        global error
        error = 0
        blank = 0
        digit = 0

        for de in range(6):
            if detail_ents[de].get() == '':
                error = 1
                blank = 1
            sum_digit = sum(a.isdigit() for a in detail_ents[de].get())
            if sum_digit != 0:
                error = 1
                digit = 1

        tc = 0

        for tn in range(int(ent_tiers.get())):
            for tep in range(3):
                if tier_ents[tc].get() == '':
                    error = 1
                    blank = 1
                
                tc += 1

        if blank == 1:
            print('blank error')
        if digit == 1:
            print('digit error')

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

    print(detail_ents)
    print(due_date_ents)
    print(tier_ents)
    print(size_ents)