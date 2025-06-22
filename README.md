# 🔐 Phishing Website Detection Tool

## 📌 Problem Statement
Phishing websites are deceptive webpages that trick users into revealing personal or financial information. These attacks contribute heavily to identity theft and online fraud.

## 🎯 Objective
Develop a lightweight tool to detect potentially harmful (phishing) URLs using rule-based logic and machine learning techniques.

---

## 🛠️ Features
- ✅ Detects whether a URL is **phishing** or **legitimate**
- ⚙️ Uses both **Rule-Based** and **Machine Learning (ML)** detection methods
- 🧠 ML model: Random Forest Classifier
- 🗂️ History of checked URLs stored in `history.csv`
- 🧽 Clear history and 📥 download CSV features
- 🌐 Flask-based web app interface (Bootstrap styled)
- 📊 Model accuracy: **94.1%**
- 🧪 Rule-based accuracy: **~69%**

---

## 📁 Folder Structure
```

phishing\_url\_detector/
├── app.py                   # Flask app
├── rule\_based\_detector.py   # Rule-based logic
├── ml\_based\_detector.py     # ML training and prediction
├── feature\_extractor.py     # Feature extraction from URL
├── history.csv              # Stored URL check history
├── requirements.txt         # Python dependencies
├── data/
│   └── phishing\_dataset.xlsx  # Dataset (20k samples)
└── templates/
└── index.html           # HTML UI (Bootstrap)

````

---

## 🔍 Dataset
- **Source**: Publicly available dataset with 20,000 URLs (balanced)
- **Format**: Excel with two columns – `Labels` and `URLs`
- **Preprocessing**: Renamed columns to standard `url` and `label`

---

## 🧪 Detection Methods

### 🔹 Rule-Based Detector
Uses patterns like:
- IP address in domain
- Use of `@`, `-`, `//`
- URL length
- Number of subdomains
- Suspicious keywords like `login`, `secure`, `bank`

### 🔸 ML-Based Detector
- Extracts numerical features from URLs
- Trained using **RandomForestClassifier**
- Achieves over **94% accuracy** on test data

---

## 🚀 How to Run

1. Clone the repository  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
````

3. Run the Flask app:

   ```bash
   python app.py
   ```
4. Open your browser and visit:
   `http://127.0.0.1:5000`

---

## 📌 Future Improvements

* 🔐 Add JWT or session-based authentication
* ☁️ Deploy on cloud (e.g., Render, Railway, Vercel)
* 📱 Add mobile support or convert to desktop app via Tkinter
* 🧠 Test other ML models: XGBoost, SVM
* 📈 Visualization of detection trends

---

## 👨‍💻 Author

**Md Fareeduddin**
BSc Computer Science, Central University of Karnataka
Project developed during internship task under RISE
