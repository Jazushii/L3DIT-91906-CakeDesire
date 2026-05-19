import tkinter as tk

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

    for r in range(3):
        for c in range(2):
            frame = tk.Frame(content, width=265, height=62, bd=1.5, relief='groove')
            frame.grid(row=r, column=c)
            frame.place(x=20+(c*275), y=20+(r*70))
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
    
    # Task 2.3
    frm_tiers = tk.Frame(content, width=265, height=100, bd=1.5, relief='groove')
    frm_tiers.place(x=20, y=230)
    frm_tiers.pack_propagate(False)
    lbl_tiers = tk.Label(frm_tiers, text='No. of Cake Tiers:', font=('Segoe Print', 12))
    lbl_tiers.place(x=5, y=-1)
    ent_tiers = tk.Entry(frm_tiers, width=2, font=('Arial', 12))
    ent_tiers.place(x=5, y=30)
    def tiers_table():
        for r in range(int(ent_tiers.get)):
            for c in range(3):
                frame = tk.Frame(frm_tiers, width=265, height=60, bd=1.5, relief='groove')
                frame.grid(row=r, column=c)
                frame.place(x=20+(c*275), y=20+(r*70))
                frame.pack_propagate(False)
                label = tk.Label(frame, text=labels[le], font=('Segoe Print', 12))
                label.place(x=5, y=-1)
    frm_btn_tiers = tk.Frame(frm_tiers, width=22, height=22, bg='#FEF8A0')
    frm_btn_tiers.place(x=27, y=30)
    frm_btn_tiers.pack_propagate(False)
    btn_tiers = tk.Button(frm_btn_tiers, text='▼', font=('Arial', 10, 'bold'), bg='#FEF8A0', command=tiers_table)
    btn_tiers.pack(fill='both', expand=True)

    # Task 1.1
    orderlist.mainloop()

if __name__ == "__main__":
    OpenOrderList()