import tkinter as tk

def OpenInventory():
    # Task 1.1 & 1.2
    inventory = tk.Tk()
    inventory.title('Cake Desire')
    inventory.geometry('960x540+195+75')
    inventory.resizable(False, False)

    main = tk.Frame(inventory, width=960, height=540)
    main.pack()
    main.pack_propagate(False)

    # Task 1.2
    title = tk.Frame(main, height=60, bg='#FFD333', bd=1, relief='solid')
    title.pack(fill=tk.X)
    title.pack_propagate(False)

    navbar = tk.Frame(main, width=110, height=480)
    navbar.place(x=0, y=60)
    navbar.pack_propagate(False)

    navbar_inven = tk.Frame(navbar, width=110, height=160, bg='#FFC957')
    navbar_inven.pack(fill=tk.X)
    navbar_inven.pack_propagate(False)
    navbar_order = tk.Frame(navbar, width=110, height=160, bg='#FEF67F')
    navbar_order.pack(fill=tk.X)
    navbar_order.pack_propagate(False)
    navbar_calen = tk.Frame(navbar, width=110, height=160, bg='#FEF67F')
    navbar_calen.pack(fill=tk.X)
    navbar_calen.pack_propagate(False)

    navbar_bd_left = tk.Frame(navbar, width=1, height=480, bg='black')
    navbar_bd_left.place(x=0, y=60)

    # Task 1.3 & 1.4
    logo = tk.PhotoImage(file='cake-desire-logo.png')
    lbl_title = tk.Label(title, text='Cake Desire ', font=('Ink Free', 24, 'bold'), image=logo, compound='right', bg='#FFD333')
    lbl_title.pack(fill="both", expand=True)

    def switch_orderlist():
        from orderlist import OpenOrderList
        inventory.destroy()
        OpenOrderList()

    def switch_calendar():
        from calendar import OpenCalendar
        inventory.destroy()
        OpenCalendar()

    btn_inven = tk.Button(navbar_inven, text='Inventory', font=('Segoe Print', 14, 'bold'), bg='#FFC957', activebackground='#FFC957')
    btn_inven.pack(fill="both", expand=True)
    btn_order = tk.Button(navbar_order, text='Order\nList', font=('Segoe Print', 14), bg='#FEF67F', activebackground='#FFC957', command=switch_orderlist)
    btn_order.pack(fill="both", expand=True)
    btn_calen = tk.Button(navbar_calen, text='Calendar', font=('Segoe Print', 14), bg='#FEF67F', activebackground='#FFC957', command=switch_calendar)
    btn_calen.pack(fill="both", expand=True)

    # Task 1.1
    inventory.mainloop()

if __name__ == "__main__":
    OpenInventory()