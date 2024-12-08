import matplotlib.pyplot as plt

def plot_histograms(data, columns=None, bins=20, color='blue'):
    if columns is None:
        columns = data.select_dtypes(include='number').columns.tolist()

    for column in columns:
        if column in data.columns:
            plt.figure(figsize=(8, 6))
            plt.hist(data[column].dropna(), bins=bins, color=color, edgecolor='black', alpha=0.7)
            plt.title(f'Histogram for {column}', fontsize=14)
            plt.xlabel(column, fontsize=12)
            plt.ylabel('Frequency', fontsize=12)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.show()
        else:
            print(f"Column '{column}' not found in the dataset.")
