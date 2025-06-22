from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from feature_extractor import load_data
from ml_based_detector import extract_features
from flask import send_file

app = Flask(__name__)

# Train model once at startup
df = load_data()
X = df['url'].apply(extract_features)
y = df['label']
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        url = request.form["url"].strip()
        if url:
            features = pd.DataFrame([extract_features(url)])
            prediction = model.predict(features)[0]
            result = "⚠️ Phishing URL" if prediction == 1 else "✅ Legitimate URL"

            # Save to CSV
            entry = {"url": url, "result": result}
            df_entry = pd.DataFrame([entry])
            if not os.path.exists("history.csv"):
                df_entry.to_csv("history.csv", index=False)
            else:
                df_entry.to_csv("history.csv", mode='a', index=False, header=False)

    # Load history from file
    history = []
    if os.path.exists("history.csv"):
        history = pd.read_csv("history.csv").to_dict(orient="records")

    return render_template("index.html", result=result, history=history)

# ✅ Route to clear history
@app.route("/clear", methods=["POST"])
def clear_history():
    if os.path.exists("history.csv"):
        os.remove("history.csv")
    return redirect(url_for("index"))


@app.route("/download", methods=["GET"])
def download_history():
    if os.path.exists("history.csv"):
        return send_file("history.csv", as_attachment=True)
    else:
        return "⚠️ No history available to download.", 404


if __name__ == "__main__":
    app.run(debug=True)
