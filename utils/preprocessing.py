import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import os
import sys

def load_and_preprocess(train_path, test_path, save_dir):
   
    try:
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)
    except FileNotFoundError as e:
        print(f" File not found: {e}")
        sys.exit(1)

    print("✅ Loaded train shape:", train_df.shape)
    print("✅ Loaded test shape:", test_df.shape)

    
    test_df.columns = train_df.columns

  
    df = pd.concat([train_df, test_df], axis=0).dropna().drop_duplicates()
    print("✅ Combined data shape after dropna & drop_duplicates:", df.shape)

   
    if df.columns[-1] != 'label':
        df.columns = list(df.columns[:-1]) + ['label']

    
    if df.empty:
        print(" Error: Combined DataFrame is empty after preprocessing.")
        sys.exit(1)

   
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])
        print(f"✅ Encoded column: {col}")

    
    X = df.drop('label', axis=1)
    y = df['label']

    print("✅ Feature shape:", X.shape)
    print("✅ Label shape:", y.shape)

    
    if X.shape[0] == 0:
        print(" Error: No samples found in the dataset. Cannot scale.")
        sys.exit(1)

    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("✅ Features scaled. Shape:", X_scaled.shape)

    
    total_samples = X_scaled.shape[0]
    part_size = total_samples // 4

    os.makedirs(save_dir, exist_ok=True)
    for i in range(4):
        start = i * part_size
        end = (i + 1) * part_size if i < 3 else total_samples
        X_part = X_scaled[start:end]
        y_part = y.iloc[start:end]
        np.savez_compressed(f"{save_dir}/client_{i+1}.npz", X=X_part, y=y_part)
        print(f"✅ Saved client_{i+1}.npz with samples: {X_part.shape[0]}")

    print("*** Preprocessing complete. Data saved to:***", save_dir)


if __name__ == "__main__":
    load_and_preprocess(
        train_path="data/KDDTrain+.csv",
        test_path="data/KDDTest+.csv",
        save_dir="data/clients"
    )
