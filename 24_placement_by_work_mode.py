
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Group students by preferred work mode
analysis = df.groupby("preferred_work_mode").agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("placement_status",
                    lambda x: (x == "Placed").sum())
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
)

# Display results
print("\nPlacement Rate by Preferred Work Mode")
print(analysis.round(2))

# Plot chart
plt.figure(figsize=(8, 5))

plt.bar(
    analysis.index,
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Preferred Work Mode")
plt.xlabel("Preferred Work Mode")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()
