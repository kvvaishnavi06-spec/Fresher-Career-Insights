
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Convert age to numeric
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Create age groups
df["Age_Group"] = pd.cut(
    df["age"],
    bins=[0, 20, 22, 24, 100],
    labels=["18-20", "21-22", "23-24", "25+"]
)

# Identify placed students
df["is_placed"] = df["placement_status"].eq("Placed")

# Remove missing age groups
age_df = df.dropna(subset=["Age_Group"]).copy()

# ------------------------------------------
# PLACEMENT ANALYSIS
# ------------------------------------------

analysis = age_df.groupby("Age_Group", observed=False).agg(
    Total_Students=("student_id", "nunique"),
    Placed_Students=("is_placed", "sum")
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
).round(2)

# Print results
print("\nPlacement Rate by Age Group")
print("=" * 60)
print(analysis.to_string())

# ------------------------------------------
# CHART 1 - PLACEMENT RATE
# ------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index.astype(str),
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Placement Rate (%)")

plt.tight_layout()
plt.show()

# ------------------------------------------
# CHART 2 - TOTAL STUDENTS
# ------------------------------------------

plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index.astype(str),
    analysis["Total_Students"]
)

plt.title("Number of Students by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()

# ------------------------------------------
# HIGHEST PLACEMENT RATE
# ------------------------------------------

valid_analysis = analysis.dropna(subset=["Placement_Rate_%"])

if not valid_analysis.empty:
    highest_group = valid_analysis["Placement_Rate_%"].idxmax()

    print("\nHighest Placement Rate Age Group")
    print("----------------------------------------")
    print("Age Group:", highest_group)
    print(
        "Placement Rate:",
        valid_analysis.loc[highest_group, "Placement_Rate_%"],
        "%"
    )
