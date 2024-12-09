import pandas as pd
import numpy as np

def z_score_analysis(data, threshold=3):
    # Select numeric columns
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    z_score_results = pd.DataFrame()

    # Calculate Z-scores and outliers
    for column in numeric_columns:
        mean = data[column].mean()
        std = data[column].std()
        z_scores = (data[column] - mean) / std

        z_score_results[f"{column}_zscore"] = z_scores
        z_score_results[f"{column}_outlier"] = np.abs(z_scores) > threshold

    # Combine original data with Z-score results
    combined_data = pd.concat([data, z_score_results], axis=1)

    return combined_data
