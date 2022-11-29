import requests

def get_data(link): # заполняям верхнее поле, основываясь на геолокации
    try:
        data = requests.get(link).json()
        en_city = data[0]['name']
        ru_city = data[0]['local_names']['ru']
        lat = data[0]['lat']
        lon = data[0]['lon']
        print(f'{en_city} - LAT:{lat} LON:{lon}')
    except:
        print(f'DATA NOT COLLECTED')
    
spb_link = f'http://api.openweathermap.org/geo/1.0/direct?q=spe,rus&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(spb_link)

mos_link = f'http://api.openweathermap.org/geo/1.0/direct?q=moscow&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(mos_link)

lnd_link = f'http://api.openweathermap.org/geo/1.0/direct?q=london&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(lnd_link)

tok_link = f'http://api.openweathermap.org/geo/1.0/direct?q=tokyo&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(tok_link)

paris_link = f'http://api.openweathermap.org/geo/1.0/direct?q=paris&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(paris_link)

ber_link = f'http://api.openweathermap.org/geo/1.0/direct?q=berlin&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(ber_link)

rom_link = f'http://api.openweathermap.org/geo/1.0/direct?q=rome&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(rom_link)

ny_link = f'http://api.openweathermap.org/geo/1.0/direct?q=new-york&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(ny_link)

la_link = f'http://api.openweathermap.org/geo/1.0/direct?q=los-angeles,us-ca,usa&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(la_link)

beij_link = f'http://api.openweathermap.org/geo/1.0/direct?q=beijing&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(beij_link)

mum_link = f'http://api.openweathermap.org/geo/1.0/direct?q=mumbai&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(mum_link)

ist_link = f'http://api.openweathermap.org/geo/1.0/direct?q=istanbul&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(ist_link)

seo_link = f'http://api.openweathermap.org/geo/1.0/direct?q=seoul&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(seo_link)

syd_link = f'http://api.openweathermap.org/geo/1.0/direct?q=sydney&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(syd_link)

cape_link = f'http://api.openweathermap.org/geo/1.0/direct?q=cape-town&appid=9b403fea7b8b325bf888172b1ed1919c'
get_data(cape_link)