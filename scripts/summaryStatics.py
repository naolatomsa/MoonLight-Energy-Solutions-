import pandas as pd
def calculate_summary(data):
    return data.drop(columns='Comments').describe()