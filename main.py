import tkinter as tk
from inventory import *
from orderlist import *
from calendar import *

# #FFD333
# #FFC957
# #FFB253

def interface(type):
    # Task 1.1 & 1.2

    root = tk.Tk()
    root.title('Cake Desire')

    root_w = 960
    root_h = 540
    center_x = int(root.winfo_screenwidth() / 2 - root_w / 2)
    center_y = int((root.winfo_screenheight() / 2 - root_h / 2) - 35)
    root.geometry(f'{root_w}x{root_h}+{center_x}+{center_y}')
    root.resizable(False, False)

    main = tk.Frame(root, width=root_w, height=root_h)
    main.pack()
    main.pack_propagate(False)

    # Task 1.2
    title = tk.Frame(main, height=60, bg='#FFD333', bd=1, relief='solid')
    title.pack(fill=tk.X)
    title.pack_propagate(False)

    navbar = tk.Frame(main, width=110, height=480)
    navbar.place(x=0, y=60)
    navbar.pack_propagate(False)

    navbar_inven = tk.Frame(navbar, height=160)
    navbar_inven.pack(fill=tk.X)
    navbar_inven.pack_propagate(False)
    navbar_order = tk.Frame(navbar, height=160)
    navbar_order.pack(fill=tk.X)
    navbar_order.pack_propagate(False)
    navbar_calen = tk.Frame(navbar, height=160)
    navbar_calen.pack(fill=tk.X)
    navbar_calen.pack_propagate(False)

    navbar_bd_left = tk.Frame(navbar, width=1, height=480, bg='black')
    navbar_bd_left.pack()

    # Task 1.3 & 1.4
    logo = tk.PhotoImage(file='cake-desire-logo.png')
    lbl_title = tk.Label(title, text='Cake Desire ', font=('Ink Free', 24, 'bold'), image=logo, compound='right', bg='#FFD333')
    lbl_title.pack(fill="both", expand=True)

    def switch(switch):
        #if change == False:
           # confirm('change')
        root.destroy()
        if switch == 'inventory':
            interface('inventory')
        if switch == 'orderlist':
            interface('orderlist')
        if switch == 'calendar':
            interface('calendar')

    inven_font = ('Segoe Print', 14, 'bold') if type == 'inventory' else ('Segoe Print', 14)
    order_font = ('Segoe Print', 14, 'bold') if type == 'orderlist' else ('Segoe Print', 14)
    calen_font = ('Segoe Print', 14, 'bold') if type == 'calendar' else ('Segoe Print', 14)

    inven_colour = '#FFC957' if type == 'inventory' else '#FEF67F'
    order_colour = '#FFC957' if type == 'orderlist' else '#FEF67F'
    calen_colour = '#FFC957' if type == 'calendar' else '#FEF67F'

    btn_inven = tk.Button(navbar_inven, text='Inventory', font=inven_font, bg=inven_colour,
                          activebackground='#FFC957', command=lambda:switch('inventory'))
    btn_inven.pack(fill="both", expand=True)
    btn_order = tk.Button(navbar_order, text='Order\nList', font=order_font, bg=order_colour,
                          activebackground='#FFC957', command=lambda:switch('orderlist'))
    btn_order.pack(fill="both", expand=True)
    btn_calen = tk.Button(navbar_calen, text='Calendar', font=calen_font, bg=calen_colour,
                          activebackground='#FFC957', command=lambda:switch('calendar'))
    btn_calen.pack(fill="both", expand=True)
    
    content = tk.Frame(main, width=850, height=480)
    content.place(x=110, y=60)
    content.pack_propagate(False)

    if type == 'inventory':
        open_inventory(content)
    if type == 'orderlist':
        open_orderlist(content)
    if type == 'calendar':
        open_calendar(content)

    root.mainloop()

interface('inventory')