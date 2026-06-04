import streamlit as st
import pickle
import numpy as np
import os

model_path = os.path.expanduser('~/enem-pipeline/src/modelo_rf.pkl')
with open(model_path, 'rb') as f:
    modelo = pickle.load(f)

st.title('Previsao de Nota de Redacao - ENEM 2023')
st.markdown('Insira as notas das provas objetivas para prever a nota de redacao.')

col1, col2 = st.columns(2)
with col1:
    nota_cn = st.slider('Ciencias da Natureza', 0, 1000, 500)
    nota_ch = st.slider('Ciencias Humanas', 0, 1000, 500)
with col2:
    nota_lc = st.slider('Linguagens', 0, 1000, 500)
    nota_mt = st.slider('Matematica', 0, 1000, 500)

tp_escola = st.selectbox('Tipo de escola', [2, 3], format_func=lambda x: 'Publica' if x == 2 else 'Privada')
media_objetivas = (nota_cn + nota_ch + nota_lc + nota_mt) / 4
features = np.array([[nota_cn, nota_ch, nota_lc, nota_mt, media_objetivas, tp_escola, 5]])

if st.button('Prever nota de redacao'):
    pred = modelo.predict(features)[0]
    pred = max(0, min(1000, pred))
    st.metric('Nota prevista de redacao', f'{pred:.0f}')
    st.info(f'Media das provas objetivas: {media_objetivas:.1f}')