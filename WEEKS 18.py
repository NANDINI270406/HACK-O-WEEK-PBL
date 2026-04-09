import pandas as pd
import matplotlib.pyplot as plt

# Load your Kaggle dataset (ensure CSV path is correct)
df = pd.read_csv('proximity_data.csv')

# Convert time column to datetime if necessary
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Compute average distance
avg_dist = df['distance'].mean()
print(f"Average Proximity: {avg_dist:.2f} units")

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['distance'], color='blue', label='Proximity Trend')
plt.axhline(y=avg_dist, color='red', linestyle='--', label='Mean Distance')
plt.title('Time-Series Proximity Visualization')
plt.xlabel('Time')
plt.ylabel('Distance')
plt.legend()
plt.show()
