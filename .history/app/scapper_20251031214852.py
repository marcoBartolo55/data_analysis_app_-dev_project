import requests
from bs4 import BeautifulSoup

class WebScrapping:
    def __init__(self,url):
        self.url = 'https://steamdb.info/stats/trendingfollowers/'
        self.response = request.get(self.url)
        
        if self.response.status_code == 200:
            self.soup = BeautifulShop(response.text,'html.parser')
            self.juegos = soup.find_all('div', class_='app')
            print(self.juegos)
            
            for self.juego in self.
            
    
    def guardar_json(self):
        pass
    
    
if __name__ == "__main__":
    url = input("Ingrese la URL a scrapear: ")
    scraper = WebScrapping(url)
    

