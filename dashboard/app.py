import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from anomaliesDetectionAndPlot import detect_and_plot_anomalies
from bubbleChart import plot_bubble_chart
from checkingAndCleaningNegativeValues import check_negative_entries
from checkingAndCleaningNegativeValues import replace_negative_with_zero
from checkingAndCleaningNegativeValues import validate_no_negative
from compareSensorReading import plot_sensor_readings
from correlationAndHeatMapping import plot_correlation_heatmap
from detectOutliers import detect_outliers
from handleMissingValue import handle_missing_values
from histogram import plot_histograms
from plotOutliers import plot_outliers
from removeOutliers import remove_outliers
from scatterPlot import plot_scatter_or_regression
from summaryStatics import calculate_summary
from timeSeriesAnalysisMonthlyAndDailyTrend import preprocess_timestamp
from timeSeriesAnalysisMonthlyAndDailyTrend import analyze_and_plot_monthly_trends
from timeSeriesAnalysisMonthlyAndDailyTrend import analyze_and_plot_hourly_trends
from windAnalysis import analyze_wind
from zScore import z_score_analysis

def eda_sierraleone():
    # Load the dataset
    data = pd.read_csv("data/sierraleone-bumbuna.csv")


   # Display summary statistics
    st.subheader("Summary Statistics")
    summary = calculate_summary(data)
    st.write(summary)

    # Handle missing values
    st.subheader("Handling Missing Values")
    data = data.drop(columns='Comments')
    st.write("Missing values removed")

    # Outlier detection
    st.subheader("Outlier Detection")
    outliers = detect_outliers(data)
    plot_outliers(data, outliers)
    
    #remove outliers
    st.subheader("Remove Outlier")
    data = remove_outliers(data, exclude_columns=['Cleaning'])
    plot_outliers(data, outliers)
    
    #checking incrorrect entries
    st.subheader("checking incrorrect entries")
    positiveColumns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust', 'WSstdev', 'BP', 'Precipitation']
    incorrectEntries = check_negative_entries(data, positiveColumns)
    st.write(incorrectEntries)
    
    #replace negative value with zero
    st.subheader("replace negative value with zero")
    columns_to_clean = ['GHI', 'DNI', 'DHI']
    # Replace negative values with zero
    cleaned_data = replace_negative_with_zero(data, columns_to_clean)
    st.write(cleaned_data)
    
    #time series analysis
    st.subheader("Time Series Analysis")
    data = preprocess_timestamp(data)
    st.subheader("plot by monthly trend")
    analyze_and_plot_monthly_trends(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'])
    st.subheader("plot by daily trend")
    analyze_and_plot_hourly_trends(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'])
    st.subheader("Compare Sensor Readings Before and After Cleaning")
    plot_sensor_readings(data, timestamp_col='Timestamp', cleaning_col='Cleaning', mod_a_col='ModA', mod_b_col='ModB')
    
    st.subheader("Highlight Anomalies")
    detect_and_plot_anomalies(data, value_col='GHI', timestamp_col='Timestamp', threshold_percentile=0.95)

    st.subheader("Correlation Matrix and Heatmap")
    columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
    # Plot correlation heatmap and get the matrix
    plot_correlation_heatmap(data, columns, title="Correlation Matrix of Solar Radiation and Wind Conditions")
    
    st.subheader("Wind Analysis")
    analyze_wind(data, wind_speed_col='WS', wind_dir_col='WD', wind_dir_stdev_col='WDstdev')
    
    st.subheader("Teamprature Analysis")
    st.subheader("Scatter Plot Relative Humidity vs Temperature")

    TempData = data.dropna(subset=['RH', 'Tamb', 'GHI'])

    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='Tamb',
        title='Relative Humidity vs Temperature',
        x_label='Relative Humidity (%)',
        y_label='Temperature (°C)',
        color='blue',
        regression=False  # No regression line
    )
    
    st.subheader("scatter Plot: RH vs Solar Radiation")

    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='GHI',
        title='Relative Humidity vs Solar Radiation',
        x_label='Relative Humidity (%)',
        y_label='Solar Radiation (GHI, W/m²)',
        color='green',
        regression=False  # No regression line
    )
    
    st.subheader("Regression Plot: RH vs Temperature")
    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='Tamb',
        title='Relative Humidity vs Temperature(Regression)',
        x_label='Relative Humidity (%)',
        y_label='Temperature (°C)',
        color='blue',
        regression=True  # No regression line
    )
    
    st.subheader("Regression Plot: RH vs Solar Radiation")
    
    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='GHI',
        title='Relative Humidity vs Solar Radiation(Regression)',
        x_label='Relative Humidity (%)',
        y_label='Solar Radiation (GHI, W/m²)',
        color='green',
        regression=True  # No regression line
    )
    
    
    st.subheader("Histogram")
    columns_to_plot = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
    plot_histograms(data, columns=columns_to_plot, bins=20, color='blue')
    
    st.subheader("Z-Score")
    z_score_threshold = 3
    results = z_score_analysis(data, threshold=z_score_threshold)
    st.write(results)
    
    st.subheader("Bubble Chart")
    plot_bubble_chart(
        data=data,
        x_col='GHI',  
        y_col='Tamb',  
        size_col='WS',  
        color_col='RH',  
        title='GHI vs Tamb with Bubble Size as WS and Color as RH',
        xlabel='Global Horizontal Irradiance (GHI)',
        ylabel='Ambient Temperature (Tamb)'
    )


