import streamlit as st
from predict import predict_food
from PIL import Image
import tempfile
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(to right, #ffecd2, #fcb69f);
    }

    /* Title */
    h1 {
        color: #ff4b2b;
        text-align: center;
        font-family: 'Arial';
    }

    /* Upload box */
    .stFileUploader {
        border: 2px dashed #ff4b2b;
        padding: 20px;
        border-radius: 10px;
        background-color: white;
    }

    /* Buttons */
    .stButton>button {
        background-color: #ff4b2b;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
    }

    /* Prediction text */
    .stSubheader {
        color: #333;
        font-weight: bold;
    }

    /* Output text */
    .stMarkdown {
        font-size: 18px;
        color: #222;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🍔 AI Food Calorie Detector")

uploaded_file = st.file_uploader("Upload food image")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_path = temp_file.name

    # Predict
    food, calories = predict_food(temp_path)

    st.success(f"🍽️ Detected Food: {food.upper()}")
    st.info(f"🔥 Estimated Calories: {calories} kcal")