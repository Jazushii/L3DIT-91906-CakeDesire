import tkinter as tk
import json
import math
from fractions import Fraction

def open_inventory(content):
    load_details('Lei Jin')
    create_header(content)
    create_ingredients_table(content)
    create_equipments_table(content)
    create_decor_table(content)
    create_inven_stock(content)

def load_details(file_name):
    with open(f'{file_name}.json', 'r') as file:
        global order
        order = json.load(file)

    with open('inventory_stock.json', 'r') as file:
        global stock
        stock = json.load(file)

    cake_vol = 0
    for i in range(int(order['tier_num'])):
        if order['cake_shape'] == 'Round':
            cake_vol += (math.pi*(math.pow((int(order[f'tier{i+1}_size_a'])/2), 2)) * int(order[f'tier{i+1}_size_b']))
        if order['cake_shape'] == 'Square':
            cake_vol += (math.pow(int(order[f'tier{i+1}_size_a']), 2)) * int(order[f'tier{i+1}_size_b'])
        if order['cake_shape'] == 'Heart':
            cake_vol += ((math.pow(((2*int(order[f'tier{i+1}_size_a']))/3), 2)+(math.pi*math.pow((int(order[f'tier{i+1}_size_a'])/3), 2))) * int(order[f'tier{i+1}_size_b']))

    global ingred_formula
    ingred_formula = {}

    ingred_formula_lbls = {
        'eggs': 4, 'milk': 160, 'oil/butter': 80, 'flour/sugar': 200, 'salt': 0.25,
        'baking powder': 1.5, 'vanilla extract': 1, 'cocoa powder': 40, 'ube extract': 2
    }

    for ingred, num in ingred_formula_lbls.items():
        if ingred == 'salt' or ingred == 'baking powder' or ingred == 'vanilla extract' or ingred == 'ube extract':
            print(((num*cake_vol)/(6*6*4)))
            if int((num*cake_vol)/(6*6*4)) == 0:
                ingred_formula[ingred] = Fraction(((num*cake_vol)/(6*6*4))).limit_denominator(4)
            else:
                if Fraction(((num*cake_vol)/(6*6*4))-int((num*cake_vol)/(6*6*4))).limit_denominator(4) == 1:
                    ingred_formula[ingred] = int((num*cake_vol)/(6*6*4))+1
                else:
                    ingred_formula[ingred] = f'{int((num*cake_vol)/(6*6*4))} {Fraction(((num*cake_vol)/(6*6*4))-int((num*cake_vol)/(6*6*4))).limit_denominator(4)}'
        else:
            ingred_formula[ingred] = round((num*cake_vol)/(6*6*4))
    print(cake_vol)

def create_header(content):
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
        f'{ingred_formula['eggs']} Eggs',
        f'{ingred_formula['milk']} ml of Milk',
        f'{ingred_formula['oil/butter']} ml of Cooking Oil',
        f'{ingred_formula['oil/butter']} g of Butter',
        f'{ingred_formula['flour/sugar']} g of Flour',
        f'{ingred_formula['flour/sugar']} g of Sugar',
        f'{ingred_formula['salt']} tsp of Salt',
        f'{ingred_formula['baking powder']} tsp of Baking Powder',
    ]

    if order['cake_flavour'] == 'Vanilla':
        ingredients_lbls.append(f'{ingred_formula['vanilla extract']} tsp of Vanilla Extract')
    if order['cake_flavour'] == 'Chocolate':
        ingredients_lbls.append(f'{ingred_formula['cocoa powder']} g of Cocoa Powder')
    if order['cake_flavour'] == 'Ube':
        ingredients_lbls.append(f'{ingred_formula['ube extract']} tsp of Ube Extract')

    for r in range(len(ingredients_lbls)):
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
        f'{order['cake_colours']} Icing'
    ]

    for i in range(int(order['tier_num'])):
        equipments_lbls.append(f'{order[f'tier{i+1}_size_a']}x{order[f'tier{i+1}_size_b']} {order['cake_shape']} Pan')

    for i in range(len(equipments_lbls)):
        frame = tk.Frame(content, width=180, height=30, bd=1.5, relief='groove', bg='#FEF8A0')
        frame.place(x=220, y=110+30*i)
        frame.pack_propagate(False)

        label = tk.Label(frame, text=equipments_lbls[i], font=('Arial', 12), bg='#FEF8A0')
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

    text = tk.Text(frame, font=('Arial', 12), bg='#FEF8A0', wrap='word')
    text.pack(fill='both', expand=True)
    text.insert(1.0, order['decor'])
    text.config(state='disabled')

