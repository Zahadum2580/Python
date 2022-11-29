from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import requests
import time

root = Tk()

API_KEY = '9b403fea7b8b325bf888172b1ed1919c' # мой API ключ
geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q=spe,rus&appid={API_KEY}' # получаем данные по текущему местоположению (городу)

# окно приложения
root.title(r'Weather')
root.geometry(r'300x350+700+300')
root.resizable(False, False)

# верхняя рамка
CurrentLocation_LabelFrame = ttk.LabelFrame(root, text='CURRENT LOCATION :')
CurrentLocation_LabelFrame.place(anchor=CENTER, rely=.07, relx=.5, height=45, relwidth=.9)
# вставка
CurrentLocation_Label = ttk.Label(CurrentLocation_LabelFrame, text='Local Data', anchor=CENTER)
CurrentLocation_Label.place(anchor=CENTER, rely=.5, relx=.5, relheight=.9, relwidth=.98)

# комбобокс
Location_Combobox = ttk.Combobox(root,  state='readonly', justify=CENTER)
Location_Combobox.place(anchor=CENTER, rely=.195, relx=.5, height=25, relwidth=.9)

def get_data(link): # заполняям верхнее поле, основываясь на геолокации
    data = requests.get(link).json()
    en_city = data[0]['name']
    ru_city = data[0]['local_names']['ru']
    lat = data[0]['lat']
    lon = data[0]['lon']
    country = data[0]['country']
    current_location = (f'LOCAL: {en_city.upper()} - {country.upper()}')
    CurrentLocation_Label['text']=f'{en_city.upper()} [{country.upper()}] - {round(lat, 4)} / {round(lon, 4)}'
    location_list = ['MOSCOW - RUS', 'LONDON - UK', 'TOKYO - JPN', 'PARIS - FRA', 'BERLIN - DEU', 'ROME - ITA', 'NEW YORK - USA', 'LOS ANGELES - USA', 'BEIJING - CHN', 'MUMBAI - IND', 'ISTANBUL - TUR', 'SEOUL - KOR', 'SYDNEY - AUS', 'CAPE TOWN - ZAF']
    location_list.insert(0, current_location)
    Location_Combobox['values']=tuple(location_list) # создаём комбобокс с нашей геолокацией

get_data(geo_url)

Location_Combobox.current(0)

def get_geo(city):
    data = requests.get().json()

def fill_weather(event):
    location = Location_Combobox.get()
    if location[0:5] == 'LOCAL':
        print(f'Combobox - LOCAL - triggered')
        get_weather(59.938732, 30.316229)
    elif location =='MOSCOW - RUS':
        get_weather(55.7504461, 37.6174943)
    elif location =='LONDON - UK':
        get_weather(51.5073219, -0.1276467)
    elif location =='TOKYO - JPN':
        get_weather(35.6828387, 139.7594549)
    elif location =='PARIS - FRA':
        get_weather(48.8588897, 2.3200410)
    elif location =='BERLIN - DEU':
        get_weather(52.5170365, 13.3888599)
    elif location =='ROME - ITA':
        get_weather(41.893203, 12.4829321)
    elif location =='NEW YORK - USA':
        get_weather(40.7127281, -74.0060152)
    elif location =='LOS ANGELES - USA':
        get_weather(34.0536909, -118.242766)
    elif location =='BEIJING - CHN':
        get_weather(39.906217, 116.3912757)
    elif location =='MUMBAI - IND':
        get_weather(19.0785451, 72.878176)
    elif location =='ISTANBUL - TUR':
        get_weather(41.0091982, 28.9662187)
    elif location =='SEOUL - KOR':
        get_weather(37.5666791, 126.9782914)
    elif location =='SYDNEY - AUS':
        get_weather(-33.8698439, 151.2082848)
    elif location =='CAPE TOWN - ZAF':
        get_weather(-33.928992, 18.417396)
    else:
        messagebox.showerror('ERROR', '!!! LOCATION ERROR !!!')
 
Location_Combobox.bind('<<ComboboxSelected>>', fill_weather)

