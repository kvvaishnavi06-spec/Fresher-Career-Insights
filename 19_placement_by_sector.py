
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Identify placed students
df["is_placed"] = df["placement_status"].eq("Placed")

# Group students by preferred job sector
analysis = df.groupby("preferred_sector").agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("is_placed", "sum")
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
)

print("\nPlacement Rate by Preferred Job Sector")
print(analysis.round(2))

# Create chart
plt.figure(figsize=(9, 5))

analysis["Placement_Rate_%"].plot(kind="bar")

plt.title("Placement Rate by Preferred Job Sector")
plt.xlabel("Preferred Job Sector")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
