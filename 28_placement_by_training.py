
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Group students by training requirement
analysis = df.groupby("training_required").agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("placement_status", lambda x: (x == "Placed").sum())
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
)

# Sort by placement rate
analysis = analysis.sort_values("Placement_Rate_%", ascending=False)

# Display results
print("\nPlacement Rate by Training Requirement")
print(analysis.round(2))

# Create bar chart
plt.figure(figsize=(10, 6))

bars = plt.barh(
    analysis.index,
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Training Requirement")
plt.xlabel("Placement Rate (%)")
plt.ylabel("Training Required")

# Add percentage labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.1,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.2f}%",
        va="center"
    )

plt.grid(axis="x", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
