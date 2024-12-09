import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def detect_and_plot_anomalies(data, value_col, timestamp_col, threshold_percentile=0.95):

    # Calculate the threshold value
    threshold = data[value_col].quantile(threshold_percentile)
    
    # Identify anomalies
    anomalies = data[data[value_col] > threshold]

    # Plot data and anomalies
    plt.figure(figsize=(10, 6))
    plt.plot(data[timestamp_col], data[value_col], label=value_col)
    plt.scatter(anomalies[timestamp_col], anomalies[value_col], color='red', label='Anomalies')
    plt.title(f'{value_col} Over Time with Anomalies Highlighted')
    plt.xlabel('Time')
    plt.ylabel(value_col)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    st.pyplot(plt)
    