# Web Scraper Supermercado (MVP)

**Scraper de Datos** desarrollado en Python para automatizar la extracción de precios y productos, en este caso del supermercado **Comodín**. 

Utiliza **Selenium** con motor Chromium (Brave/Chrome) para manejar contenido dinámico y scroll automático.

## Funcionalidades
- Navegación automatizada con soporte para JavaScript.
- Extracción de nombres y precios de más de 200 productos por categoría.
- Exportación automática a formato **Excel (.xlsx)**.
- Modo *Headless* configurable para ejecución en segundo plano.

## Tecnologías
- **Python 3.x**
- **Selenium WebDriver**
- **Pandas** (para gestión de datos)
- **Brave Browser** (Motor Chromium)

## Instalación y Configuración
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/web-scraper-supermercado.git](https://github.com/tu-usuario/web-scraper-supermercado.git)

2. Instalar dependencias:
    pip install -r requeriments.txt

3. Descargar el chromedriver.exe correspondiente a su versión de navegador y colocarlo en la raíz del proyecto.

## Estructura de salida
Los datos se guardan en: data/output/datos_comodin_sucio.xlsx