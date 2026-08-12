import tkinter as tk
import json
from calculations import *

def open_inventory(content):
    load_details(incoming_order)
    create_header(content)
    create_ingredients_table(content)
    create_equipments_table(content)
    create_decor_table(content)
    create_inven_stock(content)

def create_header(content):
    frm_header = tk.Frame(content, width=400, height=50, bd=1.5, relief='groove', bg='#FFC957')
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

    cf = 0
    if order['cake_flavour'] == 'vanilla':
        cf = 8
    if order['cake_flavour'] == 'chocolate':
        cf = 9
    if order['cake_flavour'] == 'ube':
        cf = 10

    for r in range(8):
        frame = tk.Frame(content, width=180, bd=1.5, relief='groove', bg='#FEF8A0')
        if r < 7:
            frame.config(height=30)
            frame.place(x=20, y=110+30*r)
        else:
            frame.config(height=47)
            frame.place(x=20, y=110+30*7+47*(r-7))
        frame.pack_propagate(False)

        label = tk.Label(frame, font=('Arial', 12), bg='#FEF8A0')
        if r == 8:
            label.config(text=f'{order[stock_save_lbls[r]]} {ingredients_lbls[cf]}')
        else:
            label.config(text=f'{order[stock_save_lbls[r]]} {ingredients_lbls[r]}')
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

def load_details(file_name):
    with open(f'{file_name}.json', 'r') as file:
        global order
        order = json.load(file)

def create_inven_stock(content):
    global stock_frame
    if stock_frame is not None:
        stock_frame.destroy()

    stock_frame = tk.Frame(content, width=220, height=480)
    stock_frame.place(x=630, y=0)
    stock_frame.pack_propagate(False)

    stock_border = tk.Frame(stock_frame, width=1, height=480, bg='black')
    stock_border.place(x=0, y=0)

    frm_title = tk.Frame(stock_frame, width=180, height=40, bd=1.5, relief='groove', bg='#FFC957')
    frm_title.place(x=20, y=18)
    frm_title.pack_propagate(False)

    lbl_title = tk.Label(frm_title, text='Inventory Stock:', font=('Segoe Print', 12, 'bold'), bg='#FFC957')
    lbl_title.pack()

    for r in range(11):
        for c in range(2):
            frame = tk.Frame(stock_frame, bd=1.5, relief='groove', bg='#FEF8A0')
            if c == 0:
                frame.config(width=110)
                if r < 7:
                    frame.config(height=30)
                    frame.place(x=20, y=58+30*r)
                else:
                    frame.config(height=47)
                    frame.place(x=20, y=58+30*6+47*(r-7))
                frame.pack_propagate(False)

                label = tk.Label(frame, text=stock_lbls[r], font=('Arial', 12), bg='#FEF8A0')
                label.place(x=0, y=0)

            elif c == 1:
                frame.config(width=70)
                if r < 7:
                    frame.config(height=30)
                    frame.place(x=130, y=58+30*r)
                else:
                    frame.config(height=47)
                    frame.place(x=130, y=58+30*6+47*(r-7))
                frame.pack_propagate(False)

                in_stock = tk.Label(frame, text=stock[stock_save_lbls[r]], font=('Arial', 12))
                in_stock.pack(fill='both', expand=True)

    add_frm = tk.Frame(stock_frame, width=180, height=40, bd=1.5, relief='groove', bg='#FFC957')
    add_frm.place(x=20, y=425)
    add_frm.pack_propagate(False)

    add_btn = tk.Button(add_frm, text='Add to Inventory', font=('Segoe Print', 12),
                        bg='#FFC957', command=lambda: add_stock(content))
    add_btn.pack(fill='both', expand=True)

def add_stock(content):
    add_root = tk.Toplevel()
    add_root.title('Add to Inventory')
    
    add_root_w = 220
    add_root_h = 480
    center_x = int((add_root.winfo_screenheight() / 2 - add_root_w / 2) + 450)
    center_y = int((add_root.winfo_screenheight() / 2 - add_root_h / 2) - 5)
    add_root.geometry(f'{add_root_w}x{add_root_h}+{center_x}+{center_y}')
    add_root.resizable(False, False)

    frm_title = tk.Frame(add_root, width=180, height=40, bd=1.5, relief='groove', bg='#FFC957')
    frm_title.place(x=20, y=18)
    frm_title.pack_propagate(False)
    
    lbl_title = tk.Label(frm_title, text='Add to Inventory:', font=('Segoe Print', 12, 'bold'), bg='#FFC957')
    lbl_title.pack()

    stock_ents.clear()

    for r in range(11):
        for c in range(2):
            frame = tk.Frame(add_root, bd=1.5, relief='groove', bg='#FEF8A0')
            if c == 0:
                frame.config(width=110)
                if r < 7:
                    frame.config(height=30)
                    frame.place(x=20, y=58+30*r)
                else:
                    frame.config(height=47)
                    frame.place(x=20, y=58+30*6+47*(r-7))
                frame.pack_propagate(False)

                label = tk.Label(frame, text=stock_lbls[r], font=('Arial', 12), bg='#FEF8A0')
                label.place(x=0, y=0)
        
            elif c == 1:
                frame.config(width=70)
                if r < 7:
                    frame.config(height=30)
                    frame.place(x=130, y=58+30*r)
                else:
                    frame.config(height=47)
                    frame.place(x=130, y=58+30*6+47*(r-7))
                frame.pack_propagate(False)
        
                stock_ents.append(tk.Entry(frame, font=('Arial', 12)))
                stock_ents[r].pack(fill='both', expand=True)

    for i in range(2):
        frame = tk.Frame(add_root, width=85, height=40, bd=1.5, relief='groove', bg='#FFC957')
        frame.place(x=20+95*i, y=425)
        frame.pack_propagate(False)

        btn_lbls = ['Cancel', 'Confirm']
        def btn_cmds(content, i):
            if i == 1:
                add_to_stock(content)

            add_root.destroy()

        button = tk.Button(frame, text=btn_lbls[i], font=('Segoe Print', 12), bg='#FFC957',
                           command=lambda i=i: btn_cmds(content, i))
        button.pack(fill='both', expand=True)

def add_to_stock(content):
    for i in range(11):
        if stock_ents[i].get() != '':
            stock[stock_save_lbls[i]] = stock[stock_save_lbls[i]] + int(stock_ents[i].get())

            with open('inventory_stock.json', 'w') as f:
                json.dump(stock, f, indent=4)

    create_inven_stock(content)