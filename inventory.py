import tkinter as tk

# Task 1.1
inventory = tk.Tk()
inventory.title('Inventory - Cake Desire')
inventory.geometry('960x540+195+75')
inventory.resizable(False, False)

# Task 1.2
frm_title = tk.Frame(inventory, height=60, bg='#FFD333', bd=1, relief='solid')
frm_title.pack(fill=tk.X)

frm_navbar = tk.Frame(inventory, width=100, bg='#FEF67F')
frm_navbar.pack(fill=tk.Y, side='left')
frm_active = tk.Frame(frm_navbar, width=100, height=160, bg='#FFC957')
frm_active.pack(side='top')

left_bd = tk.Frame(inventory, width=1, height=540, bg='black')
left_bd.place(x=0, y=0)
title_right_bd = tk.Frame(inventory, width=1, height=60, bg='black')
title_right_bd.place(x=959, y=0)
navbar_right_bd = tk.Frame(inventory, width=1, height=480, bg='black')
navbar_right_bd.place(x=100, y=60)
active_bottom_bd = tk.Frame(inventory, width=100, height=1, bg='black')
active_bottom_bd.place(x=0, y=220)
navbar_bottom_bd = tk.Frame(inventory, width=100, height=1, bg='black')
navbar_bottom_bd.place(x=0, y=539)

# Task 1.1
inventory.mainloop()