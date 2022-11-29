from tkinter import *
from tkinter import ttk # кнопки под ОС стиль

root = Tk() # root - так договорились
root.config(bg='#FFE4B5') # цвет фона
root.geometry('220x220+550+50') # размеры и место появления
root.resizable(False, False) # запрет resize окна по-диагонали и вертикали
root.title('Rainbow')
root.iconbitmap(r'C:\IT Tools\Test\Icons\sunny.ico')
   
label_color = Label(root)
label_color.pack(fill=X)
entry_color = Entry(root, justify=CENTER)
entry_color.pack(fill=X)

colors = {
    '#FF0000': 'Красный',
    '#FF7D00': 'Оранжевый',
    '#FFFF00': 'Желтый',
    '#00FF00': 'Зеленый',
    '#007DFF': 'Голубой',
    '#0000FF': 'Синий',
    '#7D00FF': 'Фиолетовый'
}

class MyButton:
    
    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.button = Button(master, bg=hex_color, command=self.paint)
        self.button.pack(fill=X)
        
    def paint(self):
        label_color['text'] = self.text_color
        entry_color.delete(0, END)
        entry_color.insert(END, self.hex_color)

for code, name in colors.items():
    MyButton(root, name, code)

root.mainloop()