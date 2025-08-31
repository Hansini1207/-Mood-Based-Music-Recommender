# scripts/assign_moods.py

import pandas as pd

# Load cluster-labeled songs
df = pd.read_csv("data/final_clustered_telugu_songs.csv")

# Define mood labels
mood_map = {
    0: "Instrumental / Longform",
    1: "Chill / Feel-Good",
    2: "Sad / Calm",
    3: "Classical / Devotional",
    4: "Upbeat / Romantic"
}

# Assign mood labels
df["mood_label"] = df["mood_cluster"].map(mood_map)

# Save new dataset with mood labels
output_path = "data/songs_with_moods.csv"
df.to_csv(output_path, index=False)

print("✅ Mood labels assigned and saved to:", output_path)

# Preview
print("\n🔍 Preview of songs with moods:")
print(df[["song_name", "singer", "mood_cluster", "mood_label"]].head())
