import streamlit as st
import requests
from datetime import datetime, timedelta

# 1. Configuración de la página (Modo oscuro/claro automático y ancho completo)
st.set_page_config(page_title="Financial News Terminal", layout="wide")

# 2. Estilos CSS Personalizados para un look profesional
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .news-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-top: 4px solid #007bff;
    }
    .source-tag {
        background-color: #e7f3ff;
        color: #007bff;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONFIGURACIÓN API ---
API_KEY = 'd5sffo1r01qks02d3mt0d5sffo1r01qks02d3mtg' # Coloca tu llave de Finnhub

def fetch_news(ticker):
    hoy = datetime.now().strftime('%Y-%m-%d')
    hace_3_dias = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
    url = f'https://finnhub.io/api/v1/company-news?symbol={ticker}&from={hace_3_dias}&to={hoy}&token={API_KEY}'
    try:
        response = requests.get(url)
        return response.json()
    except:
        return []

# --- INTERFAZ ---
st.title("🗞️ Terminal de Noticias Financieras")
st.markdown("Monitoreo en tiempo real de sentimiento de mercado.")

# Barra lateral
st.sidebar.header("Panel de Control")
tickers_input = st.sidebar.text_input("Ingresa Tickers (ej: NVDA, AAPL, BTC-USD):", "NVDA, AAPL")
tickers = [t.strip().upper() for t in tickers_input.split(",")]

# Mostrar noticias por ticker
for ticker in tickers:
    st.subheader(f"Últimas noticias de {ticker}")
    noticias = fetch_news(ticker)
    
    if not noticias:
        st.info(f"No se encontraron noticias recientes para {ticker}.")
        continue

    # Creamos una fila de 3 columnas para las noticias
    cols = st.columns(3)
    
    for i, n in enumerate(noticias[:6]): # Limitamos a las 6 más recientes
        with cols[i % 3]: # Distribuye las noticias en las 3 columnas
            with st.container():
                # Contenedor con estilo de tarjeta
                st.markdown(f"""
                <div class="news-card">
                    <span class="source-tag">{n['source']}</span>
                    <p style="margin-top:10px; font-weight:bold; font-size:1.1rem;">{n['headline']}</p>
                    <p style="font-size:0.9rem; color: #666;">{n['summary'][:150]}...</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Imagen opcional si existe
                if n.get('image'):
                    st.image(n['image'], use_container_width=True)
                
                # Botón de enlace
                st.link_button(f"Leer en {n['source']}", n['url'], use_container_width=True)
    st.markdown("---")