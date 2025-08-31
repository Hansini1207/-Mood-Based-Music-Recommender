# 🎵 Mood-Based Music Recommender using KMeans++ Clustering

This project clusters and recommends **Telugu songs** based on audio features using **unsupervised machine learning**. Users can explore songs by mood, filter and sort results, and enjoy an interactive music discovery experience built with **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**.

---

## 🔍 Problem Statement

People often associate music with emotions. Most recommendation systems rely on explicit user preferences or genres. This project focuses on clustering songs based on **audio characteristics** to capture their underlying mood, enabling a more **emotionally-driven music exploration**.

---

## 🎯 Objectives

1. Preprocess and clean a dataset of Telugu songs.  
2. Scale and cluster songs using **KMeans++** based on audio features.  
3. Map clusters to **mood labels** by analyzing average feature profiles.  
4. Build an interactive **Streamlit web app** where users can:  
   - Select a mood  
   - View songs matching the selected mood  
   - Filter or sort songs by singer, popularity, or tempo  
   - Search for songs using partial names  

---

## 🧪 Prework: Experiments & Learnings

### 1. Why Unsupervised Learning?
- No predefined mood labels were available.  
- Supervised models (SVM, Neural Nets, Decision Trees) require labeled data → not available.  
- Unsupervised clustering allows discovery of patterns without ground truth.  

### 2. Clustering Algorithms Tried
| Algorithm | Outcome |
|-----------|---------|
| KMeans / KMeans++ ✅ | Efficient on high-dimensional data; stable, balanced clusters; chosen final method |
| Agglomerative Clustering | Produced unbalanced clusters |
| DBSCAN | Most points marked as noise |
| Gaussian Mixture Models (GMM) | Soft clustering, but imbalanced cluster sizes |

**Final Choice:** KMeans++ with k=5 (trade-off between interpretability & stability).

### 3. Dimensionality Reduction & Visualization
- **PCA:** Reduced feature space to visualize clusters  
- **t-SNE:** Non-linear visualization to confirm mood-based grouping  

### 4. Pseudo-Labeling (Early Testing)
- Created artificial labels (e.g., danceability > 0.5 = “high danceability”)  
- Mapped clusters to pseudo-labels for evaluation (accuracy, confusion matrix)  
- Confirmed clusters capture meaningful musical properties  

---

## 📈 Mood Clustering

### 1. Elbow Method
- Plotted inertia vs number of clusters → k=5 chosen as optimal  

### 2. KMeans++ Clustering
- Applied on scaled features; each song assigned a cluster ID (0–4)  
- Centroids initialized via KMeans++ for better convergence  

### 3. Mood Mapping (Labeling Clusters)
| Cluster | Mood Label |
|---------|------------|
| 0 | Chill / Feel-Good |
| 1 | Sad / Calm |
| 2 | Dance / Energetic |
| 3 | Romantic / Soothing |
| 4 | Instrumental / Longform |

---

## 🌐 Streamlit Web App

**Features:**
- Select mood from dropdown  
- View songs in the selected cluster  
- Filters: singer, release year range  
- Sort: popularity, tempo, etc.  
- Partial search on song names  

UI mimics a realistic music exploration website.

---

## ⚙️ Data Preprocessing

1. **Duration Handling:** Converted mm:ss → seconds  
2. **Missing Values:** Dropped rows with invalid durations  
3. **Feature Selection:** `duration`, `danceability`, `acousticness`, `energy`, `liveness`, `loudness`, `speechiness`, `tempo`, `mode`, `key`, `Valence`, `time_signature`, `popularity`  
4. **Scaling:** Standardized with **StandardScaler** (zero mean, unit variance)

---

## 📁 Dataset Overview

- **Name:** `telugu_songs.csv`  
- **Source:** [Kaggle - Spotify Indian Languages Dataset](https://www.kaggle.com/datasets/gayathripullakhandam/spotify-indian-languages-datasets?select=Telugu_songs.csv)  
- **Size:** ~5,000 songs  
- **Language:** Telugu (multi-language support possible)  

---

## 🧠 Key Learnings

- KMeans++ is efficient and interpretable for audio clustering  
- Standardization & feature selection impact clustering quality  
- Clustering allows mapping songs to moods without labeled data  
- Frontend UX is crucial: clear mood labels, song titles, and filtering options improve usability  

---

## 📌 Future Enhancements

- Add multi-language support with a unified UI  
- Integrate Spotify API for real-time streaming & previews  
- Store user mood selections to create personalized recommendations  

---

## 🗂️ Folder Structure & Workflow

| Step | File | Purpose |
|------|------|--------|
| 1 | `scripts/explore_data.py` | Load & inspect raw dataset (`data/telugu_songs.csv`) |
| 2 | `scripts/prepare_data.py` | Convert durations, standardize features; outputs `processed_telugu_songs.csv` & `processed_features.csv` |
| 3 | `scripts/cluster_songs.py` | Apply Elbow Method & KMeans++ clustering; outputs `clustered_songs.csv` |
| 4 | `scripts/analyze_clusters.py` | Calculate average feature values per cluster; outputs `cluster_summary.csv` |
| 5 | `scripts/label_clusters.py` | Map clusters to human-readable moods; outputs `songs_with_moods.csv` |
| 6 | `app.py` | Streamlit web application |

---

## 🚀 How to Run

1. Install requirements:

```bash
pip install -r requirements.txt

2. Run the Streamlit app:

```bash
streamlit run app.py
