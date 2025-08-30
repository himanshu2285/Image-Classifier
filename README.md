# 🖼️ Image Classifier - AI App  

A simple **AI-powered Image Classification Web App** built with **Streamlit** and **TensorFlow**.  
This app classifies images into one of the **10 CIFAR-10 categories** using a pre-trained deep learning model.  

👉 [Live Demo on Streamlit Cloud](https://himanshu-model-image-classifier.streamlit.app/)  

---

## 🚀 Features
- 📤 Upload any image directly from your device.  
- 🤖 Get instant predictions from a trained deep learning model.  
- 🎨 Visualize results with clean UI using **Streamlit**.  
- ☁️ Deployable on **Streamlit Cloud**.  

---

## 📂 Project Structure
Image-Classifier/
│
├── images/ # Sample images
├── cifar10_model.h5 # Pre-trained model
├── main.py # Streamlit app script
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🛠️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/himanshu2285/Image-Classifier.git
cd Image-Classifier

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App Locally
streamlit run main.py


Now open your browser at 👉 http://localhost:8501