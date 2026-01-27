# 📈 Financial Price Projection with Confidence Bands

Este proyecto utiliza **Python** y **Machine Learning** (Regresión Lineal) para analizar datos históricos de acciones y proyectar tendencias futuras a 90 días, incluyendo bandas de probabilidad basadas en la desviación estándar.

## 🚀 Características
- Descarga de datos en tiempo real mediante `yfinance`.
- Cálculo de tendencia central mediante Regresión Lineal de Scikit-Learn.
- Visualización de **Bandas de Probabilidad (95%)** para medir el riesgo y la volatilidad.
- Comparativa visual entre datos históricos y proyecciones futuras.

## 🧠 Metodología y Análisis Técnico
Este proyecto implementa un enfoque cuantitativo para la estimación de precios basado en dos pilares estadísticos:

**1. Regresión Lineal Simple**
Se utiliza para identificar la tendencia subyacente. El modelo minimiza la suma de los cuadrados de las diferencias entre los precios de cierre reales y la línea proyectada:

$$y = \beta_0 + \beta_1x + \epsilon$$

Donde $\beta_1$ representa la pendiente (el momentum actual de la acción).

**2. Bandas de Error Estándar (Canal de Regresión)**
El modelo no solo proyecta una línea, sino que mide la volatilidad respecto a esa tendencia:
- Cálculo: Se obtiene la Desviación Estándar ($\sigma$) de los residuos.
- Intervalos de Confianza: Se aplican $\pm 2\sigma$ desde la línea central. Según la distribución normal, esto cubre aproximadamente el 95% de los movimientos de precio probables.

**3. Interpretación de Resultados**
- Banda Superior: Posible resistencia o zona de sobrecompra.
- Banda Inferior: Posible soporte o zona de sobreventa (oportunidad de entrada).
- Ancho del Canal: Refleja el riesgo histórico del activo. Un canal ancho indica alta volatilidad.

**🚨Disclaimer:** Este proyecto es exclusivamente con fines educativos y de portafolio. No constituye asesoría financiera.

---

## 🗞️ Módulo 2: Terminal de Noticias en Tiempo Real (Dashboard)

Además del análisis técnico, el repositorio incluye una **Terminal de Noticias** interactiva construida con **Streamlit** y conectada a la API profesional de **Finnhub**.

### 🚀 Características del Dashboard
- **Interfaz Profesional**: Diseño basado en tarjetas (Cards) con visualización de fuentes y miniaturas.
- **Conexión API**: Consumo de datos en tiempo real evitando bloqueos de scraping.
- **Multiticker**: Capacidad de monitorear múltiples activos (Acciones, Crypto) simultáneamente desde la barra lateral.
- **Filtrado de Sentimiento**: Acceso directo a resúmenes y fuentes oficiales (Yahoo Finance, Bloomberg, etc.).

### 🛠️ Cómo ejecutar el Dashboard
1. Navega a la carpeta: `cd terminal_noticias`
2. Ejecuta Streamlit: `streamlit run app_noticias.py`

## 🛠️ Tecnologías Utilizadas
- **Lenguaje**: Python 3.x
- **Análisis de Datos**: Pandas, Numpy.
- **Machine Learning**: Scikit-Learn (Linear Regression).
- **Visualización**: Matplotlib, Streamlit.
- **Fuentes de Datos**: YFinance API, Finnhub API.
