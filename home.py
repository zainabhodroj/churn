import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #faebd7;">
  <a class="Dataset" href="https://www.kaggle.com/datasets/blastchar/telco-customer-churn" target="_blank">Dataset</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only"></span></a>
      </li>
        <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/zainabhodroj/churn/main/home.py" target="_blank">Overview</a>
      </li>
      <li class="nav-item"> 
        <a class="nav-link" href="https://share.streamlit.io/zainabhodroj/datavis/main/Datavis.py" target="_blank">DataVisulization</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/zainabhodroj/churn/main/Modelapp.py" target="_blank">Model Prediction</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

image1= Image.open('1.png')
image2= Image.open('2.png')
st.set_option('deprecation.showPyplotGlobalUse', False)


st.image(image1, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')


st.title('Streamlit Project')
st.header('In this small project, I would like to explore a very underrated subject in the world of business: Customer Churn.')
st.write('In this app, You will be able to accurately predict if a customer is likely to churn.')


st.sidebar.header('What is Customer Churn?')
st.sidebar.markdown('Customer churn is the percentage of customers that stopped using your companys product or service during a certain time frame. You can calculate churn rate by dividing the number of customers you lost during that time period -- say a quarter -- by the number of customers you had at the beginning of that time period.')
st.sidebar.header('What can be a Good Customer Churn Rate?')
st.sidebar.markdown('There is no easy way of identifying a perfect customer churn rate, especially since it highly depends on the type of industry you are working in. Some sectors have significantly higher rates of customer attrition than others.')

st.image(image2, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

df= pd.read_csv('Churn.csv')

st.title('Predicting Customer Churn')
st.header('With this dashboard you will be able to explore a very crucial subject in the world of business: Customer Churn.')
st.write('You will be able to have hands on experience with a model that can accurately predict if a customer is likely to churn.')

st.header("Take a Look at the dataset :)")
if st.checkbox('Show Dataset'):
    number = st.number_input('Number of Rows to View',5,100)
    st.dataframe(df.head(number))

df= pd.read_csv('Churn.csv')
 
if st.checkbox('shape of Dataset'):
    data_dim = st.radio ('Show Dimension By',('Rows', 'Columns'))
    if data_dim == 'Row':
        st.text('Number of Rows')
        st.write(df.shape[0])
    if data_dim == 'Columns':
        st.text('Number of Columns')
        st.write(df.shape[1])
    else:
        st.write(df.shape)

if st.checkbox('Select Columns to Show'):
    all_columns= df.columns.tolist()
    selected_columns = st.multiselect('Select', all_columns)
    new_df= df[selected_columns]
    st.dataframe(new_df)

from style import webapp_style
webapp_style()

