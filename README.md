# 🔬🩺 AI-Powered _ECG_ Image Analysis App

A comprehensive case study and research paper implementation utilizing deep learning techniques to accurately classify ECG images into five distinct medical categories. Developed with VGG-19 and advanced CNN architectures, this solution is seamlessly deployed via Streamlit, featuring a professional and user-friendly interface for enhanced accessibility and efficiency.

---
## 🎯 Objectives & Key Highlights
This project explores the power of deep learning in ECG image classification, providing an AI-driven approach for cardiac and COVID-related diagnostics.
### 🔍 Core Objectives:
   - Implement and evaluate CNN-based models on ECG image data.
   - Utilize image preprocessing techniques (OpenCV) to enhance signal clarity.
   - Develop an interactive web application using Streamlit for healthcare professionals.
   - Demonstrate the impact of deep learning in medical image diagnostics.

---

## 🚀 Key Highlights:
  - Advanced Deep Learning Models: Built using ANN, CNN, and VGG-19 for ECG classification.
  - Data Preprocessing: Improved model performance with SMOTE and OpenCV-based enhancement techniques.
  - End-to-End Pipeline: Data → Model → Deployment, streamlining AI-powered workflows.
  - Interactive Web App: Real-time ECG classification deployed via Streamlit with a professional UI.
  - Performance Analysis: Comparative study between ANN and CNN models, proving CNN’s superiority for image-based classification.

---

## 🗂 Dataset & Paper

- **Dataset Source:** [ECG Images dataset of Cardiac and COVID-19 Patients](https://www.sciencedirect.com/science/article/pii/S2352340921000469)  
- **DOI:** [10.17632/gwbz3fsgp8.1](http://dx.doi.org/10.17632/gwbz3fsgp8.1)

---

## 📊 Model Comparison (ANN vs CNN)

| Model     | Accuracy | Notes                                       |
|-----------|----------|---------------------------------------------|
| ANN       | 20.13%   | Poor results, proves ANN is not suited for raw image data |
| CNN       | 90.45%   | Excellent performance, slight overfitting   |
| VGG-19    | 86.38%   | Strong balance between accuracy and generalization |

✅ This practical comparison proves CNNs are far superior to ANN for image-based classification.

---

## 📸 App Interface Preview
<img src='https://github.com/RCJ360/ECG-Image-Classification-App/blob/main/App%20Interface%20Preview.JPG' width='1000' height = '550'>

---

## 🧑‍💻 Developed By
__Rupak C. Jogi__

_Data Scientist & Analyst | AI/ML | Deep Learning Enthusiast_

<div align="center"> <a href="https://github.com/RCJ360" target="_blank" style="margin-right:10px;"> <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="25"/> </a> <a href="https://www.linkedin.com/in/rupak-jogi-py-aiml/" target="_blank"> <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25"/> </a> </div>

---

## 💻 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/RCJ360/ECG-Image-Classification-App.git
cd ecg-image-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
