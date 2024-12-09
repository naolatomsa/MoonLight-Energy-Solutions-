import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def plot_correlation_heatmap(data, columns, title="Correlation Matrix", figsize=(8, 6), cmap="coolwarm"):

    # Select relevant columns
    selected_data = data[columns]
    
    # Compute correlation matrix
    correlation_matrix = selected_data.corr()
    
    # Plot heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(correlation_matrix, annot=True, cmap=cmap, fmt=".2f", square=True)
    plt.title(title, fontsize=14)
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    st.pyplot(plt)
    