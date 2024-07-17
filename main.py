import streamlit as st
import pandas as pd
import joblib


# Load the trained model after converting the model to a
model = joblib.load('insurance_model.sav')



# Define the input features
regions = ['southeast', 'southwest', 'northeast', 'northwest']
smoker_options = ['yes', 'no']

# Function to make predictions
def predict_insurance(data):
    predictions = model.predict(data)
    return predictions

# Function to transform the data that was inputed
def transform_input_data(age, sex, bmi, children, smoker, region):
    sex = 0 if sex == 'Male' else 1
    smoker = 0 if smoker == 'yes' else 1
    region = regions.index(region)
    data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })
    return data

# Streamlit UI
st.title('Insurance Prediction Model')

st.sidebar.header('User Input Features')
##finding the maixmum and minimum values for each column
# max_age = insurance_data['age'].max() 
# min_age = insurance_data['age'].min()

# max_bmi = insurance_data['bmi'].max() 
# min_bmi = insurance_data['bmi'].min()


# Input fields in the sidebar
age = st.sidebar.number_input('Age', min_value=18, max_value=64, value=30)
sex = st.sidebar.selectbox('Sex', options=['Male', 'Female'])
bmi = st.sidebar.number_input('BMI', min_value=15.96, max_value=53.13, value=25.0, step=1.5)
children = st.sidebar.slider('Children', min_value=0, max_value=4, value=0)
smoker = st.sidebar.selectbox('Smoker', options=smoker_options, format_func=lambda x: 'Yes' if x == 'yes' else 'No')
region = st.sidebar.selectbox('Region', options=regions)

if st.sidebar.button('Predict'):
    input_data = transform_input_data(age, sex, bmi, children, smoker, region)
    predictions = predict_insurance(input_data)
    st.write("## Prediction Result")
    st.write(f"The predicted insurance price is: ${predictions[0]:.2f}")

st.write("""
## Instructions:
- Enter your details in the sidebar.
- Click 'Predict' to see your insurance price.
""")
