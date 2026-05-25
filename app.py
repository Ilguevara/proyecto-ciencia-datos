import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(
    page_title='Minas Antipersonal Colombia',
    page_icon='💣',
    layout='wide'
)

# Configuración de estilo
sns.set_theme(style='whitegrid', palette='muted')

# ============================================================
# CARGA DEL MODELO (debes guardarlo primero desde tu notebook)
# ============================================================
@st.cache_resource
def cargar_modelo():
    with open('modelo_rf_minas.pkl', 'rb') as f:
        return pickle.load(f)

# También necesitas cargar el scaler si usaste StandardScaler
@st.cache_resource
def cargar_scaler():
    try:
        with open('scaler.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        return None

# Título
st.title('💣 Predicción de Víctimas por Minas Antipersonal')
st.write('Ingrese los datos del incidente para predecir si la víctima resultará **HERIDA** o **MUERTA**.')
st.divider()

st.subheader('📋 Datos del incidente')

# Organización en columnas (igual que el ejemplo)
col1, col2 = st.columns(2)

with col1:
    # Variables geográficas y temporales
    departamento = st.selectbox('Departamento', 
        ['Antioquia', 'Nariño', 'Meta', 'Caquetá', 'Norte de Santander', 
         'Putumayo', 'Tolima', 'Cauca', 'Bolívar', 'Arauca'])
    ano = st.slider('Año del evento', 1990, 2024, 2015)
    mes = st.selectbox('Mes', list(range(1,13)), 
                       format_func=lambda x: ['Ene','Feb','Mar','Abr','May','Jun',
                                               'Jul','Ago','Sep','Oct','Nov','Dic'][x-1])
    
    # Variables de la víctima
    condicion = st.selectbox('Condición de la víctima', ['Fuerza pública', 'Civil'])
    tipoarea = st.selectbox('Tipo de área', ['Rural', 'Urbana'])
    rangoedad = st.selectbox('Rango de edad', ['Mayor de 18 años', 'Menor de 18 años'])

with col2:
    grupoetnico = st.selectbox('Grupo étnico', 
        ['Ninguno', 'Indígena', 'Afrodescendiente', 'Gitano/Rrom', 'Raizal', 'Palenquero'])
    estado = st.selectbox('Sexo', ['Hombre', 'Mujer'])
    tipoevento = st.selectbox('Tipo de evento', 
        ['Evento MAP', 'Evento MUSE', 'Accidente por manipulación', 'Otro'])
    actividad = st.selectbox('Actividad al momento', 
        ['Patrullaje militar', 'Pasando o cerca', 'Agricultura', 'Tránsito', 
         'Recolección', 'Cuidado de animales', 'Juego', 'Trabajo de casa', 'Otro'])

st.divider()

# Botón de predicción
if st.button('🔍 Predecir resultado', use_container_width=True, type='primary'):
    
    # Mostrar un spinner mientras "piensa"
    with st.spinner('Analizando datos...'):
        # Aquí iría la predicción real con tu modelo
        # Como ejemplo, simulamos una predicción basada en reglas simples
        
        # SIMULACIÓN (reemplazar con tu modelo real)
        # Cálculo de probabilidad simulada
        prob_muerte = 0.20  # Base
        
        # Reglas simples (solo para demostración)
        if condicion == 'Civil':
            prob_muerte += 0.05
        if tipoarea == 'Rural':
            prob_muerte += 0.03
        if rangoedad == 'Menor de 18 años':
            prob_muerte += 0.07
        if actividad == 'Juego':
            prob_muerte += 0.10
        if departamento in ['Putumayo', 'Tolima']:
            prob_muerte += 0.08
            
        # Limitar entre 0 y 1
        prob_muerte = min(max(prob_muerte, 0.05), 0.60)
        prob_herido = 1 - prob_muerte
        
        # Predicción
        prediccion = 1 if prob_muerte > 0.3 else 0
    
    # Mostrar resultados (igual que el ejemplo)
    st.subheader('📊 Resultado de la Predicción')
    
    col_res, col_prob = st.columns(2)
    
    with col_res:
        if prediccion == 1:
            st.error('⚠️ **Predicción: VÍCTIMA MORTAL**')
            st.caption('El modelo sugiere alta probabilidad de desenlace fatal')
        else:
            st.success('✅ **Predicción: HERIDO**')
            st.caption('El modelo sugiere supervivencia con lesiones')
    
    with col_prob:
        st.metric('Probabilidad de fallecer', f'{prob_muerte:.1%}')
        st.metric('Probabilidad de sobrevivir', f'{prob_herido:.1%}')
    
    # Gráfico de probabilidades (igual que el ejemplo)
    st.divider()
    st.subheader('📈 Distribución de Probabilidades')
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.barh(['Sobrevive (Herido)', 'Fallece (Muerto)'], 
            [prob_herido, prob_muerte],
            color=['#1D9E75', '#E24B4A'], height=0.5)
    for i, v in enumerate([prob_herido, prob_muerte]):
        ax.text(v+0.01, i, f'{v:.1%}', va='center', fontsize=12)
    ax.set_xlim(0, 1.1)
    ax.set_xlabel('Probabilidad')
    ax.set_title('Resultado predicho por el modelo')
    st.pyplot(fig)
    
    # Factores de riesgo destacados
    st.divider()
    st.subheader('⚠️ Factores de riesgo identificados')
    
    riesgos = []
    if rangoedad == 'Menor de 18 años':
        riesgos.append("• **Menor de edad** - Mayor vulnerabilidad a lesiones fatales")
    if condicion == 'Civil':
        riesgos.append("• **Civil** - Sin equipo de protección, mayor riesgo de fatalidad")
    if actividad in ['Juego', 'Recolección', 'Cuidado de animales']:
        riesgos.append(f"• **Actividad: {actividad}** - Alta exposición en zona rural")
    if tipoarea == 'Rural':
        riesgos.append("• **Zona rural** - Dificultad de acceso a atención médica oportuna")
    
    if riesgos:
        for riesgo in riesgos:
            st.warning(riesgo)
    else:
        st.info("No se identificaron factores de riesgo adicionales significativos")

# Pie de página
st.divider()
st.caption('''
**Proyecto de Ciencia de Datos** — Análisis de Víctimas por Minas Antipersonal en Colombia  
Ivy Lineth Guevara Delgado · Karen Valeria Castañeda Fuentes
''')