import streamlit as st
from EDA.benin import eda_benin
from EDA.sierraleone import eda_sierraleone
from EDA.togo import eda_togo

# Set page configuration
st.set_page_config(page_title="EDA", layout="wide")

st.title("Solar Radiation Data Analysis and Insights")
st.title("For MoonLight Energy Solutions")

# Sidebar with links as buttons
st.sidebar.title("Select Region")
home_button = st.sidebar.button("Benin Malanville")
analysis_button = st.sidebar.button("Sierraleone Bumbuna")
about_button = st.sidebar.button("Togo Dapaong Qc")

# Logic to show content based on the button clicked
if home_button:
    st.title("EDA for Benin Malanville")
    eda_benin()

elif analysis_button:
    st.title("EDA Sierraleone Bumbuna")
    eda_sierraleone()
    
elif about_button:
    st.title("EDA for Togo Dapaong Qc")
    eda_togo()


