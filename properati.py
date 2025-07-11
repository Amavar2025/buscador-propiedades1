
import requests
from bs4 import BeautifulSoup

def buscar(barrio, habitaciones, precio_max):
    url = "https://www.properati.com.co/s/medellin/apartamento/venta"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        propiedades = []

        for card in soup.select("div.listing-card"):
            titulo_el = card.select_one("h2")
            precio_el = card.select_one(".price")
            link_el = card.select_one("a")

            if titulo_el and precio_el and link_el:
                titulo = titulo_el.get_text(strip=True)
                if barrio.lower() in titulo.lower():
                    propiedades.append({
                        "Título": titulo,
                        "Habitaciones": habitaciones,
                        "Precio (millones)": precio_max,
                        "Fuente": "Properati",
                        "Link": "https://www.properati.com.co" + link_el["href"],
                    })

        return propiedades

    except Exception as e:
        return [{
            "Título": f"Error al buscar en Properati: {str(e)}",
            "Habitaciones": "",
            "Precio (millones)": "",
            "Fuente": "Properati",
            "Link": ""
        }]
