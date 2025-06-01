# -------------------------------------
# ECG Image Classification - AI Based App
# -------------------------------------

import os
import cv2
import joblib
import base64
import numpy as np
from PIL import Image
import streamlit as st
import tensorflow as tf


# Page Config
st.set_page_config(
    page_title="🫀 ECG Image Classifier",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Title
st.title("🫀 ECG Image Classifier using Deep Learning")
st.markdown("""
This application allows you to upload an ECG image and classify it into one of the following categories:

- 💓 Abnormal Heartbeat  
- 🦠 COVID-19  
- ❤️ Myocardial Infarction (MI)  
- 🔁 MI History (PMI)  
- ✅ Normal  
""")

# Load the model and scaler
@st.cache_resource
def load_model_and_scaler():
    model = tf.keras.models.load_model(r"AI-Powered ECG Image Analysis\ecg_model.h5")
    scaler = joblib.load(r"AI-Powered ECG Image Analysis\mscaler.pkl")
    return model, scaler

model, scaler = load_model_and_scaler()

# Image Preprocessing (224x224 RGB + Scaling)
def preprocess_image(image: Image.Image):
    img = image.resize((224, 224)).convert("RGB")
    img_np = np.array(img).astype("float32") / 255.0
    img_flat = img_np.reshape(-1)
    img_scaled = scaler.transform([img_flat])
    img_ready = img_scaled.reshape(224, 224, 3)
    return img_ready

# Upload Image & Predict
st.subheader("📤 Upload ECG Image for Classification")

uploaded_file = st.file_uploader("Upload an ECG image (PNG, JPG)", type=["jpg", "jpeg", "png"])

class_labels = ['Abnormal_HeartBeat', 'Covid_19', 'MI', 'MI_History', 'Normal']
class_icons = {
    'Abnormal_HeartBeat': '💓',
    'Covid_19': '🦠',
    'MI': '❤️',
    'MI_History': '🔁',
    'Normal': '✅'
}

if uploaded_file is not None:
    # Show uploaded image
    st.image(uploaded_file, caption="Uploaded ECG Image", use_column_width=True)

    # Convert and preprocess image
    image = Image.open(uploaded_file)
    input_image = preprocess_image(image)
    input_tensor = np.expand_dims(input_image, axis=0)

    # Make prediction
    predictions = model.predict(input_tensor)[0]
    predicted_index = np.argmax(predictions)
    predicted_class = class_labels[predicted_index]
    confidence = predictions[predicted_index] * 100

    # Display prediction
    st.markdown(f"### 🧠 Predicted Class: {class_icons[predicted_class]} **{predicted_class}**")
    st.metric(label="🔎 Confidence", value=f"{confidence:.2f}%")

    # Show probabilities for all classes
    st.subheader("📊 Class Probabilities")
    prob_df = {
        class_labels[i]: f"{predictions[i]*100:.2f}%" for i in range(len(class_labels))
    }

    # Create a horizontal bar chart
    st.bar_chart(data=np.array(predictions), use_container_width=True)

# Footer with Icons
st.markdown("---")
st.markdown("""
<div style="text-align: center; line-height: 1.2;">
    <h4 style="margin-bottom: 0;">👤 Developed by <strong>Rupak C. Jogi</strong></h4>
    <p style="font-size: 16px; color: gray; margin-top: 2px;">
        Data Scientist | AI/ML | Deep Learning | Computer Vision | AI in Healthcare
    </p>
</div>
""", unsafe_allow_html=True)

# Social Footer
footer_social = f"""
<div style="text-align: center; padding-top: 6px;">
    <a href="https://github.com/RCJ360" target="_blank" style="margin: 0 10px;">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" height="24" width="24" />
    </a>
    <a href="https://www.linkedin.com/in/rupak-jogi-py-aiml/" target="_blank" style="margin: 0 10px;">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" height="24" width="24" />
    </a>
</div>
"""

st.markdown(footer_social, unsafe_allow_html=True)