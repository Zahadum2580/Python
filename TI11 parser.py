from bs4 import BeautifulSoup
import urllib.request

class Team:
    def __init__(self):
        self.__name = ''
        self.__crew = []
        self.url = ''
        
    def team_print(self, n = 1):
        print(f'Команда: {self.__name}')
        for i in self.__crew:
            print(f'\t{n}. {i}.')
            n += 1
        print(f'\t   URL: {self.url}')
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = str(value.upper())
        
    @property
    def crew(self):
        return self.__crew
        
    @crew.setter
    def crew(self, value):
        for i in value:
            self.__crew.append(i)
    
    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, value):
        self.__url = str(value.upper())
                              
req = urllib.request.urlopen('https://www.cybersport.ru/tournaments/dota-2/the-international-2022')
cs_html = req.read()
cs_soup = BeautifulSoup(cs_html, 'html.parser')
d2_players = cs_soup.find_all('div', class_='root_RxXkH')
for crew in d2_players:
    team = crew.find('div', class_='title_CEMJJ').get_text(strip=True)
    team_n = crew.find('div', class_='title_CEMJJ').get_text(strip=True)
    team = Team()
    team.name = team_n
    link = crew.a.get('href')
    team.url = link
    # print(f'{team.upper()}: [{link}]')
    players = crew.find_all('div', class_='name_+Gu6V')
    x = 1
    for doter in players:
        # print(f'\t {x}. {doter.get_text().upper()}')
        pro_player = doter.get_text()
        team.crew.append(pro_player.upper())
        x += 1
    print(team.name)
    print(team.crew)
    print(team.url)
    team.team_print()
    print()