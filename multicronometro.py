import streamlit as st
import time

# Config
st.set_page_config(page_title="Multi Cronómetro", page_icon="⏱️")
st.title("⏱️ Multi Cronómetro")

nombres = ["Rivet", "Washer press", "Inspección final", "Pull inspection", "Screw fastening"]

# Inicialización
if "tiempos" not in st.session_state:
    st.session_state.tiempos = {n: 0.0 for n in nombres}
    st.session_state.en_marcha = {n: False for n in nombres}
    st.session_state.inicio = {n: 0.0 for n in nombres}

# Actualizar tiempos
hay_activos = False
for nombre in nombres:
    if st.session_state.en_marcha[nombre]:
        st.session_state.tiempos[nombre] = time.time() - st.session_state.inicio[nombre]
        hay_activos = True

# Mostrar cronómetros
for nombre in nombres:
    st.markdown(f"### 🧩 {nombre}")

    minutos = int(st.session_state.tiempos[nombre] // 60)
    segundos = int(st.session_state.tiempos[nombre] % 60)
    decimas = int((st.session_state.tiempos[nombre] * 10) % 10)
    st.markdown(f"## ⏱️ {minutos:02}:{segundos:02}.{decimas}")

    col1, col2, col3 = st.columns(3)

    if col1.button("▶️ Iniciar", key=f"iniciar_{nombre}"):
        if not st.session_state.en_marcha[nombre]:
            st.session_state.en_marcha[nombre] = True
            st.session_state.inicio[nombre] = time.time() - st.session_state.tiempos[nombre]
            st.experimental_rerun()

    if col2.button("⏸️ Detener", key=f"detener_{nombre}"):
        st.session_state.en_marcha[nombre] = False
        st.experimental_rerun()

    if col3.button("🔁 Reiniciar", key=f"reiniciar_{nombre}"):
        st.session_state.en_marcha[nombre] = False
        st.session_state.tiempos[nombre] = 0.0
        st.experimental_rerun()

    st.divider()

# Controles globales
st.markdown("## ⚙️ Controles globales")
colA, colB, colC = st.columns(3)

if colA.button("▶️ Iniciar todos"):
    for n in nombres:
        st.session_state.en_marcha[n] = True
        st.session_state.inicio[n] = time.time() - st.session_state.tiempos[n]
    st.experimental_rerun()

if colB.button("⏸️ Detener todos"):
    for n in nombres:
        st.session_state.en_marcha[n] = False
    st.experimental_rerun()

if colC.button("🔁 Reiniciar todos"):
    for n in nombres:
        st.session_state.en_marcha[n] = False
        st.session_state.tiempos[n] = 0.0
    st.experimental_rerun()

# 🔄 Refresco automático si hay cronómetros corriendo
if hay_activos:
    time.sleep(0.1)
    st.experimental_rerun()
