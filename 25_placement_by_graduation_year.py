
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Group students by graduation year
analysis = df.groupby("graduation_year").agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("placement_status", lambda x: (x == "Placed").sum())
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
)

# Display analysis
print("\nPlacement Rate by Graduation Year")
print(analysis.round(2))

# Plot bar chart
plt.figure(figsize=(9, 5))

bars = plt.bar(
    analysis.index.astype(str),
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Graduation Year")
plt.xlabel("Graduation Year")
plt.ylabel("Placement Rate (%)")

# Add percentage labels
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
