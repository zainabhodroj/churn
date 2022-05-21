import streamlit as st
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_diabetes, load_boston
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objs as go
import streamlit.components.v1 as components



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

