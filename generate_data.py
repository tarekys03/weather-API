import pandas as pd
import numpy as np

def generate_weather_data(num_rows=100, save_path="sample_weather_data.csv"):
    np.random.seed(42)  # For reproducibility

    data = {
        "Temperature": np.random.uniform(-5, 35, num_rows),   # Celsius
        "Humidity": np.random.uniform(10, 60, num_rows),      # %
        "Barometer": np.random.uniform(20, 35, num_rows),     # Example range
        "Windspeed": np.random.uniform(0, 25, num_rows),      # km/h
        "Rain": np.random.uniform(0, 5, num_rows),            # mm/h
        "Light": np.random.uniform(100, 800, num_rows),       # Lux
    }

    df = pd.DataFrame(data)
    df.to_csv(save_path, index=False)
    print(f"✅ Generated {num_rows} rows of weather data and saved to '{save_path}'")

# Run directly if this file is executed
if __name__ == "__main__":
    generate_weather_data()
