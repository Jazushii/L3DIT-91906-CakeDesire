import tkinter as tk
from inventory import *
from orderlist import *
from calendar import *

def interface(type):
    # Task 1.1 & 1.2
    root = tk.Tk()
    root.title('Cake Desire')
    root.geometry('960x540+195+75')
    root.resizable(False, False)

    main = tk.Frame(root, width=960, height=540)
    main.pack()
    main.pack_propagate(False)

    # Task 1.2
    title = tk.Frame(main, height=60, bg='#FFD333', bd=1, relief='solid')
    title.pack(fill=tk.X)
    title.pack_propagate(False)

    navbar = tk.Frame(main, width=110, height=480)
    navbar.place(x=0, y=60)
    navbar.pack_propagate(False)

    inven_colour = '#FFC957' if type == 'inventory' else '#FEF67F'
    order_colour = '#FFC957' if type == 'orderlist' else '#FEF67F'
    calen_colour = '#FFC957' if type == 'calendar' else '#FEF67F'

    navbar_inven = tk.Frame(navbar, height=160, bg=inven_colour)
    navbar_inven.pack(fill=tk.X)
    navbar_inven.pack_propagate(False)
    navbar_order = tk.Frame(navbar, height=160, bg=order_colour)
    navbar_order.pack(fill=tk.X)
    navbar_order.pack_propagate(False)
    navbar_calen = tk.Frame(navbar, height=160, bg=calen_colour)
    navbar_calen.pack(fill=tk.X)
    navbar_calen.pack_propagate(False)

    navbar_bd_left = tk.Frame(navbar, width=1, height=480, bg='black')
    navbar_bd_left.pack()

    # Task 1.3 & 1.4
    logo = tk.PhotoImage(file='cake-desire-logo.png')
    lbl_title = tk.Label(title, text='Cake Desire ', font=('Ink Free', 24, 'bold'), image=logo, compound='right', bg='#FFD333')
    lbl_title.pack(fill="both", expand=True)

    def switch(switch):
        root.destroy()
        if switch == 'inventory':
            interface('inventory')
        if switch == 'orderlist':
            interface('orderlist')
        if switch == 'calendar':
            interface('calendar')

    btn_inven = tk.Button(navbar_inven, text='Inventory', font=('Segoe Print', 14), bg=inven_colour, activebackground='#FFC957', command=lambda:switch('inventory'))
    btn_inven.pack(fill="both", expand=True)
    btn_order = tk.Button(navbar_order, text='Order\nList', font=('Segoe Print', 14, 'bold'), bg=order_colour, activebackground='#FFC957', command=lambda:switch('orderlist'))
    btn_order.pack(fill="both", expand=True)
    btn_calen = tk.Button(navbar_calen, text='Calendar', font=('Segoe Print', 14), bg=calen_colour, activebackground='#FFC957', command=lambda:switch('calendar'))
    btn_calen.pack(fill="both", expand=True)

    if type == 'inventory':
        open_inventory(main)
    if type == 'orderlist':
        open_orderlist(main)
    if type == 'calendar':
        open_calendar(main)

    root.mainloop()

interface('inventory')