stock_lbls = ['Eggs:', 'Milk:', 'Oil:', 'Butter:', 'Flour:', 'Sugar:', 'Salt:', 
              'Baking Powder:', 'Vanilla Extract:', 'Cocoa Powder:', 'Ube Extract:']

stock_ents = []

def create_inven_stock(content):
    stock_frame = tk.Frame(content, width=220, height=480)
    stock_frame.place(x=630, y=0)
    stock_frame.pack_propagate(False)

    stock_border = tk.Frame(stock_frame, width=1, height=480, bg='black')
    stock_border.place(x=0, y=0)

    frm_title = tk.Frame(stock_frame, width=180, height=40, bd=1.5, relief='groove', bg='#FFC957')
    frm_title.place(x=20, y=25)
    frm_title.pack_propagate(False)

    lbl_title = tk.Label(frm_title, text='Inventory Stock:', font=('Segoe Print', 12, 'bold'), bg='#FFC957')
    lbl_title.pack()

    for r in range(11):
        for c in range(2):
            frame = tk.Frame(stock_frame, width=90, height=30, bd=1.5, relief='groove')
            frame.place(x=20+90*c, y=65+30*r)
            frame.pack_propagate(False)

            if c == 0:
                frame.config(bg='#FEF8A0')

                label = tk.Label(frame, text=stock_lbls[r], font=('Arial', 12), bg='#FEF8A0')
                label.place(x=0, y=0)

    add_frm = tk.Frame(stock_frame, width=180, height=40, bd=1.5, relief='groove', bg='#FFC957')
    add_frm.place(x=20, y=415)
    add_frm.pack_propagate(False)

    add_btn = tk.Button(add_frm, text='Add to Inventory', font=('Segoe Print', 12), bg='#FFC957', command=lambda: add_stock())
    add_btn.pack(fill='both', expand=True)

def add_stock():
    add_root = tk.Toplevel()
    add_root.title('Add to Inventory')
    
    add_root_w = 220
    add_root_h = 480
    center_x = int((add_root.winfo_screenheight() / 2 - add_root_w / 2) + 450)
    center_y = int((add_root.winfo_screenheight() / 2 - add_root_h / 2) - 5)
    add_root.geometry(f'{add_root_w}x{add_root_h}+{center_x}+{center_y}')
    add_root.resizable(False, False)

    frm_title = tk.Frame(add_root, width=180, height=40, bd=1.5, relief='groove', bg='#FFC957')
    frm_title.place(x=20, y=25)
    frm_title.pack_propagate(False)
    
    lbl_title = tk.Label(frm_title, text='Add to Inventory:', font=('Segoe Print', 12, 'bold'), bg='#FFC957')
    lbl_title.pack()

    for r in range(11):
        for c in range(2):
            frame = tk.Frame(add_root, width=90, height=30, bd=1.5, relief='groove')
            frame.place(x=20+90*c, y=65+30*r)
            frame.pack_propagate(False)
    
            if c == 0:
                frame.config(bg='#FEF8A0')

                label = tk.Label(frame, text=stock_lbls[r], font=('Arial', 12), bg='#FEF8A0')
                label.place(x=0, y=0)

            elif c == 1:
                stock_ents.append(tk.Entry(frame, font=('Arial', 12)))
                stock_ents[r].pack(fill='both', expand=True)

    for i in range(2):
        frame = tk.Frame(add_root, width=85, height=40, bd=1.5, relief='groove', bg='#FFC957')
        frame.place(x=20+95*i, y=415)
        frame.pack_propagate(False)

        btn_lbls = ['Cancel', 'Confirm']
        btn_cmds = [add_root.destroy, add_to_stock]

        button = tk.Button(frame, text=btn_lbls[i], font=('Segoe Print', 12), bg='#FFC957', command=lambda: btn_cmds[i]())
        button.pack(fill='both', expand=True)

    add_root.mainloop()

stock_save_lbls = ['eggs', 'milk', 'oil', 'butter', 'flour', 'sugar', 'salt',
                   'baking_powder', 'vanilla_extract', 'cocoa_powder', 'ube_extract']

def add_to_stock():
    for i in range(11):
        stock[stock_save_lbls[i]] = int(stock[stock_save_lbls[i]]) + int(stock_ents[i])