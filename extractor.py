import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def extraer_productos(url):
    # -- Configuración Headless --
    chrome_options = Options()
    # chrome_options.add_argument("--headless") #No abre la ventana del navegador
    #Ruta de brave
    chrome_options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") #
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    #cambio: apuntamos al archivo descargado
    ruta_driver = os.path.join(os.getcwd(), "chromedriver.exe")    
    service = Service(executable_path=ruta_driver)    
    driver = webdriver.Chrome(service=service, options = chrome_options) 
    
    lista_productos = []
    
    try:
        print(f"Abriendo navegador en segundo plano: {url}")
        driver.get(url)
        
        #Espera activa: esperamos 10 segundos a que aparezca un producto
        time.sleep(10)
                
        #Simulación de scroll
        #Comodin carga productos mientras bajás. Bajamos 3 veces.
        for i in range (3):
            print(f"Scroll nro {i+1}...")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5) # Pausa técnica para que el servidor responda
            
        #selectores robustos
        items = driver.find_elements(By.CLASS_NAME, "product-content")
        print(f"Elementos detectados: {len(items)}")
    
        for item in items:
            try:
                #buscamos cualquier elemento que en su clase diga 'brandName'
                nombre_el = item.find_element(By.TAG_NAME, "h5")
                nombre = nombre_el.text.strip()
                
                #extraemos el precio (se toma todo el texto del div de precio)
                #se usa .get_attribute('innerText') para evitar problemas con espacios ocultos
                precio_el = item.find_element(By.CLASS_NAME, "offer-price")
                precio_raw = precio_el.get_attribute('innerText')
                
                #limpiamos el texto
                precio_limpio = precio_raw.replace('\n', ' ').replace('\xa0', ' ').strip()
                
                #solo agregamos si tenemos nombre y precio
                if nombre and precio_limpio:
                    lista_productos.append({
                        "Producto": nombre,
                        "Precio_Original": precio_limpio, #se guarda el bloque para limpiar luego
                        "Tienda": "Comodin"
                    })
                
                #print(f"Capturado: {nombre}")
            

            except Exception as e:
                # print(f"Falla en un item: {e}") #Si un item falla, opcional para debug
                continue 
        
    except Exception as e:
        print(f"Error durante el scraping: {e}")
    finally:
        print("Cerrando navegador...")
        driver.quit() #Siempre cerrar el proceso del navegador
    
    return lista_productos