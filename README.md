


 # 🏥 AI Healthcare Assistant

An intelligent web-based healthcare system that uses Artificial Intelligence and Machine Learning to provide early health risk detection and medical assistance


## Problem Statement

Healthcare diagnosis is time-consuming and requires expert analysis. 
This project aims to provide an AI-powered system that can assist in early detection of diseases, heart risk, ECG abnormalities, and medical image diagnosis.
## Solution/Overview
We built an AI-based healthcare assistant that:
- Predicts heart disease risk
- Analyzes ECG signals
- Detects diseases from input data
- Classifies medical images

All models are integrated into a single web application using Flask.
## Features
- 🫀 Heart Disease Prediction
- 📈 ECG Analysis
- 🧬 Disease Detection
- 🖼️ Medical Image Classification
- 🌐 User-friendly Web Interface

## Tech Stack

- Python(backend)
- Flask(Web Framework)
- Scikit-learn(Machine Learning)
- TensorFlow / Keras(Image model)
- Pillow(Image Handling)
- HTML, CSS(Frontend)
- NumPy, Pandas(Data Processing)


## Project Structure
📁 Project Structure
<pre>

AI_Healthcare_Project/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── uploads/
│
├── train_heart_model.py
├── train_ecg_model.py
├── train_disease_model.py
├── train_image_model.py
│
├── heart_model.pkl
├── disease_model.pkl
├── ecg_model.pkl
├── image_model.pkl

</pre>

⚠️ Important Note About ".pkl" Files

- The ".pkl" files (models) are NOT written manually
- They are automatically generated after training

🔁 How they are created:

Run the training scripts:

python train_heart_model.py
python train_ecg_model.py
python train_disease_model.py
python train_image_model.py

After running these, the following files will be created:

- "heart_model.pkl"
- "disease_model.pkl"
- "ecg_model.pkl"
- "image_model.pkl"

---

🧠 Explanation

- ".py" files → Used to train models
- ".pkl" files → Store trained models (generated automatically)
- "app.py" → Loads ".pkl" files and runs the web app

---

🚨 If ".pkl" files are missing

Just run the training scripts again to regenerate them.
## How to Run


### 1. Clone the repository
git clone https://github.com/Jasha-coder242/AI_HEALTHCARE_REPORT.git

### 2. Install dependencies
pip install flask numpy scikit-learn opencv-python pillow tensorflow

### 3. Train models (if not included)
train_heart_model.<br>>
train_ecg_model.py<br>
train_disease_model.py<br>
train_image_model.py<br>


### 4. Run the app
python app.py

### 5. Open in browser
http://127.0.0.1:5000/
## How It Works
1.Users uploads medical data or uploads image<br>
2.Data is sent to backend(Flask)<br>
3.ML models process the input<br>
4.Prediction is generated<br>
5.Result is displayed on web interface

## Sample Input & Output
---

## 📌 Sample Inputs

### Heart Risk
- Age: 55  
- BP: 150  
- Cholesterol: 240  
- Heart Rate: 95  

### Disease Prediction
- Fever: 1  
- Cough: 1  
- Fatigue: 1  

---

## 📈 Output Examples

- High Heart Disease Risk  
- Possible Disease Detected  
- Abnormal ECG  
- Disease Detected from Image
## Demo

https://youtube.com/watch?v=f8h-AuDxe2Y&si=af2x4Omz-I-PpclF


## Future Scope
- Add real-time patient monitoring
- Improve model accuracy
- Deploy on cloud (AWS / Azure)
- Add chatbot for medical assistance

## Contributors
-Shreyashee Ghosh<br>
-Jashaswi Saha<br>
-Sumana Santra<br>
-Prerona Hait<br>
## Why This Project Stands Out
- Combines multiple AI healthcare models into ONE platform
- Real-world application in early disease detection
- Scalable and deployable solution
