import streamlit as st
import time

# Título de la app
st.set_page_config(page_title="Multi Cronómetro", page_icon="⏱️")
st.title("⏱️ Multi Cronómetro")

# Nombres de los cronómetros
nombres = ["Rivet", "Washer press", "Inspección final", "Pull inspection", "Screw fastening"]

# Inicializar estados si no existen
if "tiempos" not in st.session_state:
    st.session_state.tiempos = {n: 0.0 for n in nombres}
    st.session_state.en_marcha = {n: False for n in nombres}
    st.session_state.inicio = {n: 0.0 for n in nombres}

# Actualizar tiempos en marcha
for nombre in nombres:
    if st.session_state.en_marcha[nombre]:
        st.session_state.tiempos[nombre] = time.time() - st.session_state.inicio[nombre]

# Layout de los cronómetros
for nombre in nombres:
    st.markdown(f"### 🧩 {nombre}")

    # Mostrar tiempo actual
    minutos = int(st.session_state.tiempos[nombre] // 60)
    segundos = int(st.session_state.tiempos[nombre] % 60)
    decimas = int((st.session_state.tiempos[nombre] * 10) % 10)
    st.markdown(f"## ⏱️ {minutos:02}:{segundos:02}.{decimas}")

    col1, col2, col3 = st.columns(3)

    # Botones individuales
    if col1.button("▶️ Iniciar", key=f"iniciar_{nombre}"):
        if not st.session_state.en_marcha[nombre]:
            st.session_state.en_marcha[nombre] = True
            st.session_state.inicio[nombre] = time.time() - st.session_state.tiempos[nombre]
            st.rerun()

    if col2.button("⏸️ Detener", key=f"detener_{nombre}"):
        if st.session_state.en_marcha[nombre]:
            st.session_state.en_marcha[nombre] = False
            st.session_state.tiempos[nombre] = time.time() - st.session_state.inicio[nombre]
            st.rerun()

    if col3.button("🔁 Reiniciar", key=f"reiniciar_{nombre}"):
        st.session_state.en_marcha[nombre] = False
        st.session_state.tiempos[nombre] = 0.0
        st.rerun()

    st.markdown("---")

# Botones globales
st.markdown("## ⚙️ Controles globales")
colA, colB, colC = st.columns(3)

if colA.button("▶️ Iniciar todos"):
    for n in nombres:
        st.session_state.en_marcha[n] = True
        st.session_state.inicio[n] = time.time() - st.session_state.tiempos[n]
    st.rerun()

if colB.button("⏸️ Detener todos"):
    for n in nombres:
        if st.session_state.en_marcha[n]:
            st.session_state.en_marcha[n] = False
            st.session_state.tiempos[n] = time.time() - st.session_state.inicio[n]
    st.rerun()

if colC.button("🔁 Reiniciar todos"):
    for n in nombres:
        st.session_state.en_marcha[n] = False
        st.session_state.tiempos[n] = 0.0
    st.rerun()
