import pickle
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
import warnings
warnings.filterwarnings("ignore")

model = pickle.load(open('deploy.pkl','rb'))

df = pd.read_excel("emisico2indo.xlsx")
st.set_page_config(layout='centered')

st.title('Prediksi Kualitas Udara')
year = st.slider("Pilih Prediksi Beberapa Tahun Kedepan",1,30,step = 1)

pred = np.shape(year)
pred = pd.DataFrame(df, columns=['CO2 emission per kapita'])

if st.button("Predict") :
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)