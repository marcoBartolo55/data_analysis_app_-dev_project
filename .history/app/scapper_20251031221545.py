import requests
from bs4 import BeautifulSoup

class WebScrapping:
    def __init__(self,url):
        self.url = url
        self.ids = []
        self.response = requests.get(self.url)
        
        '''
        if self.response.status_code == 200:
            self.soup = BeautifulShop(response.text,'html.parser')
            self.juegos = soup.find_all('tr', class_='app')
            self.id_juego = self.juegos.split("'")[1]
            
            for self.juego in self.juegos:
                if self.id_juego:
                    self.ids.append(self.id_juego)
                if not self.id_juego:
                    continue
        '''         
    
    def imprimir_ids(self):
        if not self.ids:
            print("No se encontraron ids.")
            return
        for id_ in self.ids:
            print(id_)
    
    def guardar_json(self):
        pass
    
    
if __name__ == "__main__":
    # url = input("Ingrese la URL de la página a scrapear: ").strip()
    url = "https://steamdb.info/stats/trendingfollowers/"
    scraper_trending = WebScrapping(url)
    scraper_trending.imprimir_ids()
    