# нижняя рамка
MainFrame_LabelFrame = ttk.LabelFrame(root, text='WEATHER :')
MainFrame_LabelFrame.place(anchor=CENTER, rely=.6, relx=.5, height=255, relwidth=.9)
# вставка
Temp_LabelFrame = ttk.LabelFrame(MainFrame_LabelFrame, text='TEMP :')
Temp_LabelFrame.place(anchor=CENTER, rely=.08, relx=.5, height=35, relwidth=.98)
Temp_Label = Label(Temp_LabelFrame, anchor=CENTER)
Temp_Label.place(anchor=CENTER, rely=0.25, relx=.5, relheight=.7, relwidth=.95)
Sky_LabelFrame = ttk.LabelFrame(MainFrame_LabelFrame, text='SKY :')
Sky_LabelFrame.place(anchor=CENTER, rely=.24, relx=.5, height=35, relwidth=.98)
Sky_Label = Label(Sky_LabelFrame, anchor=CENTER)
Sky_Label.place(anchor=CENTER, rely=0.25, relx=.5, relheight=.7, relwidth=.95)
Wind_LabelFrame = ttk.LabelFrame(MainFrame_LabelFrame, text='WIND :')
Wind_LabelFrame.place(anchor=CENTER, rely=.40, relx=.5, height=35, relwidth=.98)
Wind_Label = Label(Wind_LabelFrame, anchor=CENTER)
Wind_Label.place(anchor=CENTER, rely=0.25, relx=.5, relheight=.7, relwidth=.95)
HumPre_LabelFrame = ttk.LabelFrame(MainFrame_LabelFrame, text='HUMIDITY / AIR PRESSURE :')
HumPre_LabelFrame.place(anchor=CENTER, rely=.56, relx=.5, height=35, relwidth=.98)
HumPre_Label = Label(HumPre_LabelFrame, anchor=CENTER)
HumPre_Label.place(anchor=CENTER, rely=0.25, relx=.5, relheight=.7, relwidth=.95)
Sun_LabelFrame = ttk.LabelFrame(MainFrame_LabelFrame, text='SUNRISE & SUNSET :')
Sun_LabelFrame.place(anchor=CENTER, rely=.72, relx=.5, height=35, relwidth=.98)
Sun_Label = Label(Sun_LabelFrame, anchor=CENTER)
Sun_Label.place(anchor=CENTER, rely=0.25, relx=.5, relheight=.7, relwidth=.95)
Coord_LabelFrame = ttk.LabelFrame(MainFrame_LabelFrame, text='LOCATION :')
Coord_LabelFrame.place(anchor=CENTER, rely=.88, relx=.5, height=35, relwidth=.98)
Coord_Label = Label(Coord_LabelFrame, anchor=CENTER)
Coord_Label.place(anchor=CENTER, rely=0.25, relx=.5, relheight=.7, relwidth=.95)

def get_weather(lat, lon):
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}'   #
    weather_data = requests.get(weather_url).json()                                                                     #
    temp = weather_data['main']['temp']                                                                                 #
    feels_like = weather_data['main']['feels_like']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']
    sky = weather_data['weather'][0]['main']
    sky_des = weather_data['weather'][0]['description']
    wind_s = weather_data['wind']['speed']
    wind_d = weather_data['wind']['deg']
    hum = weather_data['main']['humidity']
    pre = weather_data['main']['pressure']
    sunrise = time.strftime('%H:%M:%S', time.localtime(weather_data['sys']['sunrise']))
    sunset = time.strftime('%H:%M:%S', time.localtime(weather_data['sys']['sunset']))
    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']
    Temp_Label['text'] = f'T:{temp}  F:{feels_like}  MAX:{temp_max}  MIN:{temp_min}'
    Sky_Label['text'] = f'SKY: {sky.upper()}    ({sky_des.upper()})'
    Wind_Label['text'] = f'WIND {wind_s} M/S - DEG: {wind_d}'
    HumPre_Label['text'] = f'HUMIDITY: {hum}    PRESSURE: {pre}'
    Sun_Label['text'] = f'SUNRISE: {sunrise}   SUNSET: {sunset}'
    Coord_Label['text'] = f'LATITUDE: {round(lat,4)}    LONGTITUDE: {round(lon, 4)}'
    
get_weather(59.938732, 30.316229)

root.mainloop()