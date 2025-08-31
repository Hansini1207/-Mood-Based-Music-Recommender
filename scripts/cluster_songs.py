import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# Step 1: Load scaled feature data
df_scaled = pd.read_csv("data/processed_features.csv")

# Step 2: Choose number of clusters (moods)
k = 5
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
df_scaled['mood_cluster'] = kmeans.fit_predict(df_scaled)

# Step 3: Save clustered features (for PCA plot etc.)
df_scaled.to_csv("data/songs_with_clusters.csv", index=False)
print("✅ Clustered features saved to: data/songs_with_clusters.csv")

# Step 4: Visualize clusters using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(df_scaled.drop(columns=['mood_cluster']))
df_scaled['pca1'] = X_pca[:, 0]
df_scaled['pca2'] = X_pca[:, 1]

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_scaled, x="pca1", y="pca2", hue="mood_cluster", palette="Set2", s=80)
plt.title("🎧 Mood Clusters (PCA View)")
plt.savefig("data/cluster_plot.png")
plt.show()

# Step 5: Merge clusters back into original song metadata
original_df = pd.read_csv("data/processed_telugu_songs.csv")
original_df["mood_cluster"] = df_scaled["mood_cluster"]

# Step 6: Save final dataset with mood clusters
original_df.to_csv("data/final_clustered_telugu_songs.csv", index=False)
print("💾 Final dataset saved to: data/final_clustered_telugu_songs.csv")


df = pd.read_csv("data/final_clustered_telugu_songs.csv")
print(df.columns.tolist())
