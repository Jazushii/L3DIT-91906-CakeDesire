import tkinter as tk

def OpenOrderList():
    # Task 1.1 & 1.2
    orderlist = tk.Tk()
    orderlist.title('Cake Desire')
    orderlist.geometry('960x540+195+75')
    orderlist.resizable(False, False)

    # Task 1.2
    frm_title = tk.Frame(orderlist, height=60, bg='#FFD333', bd=1, relief='solid')
    frm_title.pack(fill=tk.X)
    frm_title.pack_propagate(False)

    navbar_inventory = tk.Frame(orderlist, width=110, height=160, bg='#FEF67F')
    navbar_inventory.place(x=0, y=60)
    navbar_inventory.pack_propagate(False)
    navbar_orderlist = tk.Frame(orderlist, width=110, height=160, bg='#FFC957')
    navbar_orderlist.place(x=0, y=220)
    navbar_orderlist.pack_propagate(False)
    navbar_calendar = tk.Frame(orderlist, width=110, height=160, bg='#FEF67F')
    navbar_calendar.place(x=0, y=380)
    navbar_calendar.pack_propagate(False)

    # Task 1.3 & 1.4
    cd_logo = tk.PhotoImage(file='cake-desire-logo.png')
    lbl_title = tk.Label(frm_title, text='Cake Desire ', font=('Ink Free', 24, 'bold'), image=cd_logo, compound='right', bg='#FFD333')
    lbl_title.pack(fill="both", expand=True)

    def switch_inventory():
        from inventory import OpenInventory
        orderlist.destroy()
        OpenInventory()
    
    def switch_calendar():
        from calendar import OpenCalendar
        orderlist.destroy()
        OpenCalendar()

    btn_inventory = tk.Button(navbar_inventory, text='Inventory', font=('Segoe Print', 14), bg='#FEF67F', activebackground='#FFC957', command=switch_inventory)
    btn_inventory.pack(fill="both", expand=True)
    btn_orderlist = tk.Button(navbar_orderlist, text='Order\nList', font=('Segoe Print', 14, 'bold'), bg='#FFC957', activebackground='#FFC957')
    btn_orderlist.pack(fill="both", expand=True)
    btn_calendar = tk.Button(navbar_calendar, text='Calendar', font=('Segoe Print', 14), bg='#FEF67F', activebackground='#FFC957', command=switch_calendar)
    btn_calendar.pack(fill="both", expand=True)

    # Task 1.1
    orderlist.mainloop()