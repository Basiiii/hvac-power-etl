import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Load the processed data
df = pd.read_csv("../data/output/power_efficiency.csv", parse_dates=["timestamp"])

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

# === Plot 3: 3D Scatter — Outdoor Temp vs Temp Diff vs Avg Power ===
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
scatter = ax.scatter(
    df["outdoor_temp"],
    df["temp_diff"],
    df["avg_power"],
    c=df.get("efficiency", df["avg_power"]),
    cmap="viridis",
)
ax.set_xlabel("Outdoor Temp (°C)")
ax.set_ylabel("Temp Diff (°C)")
ax.set_zlabel("Avg Power")
plt.title("3D View: Power vs Temp Factors")
plt.tight_layout()
plt.savefig("3d_power_temp.png", dpi=300)
plt.close()

# === Plot 4: Histogram of Efficiency ===
plt.figure(figsize=(8, 6))
plt.hist(df["efficiency"], bins=20, color="green", alpha=0.7)
plt.xlabel("Efficiency")
plt.ylabel("Frequency")
plt.title("Distribution of HVAC Efficiency")
plt.grid(True)
plt.tight_layout()
plt.savefig("efficiency_hist.png", dpi=300)
plt.close()

# === Plot 5: Boxplot of Avg Power per Room ===
plt.figure(figsize=(8, 6))
sns.boxplot(x="room", y="avg_power", hue="room", data=df, palette="Set2", legend=False)
plt.xlabel("Room")
plt.ylabel("Average Power")
plt.title("Power Usage per Room")
plt.tight_layout()
plt.savefig("avg_power_boxplot.png", dpi=300)
plt.close()

print(
    "Saved: power_vs_outdoor_temp.png, power_vs_temp_diff.png, 3d_power_temp.png, "
    "efficiency_hist.png, avg_power_boxplot.png"
)
