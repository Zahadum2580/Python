from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.geometry(r'200x60+700+300')
root.resizable(False, False)

def tick():
    watch.after(200, tick)
    watch['text'] = time.strftime('%H:%M:%S')

watch = ttk.Label(root, font='Arail 36')
watch.pack()
tick()

root.mainloop()