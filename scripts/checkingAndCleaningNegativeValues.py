import pandas as pd

def check_negative_entries(data, columns):

    return data[columns][data[columns] < 0]

def replace_negative_with_zero(data, columns):

    data[columns] = data[columns].apply(lambda col: col.map(lambda x: max(x, 0)))
    return data

def validate_no_negative(data, columns):

    negative_counts = (data[columns] < 0).sum()
    return negative_counts.sum() == 0  # True if all columns have zero negative values
