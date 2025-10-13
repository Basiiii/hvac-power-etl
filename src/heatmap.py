import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the processed data
df = pd.read_csv("../power_efficiency.csv", parse_dates=["timestamp"])

# Produce the correlation heatmap
corr = df[["avg_power", "outdoor_temp", "temp_diff", "efficiency"]].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=300)
plt.close()