def eda_benin():
    # Load the dataset
    data = pd.read_csv("data/benin-malanville.csv")

    # Display summary statistics
    st.subheader("Summary Statistics")
    summary = calculate_summary(data)
    st.write(summary)

    # Handle missing values
    st.subheader("Handling Missing Values")
    data = data.drop(columns='Comments')
    st.write("Missing values removed")

    # Outlier detection
    st.subheader("Outlier Detection")
    outliers = detect_outliers(data)
    plot_outliers(data, outliers)
    
    #remove outliers
    st.subheader("Remove Outlier")
    data = remove_outliers(data, exclude_columns=['Cleaning'])
    plot_outliers(data, outliers)
    
    #checking incrorrect entries
    st.subheader("checking incrorrect entries")
    positiveColumns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust', 'WSstdev', 'BP', 'Precipitation']
    incorrectEntries = check_negative_entries(data, positiveColumns)
    st.write(incorrectEntries)
    
    #replace negative value with zero
    st.subheader("replace negative value with zero")
    columns_to_clean = ['GHI', 'DNI', 'DHI']
    # Replace negative values with zero
    cleaned_data = replace_negative_with_zero(data, columns_to_clean)
    st.write(cleaned_data)
    
    #time series analysis
    st.subheader("Time Series Analysis")
    data = preprocess_timestamp(data)
    st.subheader("plot by monthly trend")
    analyze_and_plot_monthly_trends(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'])
    st.subheader("plot by daily trend")
    analyze_and_plot_hourly_trends(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'])
    st.subheader("Compare Sensor Readings Before and After Cleaning")
    plot_sensor_readings(data, timestamp_col='Timestamp', cleaning_col='Cleaning', mod_a_col='ModA', mod_b_col='ModB')
    
    st.subheader("Highlight Anomalies")
    detect_and_plot_anomalies(data, value_col='GHI', timestamp_col='Timestamp', threshold_percentile=0.95)

    st.subheader("Correlation Matrix and Heatmap")
    columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
    # Plot correlation heatmap and get the matrix
    plot_correlation_heatmap(data, columns, title="Correlation Matrix of Solar Radiation and Wind Conditions")
    
    st.subheader("Wind Analysis")
    analyze_wind(data, wind_speed_col='WS', wind_dir_col='WD', wind_dir_stdev_col='WDstdev')
    
    st.subheader("Teamprature Analysis")
    st.subheader("Scatter Plot Relative Humidity vs Temperature")

    TempData = data.dropna(subset=['RH', 'Tamb', 'GHI'])

    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='Tamb',
        title='Relative Humidity vs Temperature',
        x_label='Relative Humidity (%)',
        y_label='Temperature (°C)',
        color='blue',
        regression=False  # No regression line
    )
    
    st.subheader("scatter Plot: RH vs Solar Radiation")

    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='GHI',
        title='Relative Humidity vs Solar Radiation',
        x_label='Relative Humidity (%)',
        y_label='Solar Radiation (GHI, W/m²)',
        color='green',
        regression=False  # No regression line
    )
    
    st.subheader("Regression Plot: RH vs Temperature")
    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='Tamb',
        title='Relative Humidity vs Temperature(Regression)',
        x_label='Relative Humidity (%)',
        y_label='Temperature (°C)',
        color='blue',
        regression=True  # No regression line
    )
    
    st.subheader("Regression Plot: RH vs Solar Radiation")
    
    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='GHI',
        title='Relative Humidity vs Solar Radiation(Regression)',
        x_label='Relative Humidity (%)',
        y_label='Solar Radiation (GHI, W/m²)',
        color='green',
        regression=True  # No regression line
    )
    
    
    st.subheader("Histogram")
    columns_to_plot = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
    plot_histograms(data, columns=columns_to_plot, bins=20, color='blue')
    
    st.subheader("Z-Score")
    z_score_threshold = 3
    results = z_score_analysis(data, threshold=z_score_threshold)
    st.write(results)
    
    st.subheader("Bubble Chart")
    plot_bubble_chart(
        data=data,
        x_col='GHI',  
        y_col='Tamb',  
        size_col='WS',  
        color_col='RH',  
        title='GHI vs Tamb with Bubble Size as WS and Color as RH',
        xlabel='Global Horizontal Irradiance (GHI)',
        ylabel='Ambient Temperature (Tamb)'
    )
