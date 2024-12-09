import pandas as pd

def detect_outliers(data):
    outlier = {}
    for column in data.columns:
        if data[column].dtype in ['float64', 'int64']:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)

            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outlier_condition = (data[column] < lower_bound) | (data[column] > upper_bound)
            outlier[column] = data[column][outlier_condition].values
    return outlier
