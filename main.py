import tkinter as tk
from inventory import *
from orderlist import *
from calendar import *

# #FFD333
# #FFC957
# #FFB253

# Window Creation
def create_window():

    # TASK 1.1 & 1.2
    # creates the window
    root = tk.Tk()
    root.title('Cake Desire')

    # seting the window's attributes
    root_w = 960
    root_h = 540
    center_x = int(root.winfo_screenwidth() / 2 - root_w / 2)
    center_y = int((root.winfo_screenheight() / 2 - root_h / 2) - 35)
    root.geometry(f'{root_w}x{root_h}+{center_x}+{center_y}')
    root.resizable(False, False)

    # creating frames for each interface
    global frm_inventory, frm_orderlist, frm_calendar
    frm_calendar = tk.Frame(root, width=root_w, height=root_h)
    frm_calendar.place(x=0, y=0)
    frm_calendar.pack_propagate(False)
    interface(frm_calendar, 'calendar')
    frm_orderlist = tk.Frame(root, width=root_w, height=root_h)
    frm_orderlist.place(x=0, y=0)
    frm_orderlist.pack_propagate(False)
    interface(frm_orderlist, 'orderlist')
    frm_inventory = tk.Frame(root, width=root_w, height=root_h)
    frm_inventory.place(x=0, y=0)
    frm_inventory.pack_propagate(False)
    interface(frm_inventory, 'inventory')

    # loops and actually runs the window
    root.mainloop()

in_orderlist = False
# creates the title and navbar
def interface(main, type):

    # TASK 1.2
    # creates the title block / frame
    title = tk.Frame(main, height=60, bd=1, relief='solid')
    title.pack(fill=tk.X)
    title.pack_propagate(False)

    # create the navigation bar block / frame
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

    # create the border since i can't make single sided borders
    navbar_bd_left = tk.Frame(navbar, width=1, height=480, bg='black')
    navbar_bd_left.pack()

    # TASK 1.3 & 1.4
    # create the title text and the logo in the text
    logo = tk.PhotoImage(file='cake-desire-logo.png')
    lbl_title = tk.Label(title, text='Cake Desire ', font=('Ink Free', 24, 'bold'), image=logo, compound='right', bg='#FFD333')
    lbl_title.image = logo
    lbl_title.pack(fill="both", expand=True)

    # sets the interface navbar attributes for the different interfaces
    inven_font = ('Segoe Print', 14, 'bold') if type == 'inventory' else ('Segoe Print', 14)
    inven_colour = '#FFC957' if type == 'inventory' else '#FEF67F'
    order_font = ('Segoe Print', 14, 'bold') if type == 'orderlist' else ('Segoe Print', 14)
    order_colour = '#FFC957' if type == 'orderlist' else '#FEF67F'
    calen_font = ('Segoe Print', 14, 'bold') if type == 'calendar' else ('Segoe Print', 14)
    calen_colour = '#FFC957' if type == 'calendar' else '#FEF67F'

    # create the buttons for the navbar with the command to switch them to that interface
    btn_inven = tk.Button(navbar_inven, text='Inventory', font=inven_font, bg=inven_colour,
                          activebackground='#FFC957', command=lambda:switch_check(content, 'inventory'))
    btn_inven.pack(fill="both", expand=True)
    btn_order = tk.Button(navbar_order, text='Order\nList', font=order_font, bg=order_colour,
                          activebackground='#FFC957', command=lambda:switch_check(content, 'orderlist'))
    btn_order.pack(fill="both", expand=True)
    btn_calen = tk.Button(navbar_calen, text='Calendar', font=calen_font, bg=calen_colour,
                          activebackground='#FFC957', command=lambda:switch_check(content, 'calendar'))
    btn_calen.pack(fill="both", expand=True)
    
    # creates the frame for the content
    global content
    content = tk.Frame(main, width=850, height=480)
    content.place(x=110, y=60)
    content.pack_propagate(False)

    if type == 'inventory':
        open_inventory(content)
    if type == 'orderlist':
        open_orderlist(content)
    if type == 'calendar':
        open_calendar(content)   

def switch_check(content, switch_to):
    
    global in_orderlist, change
    if in_orderlist == True:
        print('checking changes')
        check_changes()
        import orderlist
        if orderlist.change == 1:
            confirm(content, 'change', switch_to)
                
        else: 
            in_orderlist = False
            do_switch(switch_to)

    else: 
        do_switch(switch_to)

def do_switch(switch_to):
    global in_orderlist

    if switch_to == 'inventory':
        in_orderlist = False
        frm_inventory.tkraise()
    if switch_to == 'orderlist':
        in_orderlist = True
        frm_orderlist.tkraise()
    if switch_to == 'calendar':
        in_orderlist = False
        frm_calendar.tkraise()

    print(len(frm_inventory.winfo_children()))

create_window()