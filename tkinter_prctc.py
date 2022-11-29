from tkinter import *

# root = Tk()
# root.geometry(r'300x200+1000+300')

# f_Top = Frame(root, padx=10, pady=10) # отступы по осям
# f_Top.pack(side=TOP, padx=10, pady=10) # тут тоже можно - внещние отступы
# f_Bottom = LabelFrame(root, text=r'Bottom LabelFrame', padx=10, pady=10)
# f_Bottom.pack(side=TOP, padx=10, pady=10)


# label_1 = Label(f_Top, text=r'1', font=15, fg=r'#fff', bg=r'#3498DB', width=8, height=4).pack(side=LEFT)
# label_2 = Label(f_Top, text=r'2', font=15, fg=r'#fff', bg=r'#2ECC71', width=8, height=4).pack(side=RIGHT)
# label_3 = Label(f_Bottom, text=r'3', font=15, fg=r'#fff', bg=r'#F1C40F', width=8, height=4).pack(side=LEFT)
# label_4 = Label(f_Bottom, text=r'4', font=15, fg=r'#fff', bg=r'#34495E', width=8, height=4).pack(side=RIGHT)

# root.mainloop()

# root = Tk()
# root.geometry(r'200x300+1000+300')

# frame = Frame(root)
# frame.pack(pady=10)

# buttons = {
#     '0': [3, 1],
#     '1': [2, 0],
#     '2': [2, 1],
#     '3': [2, 2],
#     '4': [1, 0],
#     '5': [1, 1],
#     '6': [1, 2],
#     '7': [0, 0],
#     '8': [0, 1],
#     '9': [0, 2]
# }

# class CalcButton:
    
#     def __init__(self, master, text, row, column):
#         self.text = text
#         self.row = row
#         self.column = column
#         self.button = Button(master, text=text, font=20, padx=10, pady=5)
#         self.button.grid(row=row, column=column)

# for text, pos in buttons.items():
#     CalcButton(frame, text, pos[0], pos[1])

# root.mainloop()

root = Tk()
root.geometry(r'400x400+700+300')

# label_1 = Label(root, text=r'Hello World!', bg=r'#3498DB', fg=r'#FFF', font=16, padx=10, pady=10)
# label_1.place(x=0, y=0, anchor=NW)

# label_2 = Label(root, text=r'Hello World!', bg=r'#3498DB', fg=r'#FFF', font=16, padx=10, pady=10)
# label_2.place(relx=.5, rely=.5, anchor=CENTER)

# btn_1 = Button(root, text=r'Кнопка №1', bg=r'#3498DB', fg=r'#FFF', font=16, padx=10, pady=10)
# btn_1.place(relx=.02, rely=.02, anchor=NW)

# btn_2 = Button(root, text=r'Кнопка №2', bg=r'#2ECC71', fg=r'#FFF', font=16, padx=10, pady=10)
# btn_2.place(relx=.5, rely=.5, anchor=CENTER)

# btn_3 = Button(root, text=r'Кнопка №3', bg=r'#F1C40F', fg=r'#FFF', font=16, padx=10, pady=10)
# btn_3.place(relx=.98, rely=.98, anchor=SE)

lab_mal = Label(root, text='', bg=r'#000000')
lab_mal.place(relx=.5, rely=.5, relheight=.75, relwidth=.75, anchor=CENTER)

root.mainloop() 