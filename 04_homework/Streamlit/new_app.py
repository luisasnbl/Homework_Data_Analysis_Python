import pandas as pd
import streamlit as st

df = pd.read_csv("disney_plus_shows.csv")

st.markdown("# Disney+ shows")
st.markdown("Filter the dataset by type (movies vs series).")

types = st.multiselect(
    "Type",
    options=sorted(df["type"].dropna().unique()),
    default=sorted(df["type"].dropna().unique())
)

df_filtered = df[df["type"].isin(types)]

# Title search
search = st.text_input("Search title")
if search:
    df_filtered = df_filtered[df_filtered["title"].str.contains(search, case=False, na=False)]

# Rating slider
df["imdb_rating"] = pd.to_numeric(df["imdb_rating"], errors="coerce")
min_rating = st.slider("Min. IMDb rating", 0.0, 10.0, 0.0, 0.1)
df_filtered = df_filtered[df_filtered["imdb_rating"] >= min_rating]

# Metrics
col1, col2 = st.columns(2)
col1.metric("Titles", len(df_filtered))
col2.metric("Avg. IMDb rating", round(df_filtered["imdb_rating"].mean(), 2))

# Chart of the filtered data
st.bar_chart(df_filtered["rated"].value_counts())

# Download button
st.download_button("Download CSV", df_filtered.to_csv(index=False), "disney_filtered.csv")

#
st.markdown(f"**{len(df_filtered)}** titles")
st.dataframe(df_filtered)