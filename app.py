import streamlit as st
import pickle
import pandas as pd
import xgboost as xgb

# Load your preprocessed data, XGBoost model, and feature names
X_train_scaled = pd.read_csv("X_train_scaled.csv")

# Replace with your preprocessed X_train data
X_test_scaled = pd.read_csv(
    "X_test_scaled.csv"
)  # Replace with your preprocessed X_test data
y_train_encoded = pd.read_csv(
    "y_train_encoded.csv"
)  # Replace with your preprocessed y_train data
model = pickle.load(open("xgboost_model.pkl", "rb"))
feature_names = X_train_scaled.columns.tolist()

# Create a Streamlit web app
st.title("XGBoost Classification Model")

# Create input widgets for all features
input_features = {}
st.header("Input Features")
for feature in feature_names:
    input_features[feature] = st.number_input(f"Enter {feature}", step=0.01)

# Make predictions
if st.button("Predict"):
    input_data = [input_features[feature] for feature in feature_names]
    input_df = pd.DataFrame([input_data], columns=feature_names)

    # Ensure user input is in the same format as your preprocessed data
    user_input = input_df.values

    # Make predictions with the model
    prediction = model.predict(user_input)
    st.write(f"Prediction: {prediction[0]}")

# Display model information
st.header("Model Information")
st.write("XGBoost Classification Model")
st.write("All Features: ", feature_names)
