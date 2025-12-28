import requests
from bs4 import BeautifulSoup

class WebScrapping:
    def __init__(self,url):
        self.url = url
        self.ids = []
        self.response = requests.get(self.url)
        
        if self.response.status_code == 200:
            self.soup = BeautifulShop(response.text,'html.parser')
            self.juegos = soup.find_all('div', class_='app')
            print(self.juegos)
            
            for self.juego in self.juegos:
                appid = (juego.get('data-appid')
                        or juego.get('data-app-id')
                        or juego.get('data-ds-appid')
                        or juego.get('data-appID'))
                # buscar cualquier atributo que contenga 'appid' si no lo encontramos
                if not appid:
                    for attr_name, attr_value in juego.attrs.items():
                        if 'appid' in attr_name.lower():
                            appid = attr_value
                            break
                if appid:
                    self.ids.append(appid)
    
    def imprimir_ids(self):

    
    def guardar_json(self):
        pass
    
    
if __name__ == "__main__":
    url = input("Ingrese la URL de la página a scrapear: ")
    scraper_trending = WebScrapping(url)
    scraper_trending.imprimir_ids()
    

