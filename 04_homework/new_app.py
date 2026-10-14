import pandas as pd
import streamlit as st

df = pd.read_csv("disney_plus_shows.csv")

st.title("Disney+ shows")
st.dataframe(df)