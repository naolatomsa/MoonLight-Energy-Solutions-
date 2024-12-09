import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_outliers(data, outliers):
    for column in data.columns:
        if pd.api.types.is_numeric_dtype(data[column]):  # Check if column is numeric
            plt.figure(figsize=(8, 6))
            
            # Drop missing values for the column
            column_data = data[column].dropna()
            
            if not column_data.empty:  # Ensure there's data to plot
            
                sns.boxplot(y=column_data)
                plt.title(f"Boxplot for {column}")

            if column in outliers:
                plt.show()
            else:
                print(f"Skipping column {column}: No data to plot after handling NaNs.")
