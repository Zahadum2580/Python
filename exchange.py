from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import urllib.request
import json

root = Tk()
root.title(r'Currency Exchange')
root.geometry(r'300x350+700+300')
root.resizable(False, False)

START_VALUE = 1000
    
def get_exchange(exc_url):
    try:
        exc_data = urllib.request.urlopen(exc_url).read()
        JSON_object = json.loads(exc_data)
        usd_buy['text'] = JSON_object['Valute']['USD']['Value']
        usd_sell['text'] = JSON_object['Valute']['USD']['Previous']
        eur_buy['text'] = JSON_object['Valute']['EUR']['Value']
        eur_sell['text'] = JSON_object['Valute']['EUR']['Previous']
        cny_buy['text'] = JSON_object['Valute']['CNY']['Value']
        cny_sell['text'] = JSON_object['Valute']['CNY']['Previous']
    except:
        messagebox.showerror('Error', 'Datas are unavailable!')

def exchange_sell():
    head_value['text'] = int(exc_text.get())
    usd_value['text'] = format(float(usd_buy['text']) * int(head_value['text']), '.4f')
    eur_value['text'] = format(float(eur_buy['text']) * int(head_value['text']), '.4f')
    cny_value['text'] = format(float(cny_buy['text']) * int(head_value['text']) / 10, '.4f')
    
def exchange_buy():
    head_value['text'] = int(exc_text.get())
    usd_value['text'] = format(float(usd_sell['text']) * int(head_value['text']), '.4f')
    eur_value['text'] = format(float(eur_sell['text']) * int(head_value['text']), '.4f')
    cny_value['text'] = format(float(cny_sell['text']) * int(head_value['text']) / 10, '.4f')
    
# header frame
head_frame = ttk.LabelFrame(root, text='Currency')
head_frame.place(anchor=NW, rely=.01, relx=.03, height=40, relwidth=.94)
head_buy = ttk.Label(head_frame, text='Buy', anchor=CENTER)
head_buy.place(anchor=NW, relheight=.75, relwidth=0.3, relx=0)
head_sell = ttk.Label(head_frame, text='Sell', anchor=CENTER)
head_sell.place(anchor=NW, relheight=.75, relwidth=0.3, relx=.25)
head_value = ttk.Label(head_frame, text=f'{START_VALUE}', anchor=CENTER)
head_value.place(anchor=NW, relheight=.75, relwidth=0.3, relx=.6)

# USD frame
usd_frame = ttk.LabelFrame(root, text=r'USD x 1')
usd_frame.place(anchor=NW, rely=.16, relx=.03, height=40, relwidth=.94)
usd_buy = ttk.Label(usd_frame, text='', anchor=CENTER)
usd_buy.place(anchor=NW, relheight=.75, relwidth=0.3, relx=0)
usd_sell = ttk.Label(usd_frame, text='', anchor=CENTER)
usd_sell.place(anchor=NW, relheight=.75, relwidth=0.3, relx=.25)
usd_value = ttk.Label(usd_frame, text='', anchor=CENTER)
usd_value.place(anchor=NW, relheight=.75, relwidth=0.3, relx=.6)

# EUR frame
eur_frame = ttk.LabelFrame(root, text=r'EUR x 1')
eur_frame.place(anchor=NW, rely=.31, relx=.03, height=40, relwidth=.94)
eur_buy = ttk.Label(eur_frame, text='', anchor=CENTER)
eur_buy.place(anchor=NW, relheight=.75, relwidth=0.3, relx=.0)
eur_sell = ttk.Label(eur_frame, text='', anchor=CENTER)
eur_sell.place(anchor=NW, relheight=.75, relwidth=0.3, relx=.25)
eur_value = ttk.Label(eur_frame, text='', anchor=CENTER)
eur_value.place(anchor=NW, relheight=.75, relwidth=0.3, relx=.6)

# CNY frame
cny_frame = ttk.LabelFrame(root, text=r'CNY x 10')
cny_frame.place(anchor=NW, rely=.46, relx=.03, height=40, relwidth=.94)
cny_buy = ttk.Label(cny_frame, text='', anchor=CENTER)
cny_buy.place(anchor=NW, relheight=.75, relwidth=0.3, relx=0)
cny_sell = ttk.Label(cny_frame, text='', anchor=CENTER)
cny_sell.place(anchor=NW, relheight=.75, relwidth=0.3, relx=.25)
cny_value = ttk.Label(cny_frame, text='', anchor=CENTER)
cny_value.place(anchor=NW, relheight=.75, relwidth=0.3, relx=.6)

# exchange frame
exc_frame = ttk.LabelFrame(root, text=r'Exchage:')
exc_frame.place(anchor=NW, rely=.61, relx=.03, height=100, relwidth=.94)

exc_text = Entry(exc_frame)
exc_text.place(relx=.5, rely=.2, height=25, relwidth=0.95, anchor=CENTER)
exc_text.insert(0, '1000')

sell_button = ttk.Button(exc_frame, text=f'SELL', command=lambda: exchange_sell())
sell_button.place(anchor=NW, height=40, relwidth=0.3, relx=0.02, rely=0.45)

get_button = ttk.Button(exc_frame, text='GET INFO', command=lambda: get_exchange('https://www.cbr-xml-daily.ru/daily_json.js'))
get_button.place(anchor=CENTER, height=40, relwidth=0.3, relx=0.5, rely=0.69)

buy_button = ttk.Button(exc_frame, text=f'BUY', command=lambda: exchange_buy())
buy_button.place(anchor=NW, height=40, relwidth=0.3, relx=.68, rely=0.45)

root.mainloop()