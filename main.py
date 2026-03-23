from extractor import extraer_productos
import pandas as pd
import os

def iniciar_scraping():
    #URL de una categoria específica (ejemplo: almacén)
    url_objetivo = "https://www.comodinencasa.com.ar/almacen"
    
    print("Inicio de web scraper de mercado...")
    
    datos = extraer_productos(url_objetivo)
    
    if datos:
        df = pd.DataFrame(datos)
        
        #crear carpeta de salida si no existe
        os.makedirs("data/output", exist_ok = True)
        
        #guardar el bruto (sucio) para que luego lo limpie el otro script
        ruta_salida = "data/output/datos_comodin_sucio.xlsx"
        df.to_excel(ruta_salida, index = False)
        
        print(f"¡Se encontraron {len(df)} productos exitosamente.")
        print(f"Archivo guardado en: {ruta_salida}")
    else:
        print(" No se pudieron obtener datos. Revisar selectores HTML.")
        
if __name__ == "__main__":
    iniciar_scraping()
        