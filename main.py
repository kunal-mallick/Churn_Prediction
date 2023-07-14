import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline

#st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.slider('Voice Message', 0, 52)
    
    intl = st.columns(2)
    intl_calls = intl[0].slider("Int Call's", 0, 20)
    intl_min = intl[1].number_input("Int Min", 0.0, 20.0)

    day = st.columns(2)
    day_charges = day[0].number_input("Day Chaarge's", 0.0, 59.76)
    day_min = day[1].number_input("Day Min", 0.0, 351.5)

    st.slider("Customer's Call", 0, 9)

    check = st.columns(2)
    voice_plan = check[0].checkbox("Voice Plan", value=False)
    intl_plan = check[1].checkbox("Int Plan", value=False)

    st.button('predect', on_click=None)

    st.text('the person is less likly to chrun')

if __name__ == '__main__':

    main()    