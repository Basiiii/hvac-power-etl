import pandas as pd
import matplotlib.pyplot as plt

# Load the processed data
df = pd.read_csv("../power_efficiency.csv", parse_dates=["timestamp"])

# === Plot 1: Power vs Outdoor Temperature ===
plt.figure(figsize=(8, 6))
plt.scatter(df["outdoor_temp"], df["avg_power"], c="blue", alpha=0.6)
plt.xlabel("Outdoor Temperature (°C)")
plt.ylabel("Average Power")
plt.title("Power Usage vs Outdoor Temperature")
plt.grid(True)
plt.tight_layout()
plt.savefig("power_vs_outdoor_temp.png", dpi=300)
plt.close()

# === Plot 2: Power vs Temperature Difference ===
plt.figure(figsize=(8, 6))
plt.scatter(df["temp_diff"], df["avg_power"], c="orange", alpha=0.6)
plt.xlabel("Temperature Difference (|Outdoor - 21| °C)")
plt.ylabel("Average Power")
plt.title("Power Usage vs Temperature Difference")
plt.grid(True)
plt.tight_layout()
plt.savefig("power_vs_temp_diff.png", dpi=300)
plt.close()

print("✅ Saved: power_vs_outdoor_temp.png and power_vs_temp_diff.png")
