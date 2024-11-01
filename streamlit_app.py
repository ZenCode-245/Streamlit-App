import streamlit as st
import pandas as pd
import numpy as np

st.write("ZenCode Dashbboard New Update 22")
st.write("## Trend")

# Load the CSV data
data = pd.read_csv('cpd.csv')

# Group by 'loc_state' and count the total number of rows for each state
state_counts = data['loc_state'].value_counts().reset_index()
state_counts.columns = ['loc_state', 'Total Rows']

# Sort the data by 'Total Rows' in ascending order
state_counts = state_counts.sort_values(by='Total Rows', ascending=True)

# Plot the bar chart
st.bar_chart(state_counts.set_index("loc_state"))

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Sentiment")

source = data

st.bar_chart(source, x="Sentiment", y="loc_state", color="loc_state", horizontal=True)


with col3:
    st.header("Column 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")
