import pandas as pd
import matplotlib.pyplot as plt

# Load sensor data from a CSV file (replace with your actual file path)
csv_file = 'sensor_data.csv'
df = pd.read_csv(csv_file)

# Explore the data (optional)
print(df.head())  # Display the first few rows
print(df.describe())  # Summary statistics

# Extract temperature column (assuming it's labeled 'temperature')
temperature_data = df['temperature']

# Calculate average temperature
average_temp = temperature_data.mean()
print(f"Average Temperature: {average_temp:.2f} °C")

# Plot temperature data
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], temperature_data, marker='o', linestyle='-', label='Temperature')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Data Analysis')
plt.grid(True)
plt.legend()
plt.show()
