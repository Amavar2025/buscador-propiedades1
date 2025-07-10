import streamlit as st
import pandas as pd

# Scrapers simulados (importa los reales cuando estén listos)
import metrocuadrado
import properati
import finca_raiz
import ciencuadras
import lahaus
import olx
import londono
import onegrupo
import acrecer
import albertoalvarez
import conaltura
import mabelochoa
import umbral

st.set_page_config(page_title="Buscador Inmobiliario Medellín", layout="wide")
st.title("🏠 Buscador de Propiedades en Medellín")

# Filtros
st.sidebar.header("🔎 Filtros de búsqueda")
portales = st.sidebar.multiselect("Selecciona portales:", [
    "Metrocuadrado", "Properati", "Finca Raíz", "Ciencuadras", "La Haus",
    "OLX", "Londoño Gómez", "Acrecer", "Alberto Álvarez", "Conaltura",
    "One Grupo", "Mabel Ochoa", "Umbral"
], default=["Metrocuadrado", "Properati"])

barrio = st.sidebar.text_input("Barrio o sector", "Castropol")
habitaciones = st.sidebar.slider("Habitaciones mínimas", 1, 6, 2)
precio_max = st.sidebar.number_input("Precio máximo (millones)", 100, 5000, 1000)

if st.sidebar.button("🔍 Buscar propiedades"):
    resultados = []

    if "Metrocuadrado" in portales:
        resultados += metrocuadrado.buscar(barrio, habitaciones, precio_max)
    if "Properati" in portales:
        resultados += properati.buscar(barrio, habitaciones, precio_max)
    if "Finca Raíz" in portales:
        resultados += finca_raiz.buscar(barrio, habitaciones, precio_max)
    if "Ciencuadras" in portales:
        resultados += ciencuadras.buscar(barrio, habitaciones, precio_max)
    if "La Haus" in portales:
        resultados += lahaus.buscar(barrio, habitaciones, precio_max)
    if "OLX" in portales:
        resultados += olx.buscar(barrio, habitaciones, precio_max)
    if "Londoño Gómez" in portales:
        resultados += londono.buscar(barrio, habitaciones, precio_max)
    if "One Grupo" in portales:
        resultados += onegrupo.buscar(barrio, habitaciones, precio_max)
    if "Acrecer" in portales:
        resultados += acrecer.buscar(barrio, habitaciones, precio_max)
    if "Alberto Álvarez" in portales:
        resultados += albertoalvarez.buscar(barrio, habitaciones, precio_max)
    if "Conaltura" in portales:
        resultados += conaltura.buscar(barrio, habitaciones, precio_max)
    if "Mabel Ochoa" in portales:
        resultados += mabelochoa.buscar(barrio, habitaciones, precio_max)
    if "Umbral" in portales:
        resultados += umbral.buscar(barrio, habitaciones, precio_max)

    if resultados:
        df = pd.DataFrame(resultados)
        st.success(f"Se encontraron {len(df)} propiedades")
        st.dataframe(df)
    else:
        st.warning("No se encontraron propiedades con esos filtros.")
else:
    st.info("Usa los filtros de la barra lateral y haz clic en 'Buscar propiedades'.")

