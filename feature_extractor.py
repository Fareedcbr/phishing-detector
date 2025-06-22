import pandas as pd

def load_data(path="data/phishing_dataset.xlsx"):
    df = pd.read_excel(path, engine='openpyxl')

    # Print actual column names from the file
    print("📋 Available columns:", df.columns.tolist())

    # Use actual column names from your Excel file
    if 'URLs' in df.columns and 'Labels' in df.columns:
        df = df[['URLs', 'Labels']]
        df.columns = ['url', 'label']  # Standardize for consistency
    else:
        raise Exception("❌ Could not find 'URLs' and 'Labels' columns. Please check the Excel sheet.")

    # Clean and prepare
    df = df.dropna()
    df['label'] = df['label'].astype(int)

    print(f"\n✅ Loaded {len(df)} URLs")
    print("📊 Label distribution:\n", df['label'].value_counts())
    return df

if __name__ == "__main__":
    df = load_data()
    print("\n🔍 Sample URLs:")
    print(df.sample(5))
    print("\n✅ Sample data loaded successfully.")
