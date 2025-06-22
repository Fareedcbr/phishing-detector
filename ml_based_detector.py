import pandas as pd
from feature_extractor import load_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import re

# 🔧 Step 1: Feature Extraction Function
def extract_features(url):
    features = {
        'url_length': len(url),
        'has_ip': 1 if re.match(r"http[s]?://\d+\.\d+\.\d+\.\d+", url) else 0,
        'has_at': 1 if '@' in url else 0,
        'count_dots': url.count('.'),
        'count_hyphens': url.count('-'),
        'count_slashes': url.count('/'),
        'has_https': 1 if url.startswith('https') else 0,
        'count_www': url.count('www'),
        'suspicious_tld': 1 if any(tld in url for tld in ['.tk', '.ml', '.ga', '.cf', '.gq']) else 0,
        'has_double_slash': 1 if url.count('//') > 1 else 0
    }
    return pd.Series(features)

# 🚀 Step 2: Load Data & Extract Features
def prepare_data():
    df = load_data()
    feature_df = df['url'].apply(extract_features)
    feature_df['label'] = df['label']
    return feature_df

# 🤖 Step 3: Train ML Model
def train_and_evaluate():
    df = prepare_data()
    X = df.drop('label', axis=1)
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\n✅ ML Model Evaluation Results")
    print("🎯 Accuracy:", accuracy_score(y_test, y_pred) * 100, "%")
    print("\n📊 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("\n📝 Classification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    train_and_evaluate()
