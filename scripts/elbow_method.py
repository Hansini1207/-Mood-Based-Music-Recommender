import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load scaled data
df_scaled = pd.read_csv("data/processed_features.csv")

# Drop non-feature columns (if any)
X = df_scaled

# Try different values of k
wcss = []
K_RANGE = range(1, 11)

for k in K_RANGE:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)  # Inertia = WCSS

# Plotting the Elbow graph
plt.figure(figsize=(8, 5))
plt.plot(K_RANGE, wcss, 'bo-')
plt.title("🦴 Elbow Method for Optimal k")
plt.xlabel("Number of clusters (k)")
plt.ylabel("WCSS (Inertia)")
plt.xticks(K_RANGE)
plt.grid(True)
plt.savefig("data/elbow_plot.png")
plt.show()
