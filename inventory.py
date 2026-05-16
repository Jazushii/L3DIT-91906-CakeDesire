import tkinter as tk

# Task 1.1 & 1.2
inventory = tk.Tk()
inventory.title('Cake Desire')
inventory.geometry('960x540+195+75')
inventory.resizable(False, False)

# Task 1.2
frm_title = tk.Frame(inventory, height=60, bg='#FFD333', bd=1, relief='solid')
frm_title.pack(fill=tk.X)
frm_title.pack_propagate(False)

navbar_inventory = tk.Frame(inventory, width=110, height=160, bg='#FFC957')
navbar_inventory.place(x=0, y=60)
navbar_inventory.pack_propagate(False)
navbar_orderlist = tk.Frame(inventory, width=110, height=160, bg='#FEF67F')
navbar_orderlist.place(x=0, y=220)
navbar_orderlist.pack_propagate(False)
navbar_calendar = tk.Frame(inventory, width=110, height=160, bg='#FEF67F')
navbar_calendar.place(x=0, y=380)
navbar_calendar.pack_propagate(False)

# Task 1.3 & 1.4
cd_logo = tk.PhotoImage(file='cake-desire-logo.png')
lbl_title = tk.Label(frm_title, text='Cake Desire ', font=('Ink Free', 24, 'bold'), image=cd_logo, compound='right', bg='#FFD333')
lbl_title.pack(fill="both", expand=True)

btn_inventory = tk.Button(navbar_inventory, text='Inventory', font=('Segoe Print', 14, 'bold'), bg='#FFC957', activebackground='#FFC957')
btn_inventory.pack(fill="both", expand=True)
btn_orderlist = tk.Button(navbar_orderlist, text='Order\nList', font=('Segoe Print', 14), bg='#FEF67F', activebackground='#FFC957')
btn_orderlist.pack(fill="both", expand=True)
btn_calendar = tk.Button(navbar_calendar, text='Calendar', font=('Segoe Print', 14), bg='#FEF67F', activebackground='#FFC957')
btn_calendar.pack(fill="both", expand=True)

# Task 1.1
inventory.mainloop()