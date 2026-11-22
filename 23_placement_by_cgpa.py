import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Convert CGPA to numeric
df["cgpa"] = pd.to_numeric(df["cgpa"], errors="coerce")

# Create CGPA groups
df["CGPA_Group"] = pd.cut(
    df["cgpa"],
    bins=[-float("inf"), 6, 7, 8, float("inf")],
    labels=["Below 6.0", "6.0-6.99", "7.0-7.99", "8.0 and Above"],
    right=False
)

# Placement analysis by CGPA
analysis = df.groupby("CGPA_Group", observed=False).agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("placement_status", lambda x: (x == "Placed").sum())
)

# Calculate placement percentage
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
)

# Display results
print("\nPlacement Rate by CGPA")
print(analysis.round(2))

# Plot chart
plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index.astype(str),
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by CGPA")
plt.xlabel("CGPA Group")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()