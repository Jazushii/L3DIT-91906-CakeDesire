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

    # Task 2.1
    content = tk.Frame(main, width=850, height=480)
    content.place(x=110, y=60)
    content.pack_propagate(False)

    name = tk.Frame(content, width=200, height=60, pady=5, bd=1.5, relief='groove')
    name.place(x=20, y=20)
    name.pack_propagate(False)
    lbl_name = tk.Label(name, text='Customer Name:', font=('Segoe Print', 12))
    lbl_name.place(x=5, y=-6)
    ent_name = tk.Entry(name, width=20, font=('Arial', 12))
    ent_name.place(x=5, y=24)

    # Task 1.1
    orderlist.mainloop()

if __name__ == "__main__":
    OpenOrderList()