import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# --- CONFIGURACIÓN ---
TICKERS = ['AAPL', 'AMZN', 'QQQ', 'SPY', 'PLTR', 'M', 'V', 'AAL'] #Puedes cambiar los tickers a los que quieras
PERIOD_DATA = '1y' 
DIAS_PROYECCION = 90

def proyectar_con_bandas(ticker_simbolo):
    try:
        print(f"Calculando bandas de probabilidad para {ticker_simbolo}...")
        data = yf.download(ticker_simbolo, period=PERIOD_DATA)
        
        if data.empty: return

        # Preparación de datos
        df = data[['Close']].copy()
        df['Dias'] = np.arange(len(df))
        
        X = df[['Dias']].values
        y = df['Close'].values.reshape(-1, 1)
        
        # 1. Ajustar Regresión Lineal
        modelo = LinearRegression()
        modelo.fit(X, y)
        prediccion_entrenamiento = modelo.predict(X)
        
        # 2. Calcular el Error Estándar (Volatilidad)
        # Esto mide qué tanto se aleja el precio real de la línea de regresión
        error = y - prediccion_entrenamiento
        desviacion_estandar = np.std(error)
        
        # 3. Proyección a futuro
        ultimo_dia = df['Dias'].iloc[-1]
        dias_futuros = np.arange(ultimo_dia + 1, ultimo_dia + DIAS_PROYECCION + 1).reshape(-1, 1)
        linea_central = modelo.predict(dias_futuros)
        
        # Calcular bandas (Central +/- 2 Desviaciones Estándar)
        banda_superior = linea_central + (2 * desviacion_estandar)
        banda_inferior = linea_central - (2 * desviacion_estandar)
        
        # Fechas futuras
        ultima_fecha = df.index[-1]
        fechas_futuras = [ultima_fecha + timedelta(days=i) for i in range(1, DIAS_PROYECCION + 1)]
        
        # 4. Graficar
        plt.figure(figsize=(12, 7))
        
        # Datos Históricos
        plt.plot(df.index, df['Close'], label='Precio Real', color='black', alpha=0.6)
        plt.plot(df.index, prediccion_entrenamiento, color='blue', linestyle='--', alpha=0.3)
        
        # Proyección y Bandas
        plt.plot(fechas_futuras, linea_central, color='blue', label='Tendencia Central', linewidth=2)
        plt.fill_between(fechas_futuras, 
                         banda_inferior.flatten(), 
                         banda_superior.flatten(), 
                         color='blue', alpha=0.15, label='Zona de Probabilidad (95%)')
        
        plt.title(f"Canal de Regresión: {ticker_simbolo} ({PERIOD_DATA})")
        plt.xlabel("Fecha")
        plt.ylabel("Precio (USD)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

        print(f"[{ticker_simbolo}] Proyección a 90 días:")
        print(f"   Optimista (Techo): ${banda_superior[-1][0]:.2f}")
        print(f"   Esperado (Centro): ${linea_central[-1][0]:.2f}")
        print(f"   Pesimista (Suelo): ${banda_inferior[-1][0]:.2f}\n")

    except Exception as e:
        print(f"Error: {e}")

for t in TICKERS:
    proyectar_con_bandas(t)
