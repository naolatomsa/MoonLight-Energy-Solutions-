import matplotlib.pyplot as plt
import streamlit as st

def plot_bubble_chart(data, x_col, y_col, size_col, color_col=None, title=None, xlabel=None, ylabel=None):

    plt.figure(figsize=(10, 8))
    
    # Create scatter plot with bubble sizes
    scatter = plt.scatter(
        data[x_col],
        data[y_col],
        s=data[size_col] * 20,  # Scale bubble size for better visibility
        c=data[color_col] if color_col else 'blue',  # Use color_col for color or default to blue
        alpha=0.6,
        cmap='viridis'
    )
    
    # Add a colorbar if a color column is specified
    if color_col:
        cbar = plt.colorbar(scatter)
        cbar.set_label(color_col, fontsize=12)
    
    # Add titles and labels
    plt.title(title or f'{y_col} vs {x_col} with {size_col} as Bubble Size', fontsize=16)
    plt.xlabel(xlabel or x_col, fontsize=14)
    plt.ylabel(ylabel or y_col, fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(plt)
