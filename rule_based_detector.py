import re
import pandas as pd
from feature_extractor import load_data

def is_phishing_url(url):
    """
    Rule-based logic to flag suspicious URLs.
    Returns True if phishing, else False.
    """

    # Rule 1: IP address in URL (e.g., http://192.168.0.1)
    if re.search(r"http[s]?://\d+\.\d+\.\d+\.\d+", url):
        return True

    # Rule 2: URL contains '@'
    if '@' in url:
        return True

    # Rule 3: Too many '//'
    if url.count('//') > 2:
        return True

    # Rule 4: URL has hyphen in domain (e.g., my-bank.com)
    if '-' in url.split('/')[2]:
        return True

    # Rule 5: Very long URL
    if len(url) > 75:
        return True

    # Rule 6: Suspicious TLDs
    suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq']
    if any(tld in url for tld in suspicious_tlds):
        return True

    return False

def evaluate_rules():
    df = load_data()
    df['predicted'] = df['url'].apply(is_phishing_url)

    # Convert boolean prediction to int
    df['predicted'] = df['predicted'].astype(int)

    # Accuracy
    correct = (df['label'] == df['predicted']).sum()
    total = len(df)
    accuracy = correct / total * 100

    print(f"\n🔍 Rule-Based Accuracy: {accuracy:.2f}% ({correct}/{total} correct)")

    # Confusion matrix summary
    tp = ((df['label'] == 1) & (df['predicted'] == 1)).sum()
    tn = ((df['label'] == 0) & (df['predicted'] == 0)).sum()
    fp = ((df['label'] == 0) & (df['predicted'] == 1)).sum()
    fn = ((df['label'] == 1) & (df['predicted'] == 0)).sum()

    print(f"\n📊 Confusion Matrix:")
    print(f"TP (correct phishing): {tp}")
    print(f"TN (correct legit):   {tn}")
    print(f"FP (false phishing):  {fp}")
    print(f"FN (missed phishing): {fn}")

if __name__ == "__main__":
    evaluate_rules()
