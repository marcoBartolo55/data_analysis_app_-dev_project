import requests
from bs4 import BeautifulSoup

class WebScrapping:
    def __init__(self,url):
        ids = []
        self.url = url
        self.response = requests.get(self.url)
        
        if self.response.status_code == 200:
            self.soup = BeautifulShop(response.text,'html.parser')
            self.juegos = soup.find_all('div', class_='app')
            print(self.juegos)
            
            for self.juego in self.juegos:
                self.id = self.juego[data-appid]
                ids.append
        return 
    
    def guardar_json(self):
        pass
    
    
if __name__ == "__main__":
    url = input("Ingrese la URL de la página a scrapear: ")
    scraper = WebScrapping(url)
    

