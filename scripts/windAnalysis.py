from windrose import WindroseAxes
import matplotlib.pyplot as plt

def analyze_wind(data, wind_speed_col='WS', wind_dir_col='WD', wind_dir_stdev_col='WDstdev'):

    # Check if the required columns exist
    required_columns = [wind_speed_col, wind_dir_col, wind_dir_stdev_col]
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"Dataset must contain the following columns: {required_columns}")
    
    # Drop rows with missing or invalid values
    wind_data = data.dropna(subset=[wind_speed_col, wind_dir_col])
    
    # Ensure wind direction is within 0–360 degrees
    wind_data = wind_data[(wind_data[wind_dir_col] >= 0) & (wind_data[wind_dir_col] <= 360)]
    
    # Create a wind rose
    ax = WindroseAxes.from_ax()
    ax.bar(
        wind_data[wind_dir_col], 
        wind_data[wind_speed_col], 
        normed=True, 
        opening=0.8, 
        edgecolor='white'
    )
    ax.set_legend(title="Wind Speed (m/s)", loc="upper left", bbox_to_anchor=(1, 1))

    # Add title
    plt.title("Wind Rose: Distribution of Wind Speed and Direction")
    plt.show()

    # Analyze Wind Variability
    variability_mean = wind_data[wind_dir_stdev_col].mean()
    print(f"Average Wind Direction Variability (Standard Deviation): {variability_mean:.2f}°")
    
    return variability_mean
