import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Informe: Soluciones de Almacenamiento de Datos")

st.markdown("""
Este informe compara cuatro tecnologías de almacenamiento:
**HDD, SSD, Cinta y Nube**.

Se incluyen:  
- Tabla comparativa de métricas clave  
- Gráficos de rendimiento y costos  
- Simulación de crecimiento de datos y tiempos de respuesta
""")

# ========================
# Tabla de comparación
# ========================
st.header("1️⃣ Comparación de Tecnologías")

data = {
    "Tecnología": ["HDD", "SSD", "Cinta", "Nube"],
    "Velocidad Lectura (MB/s)": [150, 3000, 300, 300],
    "Velocidad Escritura (MB/s)": [120, 2800, 150, 200],
    "Capacidad (TB)": [20, 16, 30, 1000],
    "Costo por GB (USD)": [0.025, 0.1, 0.01, 0.05],
    "Fiabilidad (MTBF horas)": [1_200_000, 2_000_000, 2_000_000, 1_500_000],
    "Consumo (W)": [8, 4, 7, 0],
    "Seguridad (1–5)": [3, 4, 2, 5],
    "Escalabilidad (1–5)": [3, 3, 2, 5],
}
df = pd.DataFrame(data)
st.dataframe(df)

# ========================
# Gráfico de velocidades
# ========================
st.header("2️⃣ Gráfico de Velocidades")

fig, ax = plt.subplots()
ax.bar(df["Tecnología"], df["Velocidad Lectura (MB/s)"], label="Lectura")
ax.bar(df["Tecnología"], df["Velocidad Escritura (MB/s)"], alpha=0.5, label="Escritura")
ax.set_ylabel("MB/s")
ax.set_title("Comparación de Velocidades de Lectura/Escritura")
ax.legend()
st.pyplot(fig)

# ========================
# Gráfico de costo por GB
# ========================
st.header("3️⃣ Gráfico de Costo por GB")

fig2, ax2 = plt.subplots()
ax2.bar(df["Tecnología"], df["Costo por GB (USD)"])
ax2.set_ylabel("USD por GB")
ax2.set_title("Comparación de Costos por GB")
st.pyplot(fig2)

# ========================
# Simulación de crecimiento
# ========================
st.header("4️⃣ Simulación de Crecimiento y Rendimiento")

vol_inicial = st.number_input("Volumen inicial (TB)", min_value=10, max_value=1000, value=100)
crecimiento = st.slider("Crecimiento anual (%)", 5, 50, 20)
horizonte = st.slider("Horizonte (años)", 1, 10, 5)

resultados = []
for año in range(1, horizonte + 1):
    volumen = vol_inicial * ((1 + crecimiento / 100) ** (año - 1))
    tiempo_hdd = volumen * 1024 / 150 / 60  # en minutos
    tiempo_ssd = volumen * 1024 / 3000 / 60
    tiempo_cinta = volumen * 1024 / 300 / 60
    tiempo_nube = volumen * 1024 / 300 / 60  # sup. similar a cinta
    resultados.append([año, round(volumen, 1),
                       round(tiempo_hdd, 1),
                       round(tiempo_ssd, 1),
                       round(tiempo_cinta, 1),
                       round(tiempo_nube, 1)])

simulacion = pd.DataFrame(resultados, columns=["Año", "Volumen (TB)", "Tiempo HDD (min)",
                                               "Tiempo SSD (min)", "Tiempo Cinta (min)", "Tiempo Nube (min)"])
st.dataframe(simulacion)

st.markdown("""
📌 **Interpretación:**  
- **SSD** mantiene bajos tiempos de respuesta incluso con crecimiento.  
- **HDD** se degrada pero es aceptable para analítica y batch.  
- **Cinta y Nube** son útiles para archivo y respaldo, no para acceso frecuente.
""")
