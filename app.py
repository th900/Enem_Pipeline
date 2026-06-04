import streamlit as st
import pickle
import os

model_path = 'modelo_rf.pkl'
with open(model_path, 'rb') as f:
    modelo = pickle.load(f)

st.title('Previsao de Nota de Redacao - ENEM 2023')
