import tkinter as tk
from tkinter import messagebox
import re
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from feature_extractor import load_data
from ml_based_detector import extract_features

# Train model once when GUI starts
def train_model():
    df = load_data()
    features = df['url'].apply(extract_features)
    X = features
    y = df['label']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

# Predict from a single URL
def predict_url(model, url):
    feature_series = extract_features(url)
    feature_df = pd.DataFrame([feature_series])  # Keep column names
    prediction = model.predict(feature_df)[0]
    return prediction


# Tkinter GUI
def start_gui():
    model = train_model()

    def on_check():
        url = entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return

        result = predict_url(model, url)
        if result == 1:
            result_label.config(text="⚠️ Phishing URL Detected!", fg="red")
        else:
            result_label.config(text="✅ Safe / Legitimate URL", fg="green")

    window = tk.Tk()
    window.title("Phishing URL Detector")
    window.geometry("450x200")
    window.resizable(False, False)

    tk.Label(window, text="Enter URL to Check:", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(window, width=50, font=("Arial", 12))
    entry.pack(pady=5)

    check_button = tk.Button(window, text="Check URL", command=on_check, font=("Arial", 11), bg="#007acc", fg="white")
    check_button.pack(pady=10)

    result_label = tk.Label(window, text="", font=("Arial", 14))
    result_label.pack()

    window.mainloop()

if __name__ == "__main__":
    start_gui()
