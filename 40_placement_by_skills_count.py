
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Count the number of skills for each student
df["Skills_Count"] = (
    df["skills"]
    .fillna("")
    .apply(lambda x: len([s.strip() for s in x.split(";") if s.strip() != ""]))
)

# Create skill count groups
df["Skills_Group"] = pd.cut(
    df["Skills_Count"],
    bins=[-1, 2, 4, 6, 100],
    labels=["1-2 Skills", "3-4 Skills", "5-6 Skills", "7+ Skills"]
)

# Identify placed students
df["is_placed"] = df["placement_status"].eq("Placed")

# Group by skill count
analysis = df.groupby("Skills_Group", observed=False).agg(
    Total_Students=("student_id", "nunique"),
    Placed_Students=("is_placed", "sum")
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
).round(2)

# Print results
print("\nPlacement Rate by Number of Skills")
print("=" * 60)
print(analysis.to_string())

# ----------------------------------------
# CHART 1 - PLACEMENT RATE
# ----------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index.astype(str),
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Number of Skills")
plt.xlabel("Number of Skills")
plt.ylabel("Placement Rate (%)")

plt.tight_layout()
plt.show()

# ----------------------------------------
# CHART 2 - STUDENT COUNT
# ----------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index.astype(str),
    analysis["Total_Students"]
)

plt.title("Number of Students by Skills Group")
plt.xlabel("Number of Skills")
plt.ylabel("Total Students")

plt.tight_layout()
plt.show()

# ----------------------------------------
# HIGHEST PLACEMENT RATE
# ----------------------------------------

highest = analysis["Placement_Rate_%"].idxmax()

print("\nGroup with Highest Placement Rate:")
print(highest, "-", analysis.loc[highest, "Placement_Rate_%"], "%")
