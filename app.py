
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Nudar's Git Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Git Dashboard")
st.write("Welcome to Nudar's public Git and data dashboard.")

st.header("Project Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Project", "Git Dashboard")

with col2:
    st.metric("Student", "Nudar")

with col3:
    st.metric("Repository", "git-dashboard")

st.header("Sample Data")

data = pd.DataFrame({
    "Category": ["Git", "Python", "Streamlit", "GitHub"],
    "Score": [90, 85, 95, 92]
})

st.dataframe(data, use_container_width=True)

fig, ax = plt.subplots()
ax.bar(data["Category"], data["Score"])
ax.set_xlabel("Technology")
ax.set_ylabel("Score")
ax.set_title("Project Technology Scores")

st.pyplot(fig)

st.success("Dashboard deployed successfully!")
