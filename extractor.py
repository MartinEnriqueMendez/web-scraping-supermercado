import requests
from bs4 import BeautifulSoup
import pandas as pd

def extraer_productos(url):
    # El user-agent es nuestro "disfraz" de navegador humano
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        print(f"--- Solicitando datos de: {url}---")
        response = requests.get(url, headers=headers)
        response.raise_for_status() #lanza error si la web no responde bien
        
        sopa = BeautifulSoup(response.text, 'html.parser')
        
        #lista para guardar lo que no encontramos
        lista_productos = []
        
        
        # Buscamos los contenedores (Ajustar las clases según la inspección)
        # Nota: VTEX (la plataforma de Comodin) usa clases largas.
        productos = sopa.find_all('div', class_='vtex-search-result-3-x-galleryItem')
        
        for p in productos:
            # Extraemos el nombre
            nombre = p.find('span', class_='vtex-product-summary-2-x-brandName')
            nombre = nombre.text.strip() if nombre else "N/A"
            
            # Extraemos el precio
            precio = p.find('span', class_= 'vtex-product-summary-2-x-currencyContainer')
            precio = precio.text.strip() if precio else "0"
            
            lista_productos.append({
                "Producto": nombre,
                "Precio_Original": precio,
                "Tienda": "Comodin"
            })
        return lista_productos
    
    except Exception as e:
        print(f"Error en la extracción: {e}")
        return []
            