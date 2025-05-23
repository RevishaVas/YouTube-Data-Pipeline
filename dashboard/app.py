import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect(host="postgres", dbname="yt", user="postgres", password="pass")
df = pd.read_sql("SELECT * FROM videos ORDER BY published_at DESC", conn)

st.title("📊 YouTube Video Dashboard")
st.write("Latest videos on 'data engineering':")
st.dataframe(df)
