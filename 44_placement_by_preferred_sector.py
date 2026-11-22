
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Identify placed students
df["is_placed"] = df["placement_status"].eq("Placed")

# Group by preferred job sector
analysis = df.groupby("preferred_sector").agg(
    Total_Students=("student_id", "nunique"),
    Placed_Students=("is_placed", "sum")
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
).round(2)

# Sort by placement rate
analysis = analysis.sort_values("Placement_Rate_%", ascending=False)

# Print results
print("\nPlacement Rate by Preferred Job Sector")
print("=" * 60)
print(analysis.to_string())

# ------------------------------------------
# CHART 1 - PLACEMENT RATE
# ------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index,
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Preferred Job Sector")
plt.xlabel("Preferred Job Sector")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# ------------------------------------------
# CHART 2 - STUDENT COUNT
# ------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index,
    analysis["Total_Students"]
)

plt.title("Number of Students by Preferred Job Sector")
plt.xlabel("Preferred Job Sector")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# ------------------------------------------
# HIGHEST PLACEMENT RATE
# ------------------------------------------

highest = analysis.iloc[0]

print("\nHighest Placement Rate Sector")
print("--------------------------------")
print("Sector:", analysis.index[0])
print("Placement Rate:", highest["Placement_Rate_%"], "%")
