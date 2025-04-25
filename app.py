import streamlit as st
from utils.auth import authenticate_user, register_user
from models.crop_price_model import predict_crop_prices
from models.crop_recommendation_model import recommend_crops
from utils.data_loader import load_company_posts, save_company_post

# App Title
st.title("KrishiConnect - Empowering Farmers")

# Navigation
menu = st.sidebar.selectbox("Menu", ["Home", "Login", "Signup", "Crop Price Prediction", "Crop Recommendation", "Crop Marketplace"])

if menu == "Home":
    st.header("Welcome to KrishiConnect")
    st.write("🚜 A platform connecting Farmers and Companies in Karnataka.")
    # TODO: Add summary of current average crop prices
elif menu == "Login":
    st.header("Login")
    role = st.radio("Login as:", ["Farmer", "Company"])
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        if authenticate_user(username, password, role):
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid credentials.")
elif menu == "Signup":
    st.header("Signup")
    role = st.radio("Signup as:", ["Farmer", "Company"])
    name = st.text_input("Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    location = st.text_input("Location")
    if st.button("Signup"):
        if register_user(name, username, password, role, location):
            st.success("User registered successfully! Please login.")
        else:
            st.error("Username already exists.")
elif menu == "Crop Price Prediction":
    st.header("Crop Price Prediction")
    crop = st.selectbox("Select Crop", ["Wheat", "Rice", "Maize", "Sugarcane"])  # Example crops
    location = st.selectbox("Select Location", ["Bangalore", "Mysore"])  # Example locations
    if st.button("Predict"):
        price_predictions = predict_crop_prices(crop, location)
        st.line_chart(price_predictions)
elif menu == "Crop Recommendation":
    st.header("Crop Recommendation")
    location = st.selectbox("Select Location", ["Bangalore", "Mysore"])  # Example locations
    soil_type = st.selectbox("Select Soil Type", ["Clay", "Sandy", "Loamy"])  # Example soil types
    land_size = st.number_input("Enter Land Size (in acres)", min_value=1.0, step=0.1)
    if st.button("Recommend"):
        recommendations = recommend_crops(location, soil_type, land_size)
        st.table(recommendations)
elif menu == "Crop Marketplace":
    st.header("Crop Marketplace")
    role = st.radio("I am a:", ["Farmer", "Company"])
    if role == "Company":
        crop = st.text_input("Crop")
        quantity = st.number_input("Quantity (in tons)", min_value=0.1, step=0.1)
        contact = st.text_input("Contact Information")
        location = st.text_input("Location")
        if st.button("Post Requirement"):
            save_company_post(crop, quantity, contact, location)
            st.success("Requirement posted successfully!")
    else:
        st.subheader("Crop Requirements")
        requirements = load_company_posts()
        st.table(requirements)