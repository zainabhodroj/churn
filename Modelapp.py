# Required Packages
import streamlit as st
import pandas as pd
import pickle
from style import webapp_style
from input import user_input_features
from PIL import Image

# Web Page configuration
st.set_page_config(
    page_title="Customer Churn Predection App",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #faebd7;">
  <a class="Dataset" href="https://www.kaggle.com/datasets/blastchar/telco-customer-churn" target="_blank">Dataset</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
        <li class="nav-item">
        <a class="nav-link" href="https://share.streamlit.io/zainabhodroj/sthome/main/home.py" target="_blank">Overview</a>
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
""", unsafe_allow_html=True


# Title for the app
col1,col2 = st.columns([1, 5, 25])
with col1:
    st.write("Model")
with col2:
    st.title("""
                Customer Churn Prediction App
                This app predicts if the customer will churn or not.\n
                Data obtained from the Kaggle - [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
                """)

# Sidebar
st.sidebar.header('Upload Data')
st.sidebar.markdown('[Example CSV Input file](https://www.kaggle.com/blastchar/telco-customer-churn)')

# Collect user input features into dataframe
# Upload the CSV file
uploaded_file = st.sidebar.file_uploader('Upload your input CSV file', type=['csv'])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    # Enter manually
    st.sidebar.write('Enter the data manually')
    input_df = user_input_features()

# Combining the user input features with entire churn dataset
# This will be useful for the encoding phase
raw_churn_data = pd.read_csv('Churn.csv')
raw_churn_data = raw_churn_data.drop(columns=['customerID', 'Churn'])
df = pd.concat([input_df, raw_churn_data], axis=0)

# Encoding of the categorical features
encode = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
          'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
          'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
          'PaperlessBilling', 'PaymentMethod']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col, drop_first=True)
    df = pd.concat([df, dummy], axis=1)
    del df[col]
# Select only the first row (the user input data)
df = df[: 1]
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])

# Displays the user input features
st.subheader('User Input features')
if uploaded_file:
    st.write(input_df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using below example.')
    st.write(input_df.iloc[:, :7])
    st.write(input_df.iloc[:, 7: 15])
    st.write(input_df.iloc[:, 15:])

# Load the saved model
load_clf = pickle.load(open('modelForPrediction.sav', 'rb'))

# Apply model on the prediction
st.subheader('Prediction')
st.write('Hit "Predict" button to run the app!')
predict = st.button('Predict')
if predict:
    # predictions
    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)

    # output results
    if prediction == 1:
        st.write('This customer is likely to be churned.')
        st.write(f'Confidence: {prediction_proba[:, 1] * 100}')
    else:
        st.write('This customer is likely to continue with the service.')
        st.write(f'Confidence: {prediction_proba[:, 0] * 100}')

# WebApp Style Settings
webapp_style()

