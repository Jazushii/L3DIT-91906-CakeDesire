import tkinter as tk
import json

def open_inventory(content):
    create_header(content, 'Thanapn M')
    create_ingredients_table(content)

def create_header(content, file_name):
    with open(f'{file_name}.json', 'r') as file:
        order = json.load(file)

    frm_header = tk.Frame(content, width=400, height=50, bd=1.5, relief='groove')
    frm_header.place(x=100, y=10)
    frm_header.pack_propagate(False)

    lbl_header = tk.Label(frm_header, text=f"{order['customer_name']}'s {order['cake_type']} Cake",
                          font=('Segoe Print', 16, 'bold'), bg='#FFC957')
    lbl_header.pack(fill='both', expand=True)

def create_ingredients_table(content):
    frm_title = tk.Frame(content)
    frm_title.place(x=10, y=70)
    frm_title.pack_propagate(False)

    for r in range(9):
        for c in range(2):
            frame = tk.Frame(content)
            frame.place()
