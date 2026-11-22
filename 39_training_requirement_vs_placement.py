
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Identify students placed
df["is_placed"] = df["placement_status"].eq("Placed")

# Group by training requirement
analysis = df.groupby("training_required").agg(
    Total_Students=("student_id", "nunique"),
    Placed_Students=("is_placed", "sum")
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
).round(2)

# Sort by placement rate (highest first)
analysis = analysis.sort_values("Placement_Rate_%", ascending=False)

# Print results
print("\nPlacement Rate by Training Requirement")
print("=" * 60)
print(analysis.to_string())

# ----------------------------------------
# CHART 1 - PLACEMENT RATE
# ----------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    analysis.index,
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Training Requirement")
plt.xlabel("Training Requirement")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()

# ----------------------------------------
# CHART 2 - PLACED STUDENTS
# ----------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    analysis.index,
    analysis["Placed_Students"]
)

plt.title("Number of Placed Students by Training Requirement")
plt.xlabel("Training Requirement")
plt.ylabel("Number of Placed Students")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()

# ----------------------------------------
# HIGHEST AND LOWEST PLACEMENT RATE
# ----------------------------------------

highest = analysis.iloc[0]
lowest = analysis.iloc[-1]

print("\nHighest Placement Rate")
print(
    f"{analysis.index[0]}: "
    f"{highest['Placement_Rate_%']}%"
)

print("\nLowest Placement Rate")
print(
    f"{analysis.index[-1]}: "
    f"{lowest['Placement_Rate_%']}%"
)
