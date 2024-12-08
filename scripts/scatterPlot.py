import matplotlib.pyplot as plt
import seaborn as sns

def plot_scatter_or_regression(data, x_col, y_col, title, x_label, y_label, color='blue', regression=False):

    plt.figure(figsize=(8, 6))
    if regression:
        sns.regplot(x=x_col, y=y_col, data=data, scatter_kws={'color': color}, line_kws={'color': 'red'})
    else:
        sns.scatterplot(x=x_col, y=y_col, data=data, color=color)
    
    plt.title(title, fontsize=14)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.grid(True)
    plt.show()
