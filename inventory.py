import tkinter as tk
import json

def open_inventory(content):
    create_header(content, 'Thanapn M')
    create_ingredients_table(content)
    create_equipments_table(content)
    create_decor_table(content)

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

    frm_title = tk.Frame(content, width=180, height=40, bd=1.5, relief='groove', bg='#FFC957')
    frm_title.place(x=20, y=70)
    frm_title.pack_propagate(False)

    lbl_title = tk.Label(frm_title, text='Ingredients Needed:', font=('Segoe Print', 12, 'bold'), bg='#FFC957')
    lbl_title.pack()

    ingredients_lbls = [
        '- Eggs',
        '-ml of Milk',
        '-ml of Cooking Oil',
        '-g of Flour',
        '-g of Sugar',
        '-g of Butter',
        '-tsp of Salt',
        '-tsp of Baking Soda',
        '-tsp Cocoa Powder',
    ]

    for r in range(9):
        frame = tk.Frame(content, width=180, height=30, bd=1.5, relief='groove', bg='#FEF8A0')
        frame.place(x=20, y=110+30*r)
        frame.pack_propagate(False)

        label = tk.Label(frame, text=ingredients_lbls[r], font=('Arial', 12), bg='#FEF8A0')
        label.place(x=0, y=1)

def create_equipments_table(content):

    frm_title = tk.Frame(content, width=180, height=40, bd=1.5, relief='groove', bg='#FFC957')
    frm_title.place(x=220, y=70)
    frm_title.pack_propagate(False)

    lbl_title = tk.Label(frm_title, text='Equipment Needed:', font=('Segoe Print', 12, 'bold'), bg='#FFC957')
    lbl_title.pack()

    equipments_lbls = [
        'Mixing Bowls',
        'Measuring Cups',
        'Measuring Spoons',
        'Whisk',
        'Spatula',
    ]

    for r in range(len(equipments_lbls)):
        frame = tk.Frame(content, width=180, height=30, bd=1.5, relief='groove', bg='#FEF8A0')
        frame.place(x=220, y=110+30*r)
        frame.pack_propagate(False)

        label = tk.Label(frame, text=equipments_lbls[r], font=('Arial', 12), bg='#FEF8A0')
        label.place(x=0, y=1)

def create_decor_table(content):

    frm_title = tk.Frame(content, width=190, height=40, bd=1.5, relief='groove', bg='#FFC957')
    frm_title.place(x=420, y=70)
    frm_title.pack_propagate(False)

    lbl_title = tk.Label(frm_title, text='Decoration/Toppings:', font=('Segoe Print', 12, 'bold'), bg='#FFC957')
    lbl_title.pack()

    frame = tk.Frame(content, width=190, height=300, bd=1.5, relief='groove', bg='#FEF8A0')
    frame.place(x=420, y=110)
    frame.pack_propagate(False)

    text = tk.Text(frame, font=('Arial', 12), bg='#FEF8A0', state='disabled')
    text.pack(fill='both', expand=True)
    text.insert(1.0, 'rah')