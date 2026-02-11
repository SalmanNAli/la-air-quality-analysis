import pandas as pd
import matplotlib.pyplot as plt

# Example: Load air quality data
# Replace 'air_quality.csv' with your real dataset later
try:
    df = pd.read_csv("air_quality.csv")
    print(df.head())

    # Example plot (adjust column names later)
    if "AQI" in df.columns:
        df["AQI"].plot(title="LA Air Quality Index Trends")
        plt.xlabel("Time")
        plt.ylabel("AQI")
        plt.show()
    else:
        print("AQI column not found in dataset.")

except FileNotFoundError:
    print("Dataset not found. Please add air_quality.csv to the project.")
