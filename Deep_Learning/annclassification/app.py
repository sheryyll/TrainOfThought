import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')
import os

# load the trained model
BASE_DIR = os.path.dirname(__file__)

@st.cache_resource
def load_model_and_tools():
    model = tf.keras.models.load_model(
    os.path.join(BASE_DIR, 'model.keras')
    )

    with open(os.path.join(BASE_DIR, 'onehot_encoder_geo.pkl'), 'rb') as file:
        onehot_encoder_geo = pickle.load(file)

    with open(os.path.join(BASE_DIR, 'label_encoder_gender.pkl'), 'rb') as file:
        label_encoder_gender = pickle.load(file)

    with open(os.path.join(BASE_DIR, 'scaler.pkl'), 'rb') as file:
        scaler = pickle.load(file)

    return model, onehot_encoder_geo, label_encoder_gender, scaler

model, onehot_encoder_geo, label_encoder_gender, scaler = load_model_and_tools()

# streamlit file
st.title('Customer Churn Prediction')

# user input
geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0,1])
is_active_member = st.selectbox('Is Active Memeber', [0,1])

# prepare input data as DataFrame
input_df = pd.DataFrame({
    'CreditScore' : [credit_score],
    'Gender' : [label_encoder_gender.transform([gender])[0]],
    'Age' : [age],
    'Tenure' : [tenure],
    'Balance' : [balance],
    'NumOfProducts' : [num_of_products],
    'HasCrCard' : [has_cr_card],
    'IsActiveMember' : [is_active_member],
    'EstimatedSalary' : [estimated_salary]
})

# ohe on 'Geography'
geo_encoded = onehot_encoder_geo.transform(pd.DataFrame({'Geography': [geography]}))

geo_encoded_df = pd.DataFrame(
    geo_encoded,
    columns=onehot_encoder_geo.get_feature_names_out(['Geography'])
)

# Combine
input_df = pd.concat([input_df, geo_encoded_df], axis=1)

# scale
input_data_scaled = scaler.transform(input_df)

# Predict churn
prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

st.write(f'Churn Probability : {prediction_proba:.2f}')

if prediction_proba > 0.5:
    st.write('The customer is likely to churn')
else:
    st.write('The customer is not likely to churn.')