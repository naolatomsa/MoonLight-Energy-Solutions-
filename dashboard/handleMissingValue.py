import pandas as pd

def handle_missing_values(data, action="remove"):

    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    
    if action == "check":
        # Report missing value counts
        missing_counts = data.isnull().sum().to_dict()
        return missing_counts
    elif action == "remove":
        # Remove rows with missing values
        return data.dropna()
    elif action == "fill":
        # Fill missing values with the mean of each column
        return data.fillna(data.mean())
    else:
        raise ValueError("Invalid action. Use 'check', 'remove', or 'fill'.")
