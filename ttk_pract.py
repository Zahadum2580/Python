from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk

root = Tk()
root.geometry('400x300+700+300')

def addto_combobox():
    text = entry_2.get()
    list = []
    for i in select['values']:
        print(i)
        list.append(i)
    list.append(text)
    # print(list)
    # print(tuple(list))
    select['values'] = tuple(list)
    
s = ttk.Style()
s.theme_use('xpnative')

button_1 = ttk.Button(root, text='Button 1')
button_1.pack()

entry_1 = ttk.Entry(root)
entry_1.pack()

button_2 = ttk.Button(root, text='Button 2', command=lambda: addto_combobox())
button_2.pack()

entry_2 = ttk.Entry(root, width=40)
entry_2.pack()

select = ttk.Combobox(root, values=['Melee DPS', 'Tank', 'Caster', 'Ranged DPS', 'Support', 'Semi-support'], state='readonly')
select.pack()

select.current(0)

def popmsg(event):
    messagebox.showinfo('SELECTED', select.get())
# select.bind('<<ComboboxSelected>>', popmsg)

root.mainloop()