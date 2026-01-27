# 🏛️ Finance-Analytics-Dashboard

Este proyecto es una herramienta práctica para el análisis de mercados que une dos mundos: la estadística matemática y el flujo de noticias real. Su objetivo es evitar que tomes decisiones basadas solo en una gráfica, dándote contexto sobre qué está pasando en el mundo mientras analizas la tendencia del precio.

### 🎯 ¿Para qué sirve?
* **Análisis Técnico**: Calcula automáticamente hacia dónde se dirige el precio y define zonas de riesgo (soporte/resistencia) usando modelos matemáticos.
* **Contexto Fundamental**: Filtra y organiza las noticias más importantes de tus activos para que no tengas que buscarlas manualmente en diferentes portales.
* **Decisiones Informadas**: Al tener la proyección y la noticia en un mismo lugar, puedes validar si un movimiento de mercado tiene un sustento real o es puro ruido.

---

## 📈 Módulo 1: Proyección de Precios con Bandas de Confianza

Este módulo implementa un enfoque cuantitativo para la estimación de precios basado en dos pilares estadísticos fundamentales.

### 🧠 Metodología y Análisis Técnico

#### 1. Regresión Lineal Simple
Se utiliza para identificar la tendencia subyacente del activo. El modelo minimiza la suma de los cuadrados de las diferencias entre los precios de cierre reales y la línea proyectada:

$$y = \beta_0 + \beta_1x + \epsilon$$

Donde $\beta_1$ representa la pendiente, es decir, el **momentum** actual de la acción.

#### 2. Bandas de Error Estándar (Canal de Regresión)
El modelo no solo proyecta una línea, sino que mide la **volatilidad** respecto a esa tendencia para gestionar el riesgo:

* **Cálculo**: Se obtiene la Desviación Estándar ($\sigma$) de los residuos (la distancia entre el precio real y la línea de regresión).
* **Intervalos de Confianza**: Se aplican **$\pm2\sigma$** desde la línea central. Según la distribución normal, esto cubre aproximadamente el **95% de los movimientos de precio probables**, permitiendo identificar zonas de agotamiento.

#### 3. Interpretación de Resultados
* **Banda Superior**: Posible zona de sobrecompra o resistencia técnica.
* **Banda Inferior**: Posible zona de sobreventa o soporte (oportunidad de entrada).
* **Ancho del Canal**: Refleja el riesgo histórico; un canal ancho indica alta volatilidad.

---

## 🗞️ Módulo 2: Terminal de Noticias en Tiempo Real (Dashboard)

Dashboard interactivo construido con **Streamlit** y conectado a la API profesional de **Finnhub** para el análisis fundamental.

### 🚀 Características
* **Interfaz Profesional**: Diseño basado en tarjetas (Cards) con visualización de fuentes y miniaturas.
* **Conexión API**: Consumo de datos en tiempo real evitando bloqueos de scraping.
* **Multiticker**: Monitoreo simultáneo de múltiples activos (Acciones, Crypto).
* **Análisis Rápido**: Acceso directo a resúmenes y fuentes oficiales.

---

## 🛠️ Instalación y Uso

1.  **Clonar el repositorio**:
    ```bash
    git clone [https://github.com/ZDRAVKO-YURAS/Finance-Analytics-Dashboard.git](https://github.com/ZDRAVKO-YURAS/Finance-Analytics-Dashboard.git)
    ```
2.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Ejecutar Dashboard de Noticias**:
    ```bash
    streamlit run terminal_noticias/noticias_dashboard_2.py
    ```

---
> **Disclaimer**: Este proyecto es exclusivamente con fines educativos. No constituye asesoría financiera.
