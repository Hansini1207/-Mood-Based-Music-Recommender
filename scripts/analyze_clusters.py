import pandas as pd

# Load clustered dataset
df = pd.read_csv("data/final_clustered_telugu_songs.csv")

# Columns to analyze
audio_features = [
    'danceability', 'energy', 'acousticness', 'Valence',
    'tempo', 'loudness', 'speechiness', 'duration_sec'
]

# Compute mean values of features per cluster
cluster_summary = df.groupby('mood_cluster')[audio_features].mean().round(2)

print("📊 Cluster-wise audio feature averages:\n")
print(cluster_summary)
