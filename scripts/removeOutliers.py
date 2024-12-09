import pandas as pd

def remove_outliers(data, columns=None, exclude_columns=None):
    
    # Make a copy of the original DataFrame to avoid modifying it directly
    cleaned_data = data.copy()
    
    # If no columns are specified, process all numeric columns
    if columns is None:
        columns = data.select_dtypes(include=['number']).columns.tolist()
    
    # Exclude specified columns from processing
    if exclude_columns:
        columns = [col for col in columns if col not in exclude_columns]
    
    # Process each column
    for column in columns:
        Q1 = cleaned_data[column].quantile(0.25)  # First quartile
        Q3 = cleaned_data[column].quantile(0.75)  # Third quartile
        
        IQR = Q3 - Q1  # Interquartile range
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Clip outliers to within bounds
        cleaned_data[column] = cleaned_data[column].clip(lower_bound, upper_bound)
    
    return cleaned_data
