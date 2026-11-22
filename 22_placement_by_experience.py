import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# Use the SAME CSV path as your previous working Python files
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Convert experience_months to numeric
df["experience_months"] = pd.to_numeric(
    df["experience_months"], errors="coerce"
).fillna(0)

# Create experience groups
df["Experience_Group"] = pd.cut(
    df["experience_months"],
    bins=[-1, 0, 6, 12, float("inf")],
    labels=["No Experience", "1-6 Months", "7-12 Months", "Above 12 Months"]
)

# Placement analysis
analysis = df.groupby("Experience_Group", observed=False).agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("placement_status", lambda x: (x == "Placed").sum())
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
)

# Print results
print("\nPlacement Rate by Experience")
print(analysis.round(2))

# Plot chart
plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index.astype(str),
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Experience")
plt.xlabel("Experience Group")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()