
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Group by government exam interest
analysis = df.groupby("government_exam_interest").agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("placement_status", lambda x: (x == "Placed").sum())
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
)

# Display results
print("\nPlacement Rate by Government Exam Interest")
print(analysis.round(2))

# Create bar chart
plt.figure(figsize=(8, 5))

bars = plt.bar(
    analysis.index.astype(str),
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Government Exam Interest")
plt.xlabel("Government Exam Interest")
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
