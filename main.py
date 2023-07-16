import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline

#st.set_page_config(layout="wide")
ch = pd.read_csv('https://raw.githubusercontent.com/kunal-mallick/Churn_Prediction/main/Data%20Preprocessing%20%26%20EDA/eda.csv')
x = ch.iloc[:,[1,2,3,5,7,8,14,70,71,72,73]]

load = open('model.pkl','rb')
model = pickle.load(load)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Adding Column Funtion
def col_pc_n(n):

    col = []
    p = 'pc'

    for i in range(0,n):
        col_n = p + str(i)
        col.append(col_n)

    return col

# Adding Standard Scaler Funtion
def stand(x, a):

    x.loc[len(x.index)] = a
    sc = StandardScaler()
    scaled_x  = pd.DataFrame(sc.fit_transform(x), 
                        columns=['voice_message', 'intl_min', 'intl_calls', 'day_min', 'day_charges', 'eve_min', 'customer_call', 'voice_plan_no', 'voice_plan_yes', 'intl_plan_no', 'intl_plan_yes'])

    return scaled_x

# Adding PCA Funtion
def pca(sd):
    pcax = PCA(n_components = 8)
    pcsy = pcax.fit_transform(sd)

    ch_scaled_pca = pd.DataFrame(pcsy, columns=col_pc_n(8))
    
    last = len(ch_scaled_pca) -1
    return ch_scaled_pca.iloc[last:]

# Adding Prediction Funtion
def pred(voice_message, intl_min, intl_calls, day_min, day_charges, eve_min, customer_call, voice_plan_no, voice_plan_yes, intl_plan_no, intl_plan_yes):

    a = [voice_message, intl_min, intl_calls, day_min, day_charges, eve_min, customer_call, voice_plan_no, voice_plan_yes, intl_plan_no, intl_plan_yes]
    y = stand(x,a)
    z = pca(y)
    prediction = model.predict_proba(z)
    
    return round(prediction[0][0] * 100, 2)

# Adding Main Funtion
def main(): 
    voice_message =st.slider('Voice Message', 0, 52)
    
    intl = st.columns(2)
    intl_calls = intl[0].slider("Int Call's", 0, 20)
    intl_min = intl[1].number_input("Int Min", 0.0, 20.0)

    day = st.columns(2)
    day_charges = day[0].number_input("Day Chaarge's", 0.0, 59.76)
    day_min = day[1].number_input("Day Min", 0.0, 351.5)

    es = st.columns(2)
    customer_call = es[0].slider("Customer's Call", 0, 9)
    eve_min = es[1].number_input("Eve Min", 0.0, 363.7)

    check = st.columns(2)
    voice_plan = check[0].checkbox("Voice Plan", value=False)
    if voice_plan == False:
        voice_plan_no = 1
        voice_plan_yes = 0
    else:
        voice_plan_no = 0
        voice_plan_yes = 1
    intl_plan = check[1].checkbox("Int Plan", value=False)
    if intl_plan == False:
        intl_plan_no = 1
        intl_plan_yes = 0
    else:
        intl_plan_no = 0
        intl_plan_yes = 1

    if st.button('Predict'):

        result = pred(voice_message, intl_min, intl_calls, day_min, day_charges, eve_min, customer_call, voice_plan_no, voice_plan_yes, intl_plan_no, intl_plan_yes)
        st.text(str(result)+ " % chance of staying")

# Runing Main Funtion
if __name__ == '__main__':

    main()