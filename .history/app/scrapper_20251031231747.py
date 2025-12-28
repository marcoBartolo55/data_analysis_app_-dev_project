import requests
from bs4 import BeautifulSoup

class WebScrapping:
    def __init__(self,url):
        self.url = url
        self.headers = {
            # ¡CLAVE! Usa un User-Agent de un navegador real (ej. Chrome)
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
            # Puedes añadir otros encabezados si el sitio los requiere:
            # 'Accept-Language': 'es-ES,es;q=0.9',
            # 'Referer': 'https://www.google.com/', 
        }
        
        '''
        #! Código incorrecto, pendiente de correción
        self.ids = []
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
        try:
            resp = requests.get(self.url, ,timeout=10)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f'Request error: {e}')
            
    
    #? Método funcional, con opción a quedarse o no
    '''
    def imprimir_ids(self):
        if not self.ids:
            print("No se encontraron ids.")
            return
        for id_ in self.ids:
            print(id_)
    #? Método pendiente de implementar, cuando este funcional la creación del objeto
    def guardar_json(self):
        pass
    '''
    
if __name__ == "__main__":
    # url = input("Ingrese la URL de la página a scrapear: ").strip()
    url = "https://steamdb.info/stats/trendingfollowers/"
    scraper_trending = WebScrapping(url)
    print(scraper_trending)
    