def eda_togo():
    # Load the dataset
    data = pd.read_csv("data/togo-dapaong_qc.csv")


   # Display summary statistics
    st.subheader("Summary Statistics")
    summary = calculate_summary(data)
    st.write(summary)

    # Handle missing values
    st.subheader("Handling Missing Values")
    data = data.drop(columns='Comments')
    st.write("Missing values removed")

    # Outlier detection
    st.subheader("Outlier Detection")
    outliers = detect_outliers(data)
    plot_outliers(data, outliers)
    
    #remove outliers
    st.subheader("Remove Outlier")
    data = remove_outliers(data, exclude_columns=['Cleaning'])
    plot_outliers(data, outliers)
    
    #checking incrorrect entries
    st.subheader("checking incrorrect entries")
    positiveColumns = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust', 'WSstdev', 'BP', 'Precipitation']
    incorrectEntries = check_negative_entries(data, positiveColumns)
    st.write(incorrectEntries)
    
    #replace negative value with zero
    st.subheader("replace negative value with zero")
    columns_to_clean = ['GHI', 'DNI', 'DHI']
    # Replace negative values with zero
    cleaned_data = replace_negative_with_zero(data, columns_to_clean)
    st.write(cleaned_data)
    
    #time series analysis
    st.subheader("Time Series Analysis")
    data = preprocess_timestamp(data)
    st.subheader("plot by monthly trend")
    analyze_and_plot_monthly_trends(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'])
    st.subheader("plot by daily trend")
    analyze_and_plot_hourly_trends(data, columns=['GHI', 'DNI', 'DHI', 'Tamb'])
    st.subheader("Compare Sensor Readings Before and After Cleaning")
    plot_sensor_readings(data, timestamp_col='Timestamp', cleaning_col='Cleaning', mod_a_col='ModA', mod_b_col='ModB')
    
    st.subheader("Highlight Anomalies")
    detect_and_plot_anomalies(data, value_col='GHI', timestamp_col='Timestamp', threshold_percentile=0.95)

    st.subheader("Correlation Matrix and Heatmap")
    columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'WS', 'WSgust', 'WD']
    # Plot correlation heatmap and get the matrix
    plot_correlation_heatmap(data, columns, title="Correlation Matrix of Solar Radiation and Wind Conditions")
    
    st.subheader("Wind Analysis")
    analyze_wind(data, wind_speed_col='WS', wind_dir_col='WD', wind_dir_stdev_col='WDstdev')
    
    st.subheader("Teamprature Analysis")
    st.subheader("Scatter Plot Relative Humidity vs Temperature")

    TempData = data.dropna(subset=['RH', 'Tamb', 'GHI'])

    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='Tamb',
        title='Relative Humidity vs Temperature',
        x_label='Relative Humidity (%)',
        y_label='Temperature (°C)',
        color='blue',
        regression=False  # No regression line
    )
    
    st.subheader("scatter Plot: RH vs Solar Radiation")

    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='GHI',
        title='Relative Humidity vs Solar Radiation',
        x_label='Relative Humidity (%)',
        y_label='Solar Radiation (GHI, W/m²)',
        color='green',
        regression=False  # No regression line
    )
    
    st.subheader("Regression Plot: RH vs Temperature")
    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='Tamb',
        title='Relative Humidity vs Temperature(Regression)',
        x_label='Relative Humidity (%)',
        y_label='Temperature (°C)',
        color='blue',
        regression=True  # No regression line
    )
    
    st.subheader("Regression Plot: RH vs Solar Radiation")
    
    plot_scatter_or_regression(
        data=TempData,
        x_col='RH',
        y_col='GHI',
        title='Relative Humidity vs Solar Radiation(Regression)',
        x_label='Relative Humidity (%)',
        y_label='Solar Radiation (GHI, W/m²)',
        color='green',
        regression=True  # No regression line
    )
    
    
    st.subheader("Histogram")
    columns_to_plot = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
    plot_histograms(data, columns=columns_to_plot, bins=20, color='blue')
    
    st.subheader("Z-Score")
    z_score_threshold = 3
    results = z_score_analysis(data, threshold=z_score_threshold)
    st.write(results)
    
    st.subheader("Bubble Chart")
    plot_bubble_chart(
        data=data,
        x_col='GHI',  
        y_col='Tamb',  
        size_col='WS',  
        color_col='RH',  
        title='GHI vs Tamb with Bubble Size as WS and Color as RH',
        xlabel='Global Horizontal Irradiance (GHI)',
        ylabel='Ambient Temperature (Tamb)'
    )


# Set page configuration
st.set_page_config(page_title="EDA", layout="wide")

st.title("Solar Radiation Data Analysis and Insights")
st.title("For MoonLight Energy Solutions")

# Sidebar with links as buttons
st.sidebar.title("Select Region")
home_button = st.sidebar.button("Benin Malanville")
analysis_button = st.sidebar.button("Sierraleone Bumbuna")
about_button = st.sidebar.button("Togo Dapaong Qc")

# Logic to show content based on the button clicked
if home_button:
    st.title("EDA for Benin Malanville")
    eda_benin()

elif analysis_button:
    st.title("EDA Sierraleone Bumbuna")
    eda_sierraleone()
    
elif about_button:
    st.title("EDA for Togo Dapaong Qc")
    eda_togo()


