import tkinter as tk

# Task 1.1
inventory = tk.Tk()
inventory.title('Inventory - Cake Desire')
inventory.geometry('960x540+195+75')

# Task 1.2
frm_title = tk.Frame(inventory, height=60, bg='#FFD333')
frm_title.pack(fill=tk.X, side='top')

frm_navbar = tk.Frame(inventory, width=100, bg='#FEF67F')
frm_navbar.pack(fill=tk.Y, side='left')
frm_active = tk.Frame(frm_navbar, width=100, height=160, bg='#FFC957')
frm_active.pack(side='top')

# Task 1.1
inventory.mainloop()