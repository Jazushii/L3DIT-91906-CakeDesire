import tkinter as tk

# Task 1.1
inventory = tk.Tk()
inventory.title('Inventory - Cake Desire')
inventory.geometry('960x540+195+75')
inventory.resizable(False, False)

# Task 1.2
frm_title = tk.Frame(inventory, height=60, bg='#FFD333', bd=1, relief='solid')
frm_title.pack(fill=tk.X)
frm_title.pack_propagate(False)

frm_navbar = tk.Frame(inventory, width=110, bg='#FEF67F')
frm_navbar.pack(fill=tk.Y, side='left')
frm_navbar.pack_propagate(False)
frm_active = tk.Frame(frm_navbar, width=110, height=160, bg='#FFC957')
frm_active.pack(side='top')
frm_active.pack_propagate(False)

left_bd = tk.Frame(inventory, width=1, height=540, bg='black')
left_bd.place(x=0, y=0)
title_right_bd = tk.Frame(inventory, width=1, height=60, bg='black')
title_right_bd.place(x=959, y=0)
navbar_right_bd = tk.Frame(inventory, width=1, height=480, bg='black')
navbar_right_bd.place(x=110, y=60)
active_bottom_bd = tk.Frame(inventory, width=110, height=1, bg='black')
active_bottom_bd.place(x=0, y=220)
navbar_bottom_bd = tk.Frame(inventory, width=110, height=1, bg='black')
navbar_bottom_bd.place(x=0, y=539)

# Task 1.3
cd_logo = tk.PhotoImage(file='cake-desire-logo.png')
lbl_title = tk.Label(frm_title, text='Cake Desire ', font=('Ink Free', 24, 'bold'), image=cd_logo, compound='right', bg='#FFD333')
lbl_title.place(relx=0.5, rely=0.5, anchor='center')

lbl_active = tk.Label(frm_active, text='Inventory', font=('Segoe Print', 14, 'bold'), bg='#FFC957')
lbl_active.place(relx=0.5, rely=0.5, anchor='center')
lbl_navbar = tk.Label(frm_navbar, text='Order\nList', font=('Segoe Print', 14), bg='#FEF67F')
lbl_navbar.place(relx=0.5, rely=0.5, anchor='center')
lbl_navbar = tk.Label(frm_navbar, text='Calendar', font=('Segoe Print', 14), bg='#FEF67F')
lbl_navbar.place(relx=0.5, rely=5/6, anchor='center')

# Task 1.1
inventory.mainloop()