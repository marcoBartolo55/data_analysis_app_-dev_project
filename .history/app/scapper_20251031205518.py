import requests
from bs4 import BeautifulSoup

class WebScrapping:
    def __init__(self,url):
        self.url = ''
    
    def obtener_html(self):
        pass
    
    def analizar_datos(self):
        pass
    
    
if __name__ == "__main__":
    url = "https://example.com"
    scraper = WebScrapping(url)
    html_content = scraper.obtener_html()
    datos_analizados = scraper.analizar_datos()
    print(datos_analizados)

