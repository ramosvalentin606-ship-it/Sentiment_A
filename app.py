from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator
from streamlit_lottie import st_lottie
import requests

st.title('Análisis de Sentimiento')

image = Image.open('MIUW.jpeg')
st.image(image)

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

# Función para cargar animaciones
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animaciones
lottie_positive = load_lottie("https://assets2.lottiefiles.com/packages/lf20_jbrw3hcz.json")
lottie_negative = load_lottie("https://assets2.lottiefiles.com/packages/lf20_t9gkkhz4.json")
lottie_neutral = load_lottie("https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write("""
    Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

    Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')

    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text

        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity,2)
        subjectivity = round(blob.sentiment.subjectivity,2)

        st.write('Polarity: ', polarity)
        st.write('Subjectivity: ', subjectivity)

        if polarity > 0:
            st.success('Es un sentimiento Positivo 😊')
            st_lottie(lottie_positive, height=200)

        elif polarity < 0:
            st.error('Es un sentimiento Negativo 😔')
            st_lottie(lottie_negative, height=200)

        else:
            st.info('Es un sentimiento Neutral 😐')
            st_lottie(lottie_neutral, height=200)
