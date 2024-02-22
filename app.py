import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
customer_interactions = pd.read_csv("customer_interactions.csv")
product_details = pd.read_csv("product_details.csv", delimiter=";")
purchase_history = pd.read_csv("purchase_history.csv", delimiter=";")

# Merge data
merged_data = pd.merge(customer_interactions, purchase_history, on="customer_id")

# Load the trained model from disk
model = joblib.load('model.pkl')

# Define Streamlit app
def main():
    st.title('Product Prediction App')

    # Sidebar for user input
    st.sidebar.header('User Input')
    customer_id = st.sidebar.number_input('Customer ID', min_value=1, max_value=999999)
    page_views = st.sidebar.number_input('Page Views', min_value=0)
    time_spent = st.sidebar.number_input('Time Spent', min_value=0.0)

    # Prediction logic
    if st.sidebar.button('Predict'):
        prediction = predict(customer_id, page_views, time_spent)
        st.write(prediction)

# Prediction function
def predict(customer_id, page_views, time_spent):
    # Check if the provided customer_id exists in the data
    if customer_id not in customer_interactions['customer_id'].values:
        return {'error': 'Invalid customer ID.'}

    # Prediction
    prediction = model.predict([[page_views, time_spent]])

    # Get product information
    product_info = product_details[product_details['product_id'] == prediction[0]]

    predicted_product = {
        'product_id': int(prediction[0]),
        'category': product_info['category'].values[0],
        'price': float(product_info['price'].values[0]),
        'ratings': float(product_info['ratings'].values[0])
    }

    return predicted_product

if __name__ == '__main__':
    main()
