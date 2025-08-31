# app.py

import streamlit as st
import pandas as pd

# Load songs with mood labels
df = pd.read_csv("data/songs_with_moods.csv")

# ---- SIDEBAR ----
st.sidebar.title("🎵 Mood-Based Recommender")

# Dropdown to select mood
mood_options = df["mood_label"].unique()
selected_mood = st.sidebar.selectbox("Select a mood", sorted(mood_options))

# Search input
search_text = st.sidebar.text_input("Search by song or singer", "")

# Duration filter
min_dur = int(df["duration_sec"].min())
max_dur = int(df["duration_sec"].max())
duration_range = st.sidebar.slider("Filter by duration (sec)", min_dur, max_dur, (min_dur, max_dur))

# Popularity filter
min_pop = int(df["popularity"].min())
max_pop = int(df["popularity"].max())
popularity_range = st.sidebar.slider("Filter by popularity", min_pop, max_pop, (min_pop, max_pop))

# Sort options
sort_by = st.sidebar.selectbox("Sort by", ["popularity", "duration_sec"])
sort_order = st.sidebar.radio("Order", ["Descending", "Ascending"])

# ---- MAIN CONTENT ----
st.title("🎧 Mood-Based Music Recommender")
st.write(f"Showing songs for mood: **{selected_mood}**")

# Filter by mood
filtered_df = df[df["mood_label"] == selected_mood]

# Apply search
if search_text:
    search_text = search_text.strip().lower()
    filtered_df = filtered_df[
        filtered_df["song_name"].str.lower().str.contains(search_text, na=False) |
        filtered_df["singer"].str.lower().str.contains(search_text, na=False)
    ]


# Apply duration and popularity filters
filtered_df = filtered_df[
    (filtered_df["duration_sec"] >= duration_range[0]) &
    (filtered_df["duration_sec"] <= duration_range[1]) &
    (filtered_df["popularity"] >= popularity_range[0]) &
    (filtered_df["popularity"] <= popularity_range[1])
]

# Sort
ascending = sort_order == "Ascending"
filtered_df = filtered_df.sort_values(by=sort_by, ascending=ascending)

# Display
st.dataframe(filtered_df[["song_name", "singer", "duration_sec", "popularity"]].reset_index(drop=True))
