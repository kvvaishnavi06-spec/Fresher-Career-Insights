
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Identify placed students
df["is_placed"] = df["placement_status"].eq("Placed")

# Group by preferred job role
analysis = df.groupby("preferred_job_role").agg(
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
print("\nPlacement Rate by Preferred Job Role")
print("=" * 70)
print(analysis.to_string())

# ------------------------------------------
# CHART 1 - PLACEMENT RATE BY JOB ROLE
# ------------------------------------------

plt.figure(figsize=(12, 7))

plt.barh(
    analysis.index,
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Preferred Job Role")
plt.xlabel("Placement Rate (%)")
plt.ylabel("Preferred Job Role")

# Highest placement rate at the top
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()

# ------------------------------------------
# CHART 2 - PLACED STUDENTS BY JOB ROLE
# ------------------------------------------

plt.figure(figsize=(12, 7))

plt.barh(
    analysis.index,
    analysis["Placed_Students"]
)

plt.title("Number of Placed Students by Preferred Job Role")
plt.xlabel("Placed Students")
plt.ylabel("Preferred Job Role")

plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()

# ------------------------------------------
# TOP 5 JOB ROLES BY PLACEMENT RATE
# ------------------------------------------

print("\nTop 5 Job Roles by Placement Rate")
print("=" * 60)
print(analysis.head(5).to_string())

# ------------------------------------------
# HIGHEST PLACEMENT RATE
# ------------------------------------------

if not analysis.empty:
    highest = analysis.iloc[0]

    print("\nHighest Placement Rate Job Role")
    print("----------------------------------------")
    print("Job Role:", analysis.index[0])
    print("Placement Rate:", highest["Placement_Rate_%"], "%")
    print("Placed Students:", int(highest["Placed_Students"]))
    print("Total Students:", int(highest["Total_Students"]))
