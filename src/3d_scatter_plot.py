from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

# Load the processed data
df = pd.read_csv("../power_efficiency.csv", parse_dates=["timestamp"])

# Produce the 3D scatter plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(
    df["outdoor_temp"],
    df["temp_diff"],
    df["avg_power"],
    c=df["efficiency"],
    cmap="viridis",
)
ax.set_xlabel("Outdoor Temp (°C)")
ax.set_ylabel("Temp Diff (°C)")
ax.set_zlabel("Avg Power")
plt.title("3D View: Power vs Temp Factors")
plt.tight_layout()
plt.savefig("3d_power_temp.png", dpi=300)
plt.close()
