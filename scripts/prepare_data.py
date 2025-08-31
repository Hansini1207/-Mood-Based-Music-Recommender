import pandas as pd
import os
from sklearn.preprocessing import StandardScaler

# File paths
INPUT_CSV = "data/telugu_songs.csv"
OUTPUT_CSV_CLEANED = "data/processed_telugu_songs.csv"
OUTPUT_CSV_SCALED = "data/processed_features.csv"

# Helper: Convert 'mm:ss' duration to seconds
def duration_to_seconds(duration_str):
    try:
        parts = duration_str.strip().split(':')
        if len(parts) == 2:
            minutes, seconds = map(int, parts)
            return minutes * 60 + seconds
        elif len(parts) == 3:
            hours, minutes, seconds = map(int, parts)
            return hours * 3600 + minutes * 60 + seconds
        else:
            return None
    except:
        return None

# Step 1: Load and clean dataset
if not os.path.exists(INPUT_CSV):
    print(f"❌ File not found: {INPUT_CSV}")
else:
    df = pd.read_csv(INPUT_CSV)
    print("✅ Loaded original dataset!")

    # Convert and clean duration
    df['duration_sec'] = df['duration'].apply(duration_to_seconds)
    before = df.shape[0]
    df = df.dropna(subset=['duration_sec'])
    after = df.shape[0]
    print(f"🧹 Dropped {before - after} rows with invalid duration format.")

    # Save cleaned version (optional)
    df.to_csv(OUTPUT_CSV_CLEANED, index=False)
    print(f"📁 Cleaned data saved to: {OUTPUT_CSV_CLEANED}")

    # Step 2: Select and scale features
    features = [
        'duration_sec', 'danceability', 'acousticness', 'energy', 'liveness', 
        'loudness', 'speechiness', 'tempo', 'mode', 'key', 
        'Valence', 'time_signature', 'popularity'
    ]

    X = df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    df_scaled = pd.DataFrame(X_scaled, columns=features)
    df_scaled.to_csv(OUTPUT_CSV_SCALED, index=False)
    print(f"📊 Scaled features saved to: {OUTPUT_CSV_SCALED}")

    # Preview
    print("\n🔍 Sample of cleaned & scaled data:")
    print(df_scaled.head())
