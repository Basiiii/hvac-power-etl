import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("../power_efficiency.csv", parse_dates=["timestamp"])

# Optional: check columns
print(df.head())
print(df.columns)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(df["timestamp"], df["avg_power"], label="Avg Power", color="blue")
plt.plot(df["timestamp"], df["temp_diff"], label="Temp Diff", color="orange")
plt.plot(df["timestamp"], df["efficiency"], label="Efficiency", color="green")
plt.xlabel("Timestamp")
plt.ylabel("Value")
plt.title("Power, Temperature Deviation, and Efficiency Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save to PNG
plt.savefig("power_efficiency_plot.png", dpi=300)
print("Plot saved as power_efficiency_plot.png")
