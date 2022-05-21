import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
showWarningOnDirectExecution = False
st.set_option('deprecation.showPyplotGlobalUse', False)

st.header("Telco Customer Churn Prediction :bar_chart:")

df = pd.read_csv("Churn.csv")
st.write(df.head(10))
st.write("Data points in Churn is",len(df['Churn']))
       
col1, col2, col3 = st.columns(3)
with col1:
        df['Churn'].value_counts().plot(kind = 'bar', title = 'Bar Graph of Non-Churners vs Churners by Count (Churn is a 1)', color = 'blue', align = 'center') 
        st.pyplot(plt.show())
     
with col2:
        # Explore the relationship between instances of Tech Support and Churn. 
        # Stacked Bar of Tech Support and Churn.
        tech_support_churn = pd.crosstab(df['TechSupport'], df['Churn'])
        tech_support_churn.plot(kind = 'bar', stacked = True)
        plt.ylabel('Count')
        plt.xlabel('Tech Support Count')
        plt.title('Churn Rate Relative to Uses of Tech Support (Churned is a 1)')
        fig= plt.show()
        st.pyplot(fig)
with col3:
        # Plot the distribution of observations for tenure.
        sns.distplot(df['tenure']);
        st.pyplot(plt.show())
 

st.sidebar.title("Telco Customer Churn Exploratory Data Analysis")       
st.sidebar.subheader("Filter by Gender")
gender = ["Female", "Male", "ALL"]
    
gender_selections = st.sidebar.radio(
        "Select Gender to filter", gender)


st.sidebar.subheader("Filter by Payment Method")
payment_method = list(df.PaymentMethod.unique())
    
payment_selections = st.sidebar.selectbox(
        "Select Payment Method", payment_method)


st.sidebar.subheader("Choose Customer ID to see more details")
customerIDs = list(df.customerID.unique())
    
customer_selections = st.sidebar.selectbox(
        "Select Customer ID to filter by", customerIDs)


st.header("INSIGHTS")
st.write("Relationship between Gender and Churn")
gender_churn_contingency = pd.crosstab(df["gender"], df["Churn"])
st.write(gender_churn_contingency)    

fig, axes = plt.subplots(1, 2, sharey=True, figsize=(30, 10)) 
sns.countplot(x='PaperlessBilling', hue='Churn', data=df, ax=axes[0]);
sns.countplot(x='PaymentMethod', hue='Churn',data=df, ax=axes[1]);
st.pyplot(fig)




        # See if the other products they have from this company has to do with their churn.
fig2, axes = plt.subplots(1, 2, sharey=True, figsize=(30, 10)) 
sns.countplot(x='PhoneService', hue='Churn',data=df, ax=axes[0]);
st.write("We can see that customers that use paperless billing are much more likely to churn. That seems backwards I would go check that data with the team. We can see that customers that have the 0 payment method (electronic check) are much more likely to churn.If they don't have Phone Service,Internet Service, they are more likely to churn.")

sns.countplot(x='InternetService', hue='Churn',data=df, ax=axes[1]);
st.pyplot(fig2)
st.write("Customers with the highest Internet Service are least likely to churn.Customers with other products from the company, and premium products, churn less.")

    
