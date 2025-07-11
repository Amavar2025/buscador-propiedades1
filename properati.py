
import requests
from bs4 import BeautifulSoup

def buscar(barrio, habitaciones, precio_max):
    # Normalizar los datos de entrada
    barrio_slug = barrio.lower().replace(" ", "-")
    url = f"https://www.properati.com.co/s/medellin/{barrio_slug}/apartamento/venta"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        propiedades = []

        for card in soup.select("div.listing-card"):
            titulo = card.select_one("h2")
            precio = card.select_one(".price")
            link = card.select_one("a")

            if titulo and precio and link:
                propiedades.append({
                    "Título": titulo.get_text(strip=True),
                    "Habitaciones": habitaciones,
                    "Precio (millones)": precio_max,
                    "Fuente": "Properati",
                    "Link": "https://www.properati.com.co" + link["href"],
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
