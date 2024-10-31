import streamlit as st
import pandas as pd
import numpy as np

st.write("ZenCode Dashbboard")
st.write("## ZenCode data analysis Dashboard")
x = st.text_input("Movie", "Star Wars")

if st.button("Click Me"):
    st.write(f"Your favorite movie is `{x}`")


data = pd.read_csv("movies.csv")
st.write(data)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Release Year", "Type", "Genres"])

st.bar_chart(chart_data)
