
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Convert salary column to numeric
df["expected_monthly_salary_inr"] = pd.to_numeric(
    df["expected_monthly_salary_inr"],
    errors="coerce"
)

# Create salary expectation groups
df["Salary_Group"] = pd.cut(
    df["expected_monthly_salary_inr"],
    bins=[0, 20000, 25000, 30000, 35000, 50000],
    labels=[
        "Below 20,000",
        "20,000-25,000",
        "25,000-30,000",
        "30,000-35,000",
        "Above 35,000"
    ]
)

# Identify placed students
df["is_placed"] = df["placement_status"].eq("Placed")

# Remove rows without salary data
salary_df = df.dropna(subset=["Salary_Group"]).copy()

# ----------------------------------------
# ANALYSIS
# ----------------------------------------

analysis = salary_df.groupby("Salary_Group", observed=False).agg(
    Total_Students=("student_id", "nunique"),
    Placed_Students=("is_placed", "sum")
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
).round(2)

print("\nPlacement Rate by Salary Expectation")
print("=" * 65)
print(analysis.to_string())

# ----------------------------------------
# CHART 1 - PLACEMENT RATE
# ----------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    analysis.index.astype(str),
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Salary Expectation")
plt.xlabel("Expected Monthly Salary (INR)")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=25, ha="right")

plt.tight_layout()
plt.show()

# ----------------------------------------
# CHART 2 - NUMBER OF STUDENTS
# ----------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    analysis.index.astype(str),
    analysis["Total_Students"]
)

plt.title("Students by Salary Expectation")
plt.xlabel("Expected Monthly Salary (INR)")
plt.ylabel("Number of Students")
plt.xticks(rotation=25, ha="right")

plt.tight_layout()
plt.show()

# ----------------------------------------
# HIGHEST PLACEMENT RATE
# ----------------------------------------

valid_analysis = analysis.dropna(subset=["Placement_Rate_%"])

if not valid_analysis.empty:
    highest_group = valid_analysis["Placement_Rate_%"].idxmax()

    print("\nHighest Placement Rate Salary Group")
    print("-" * 45)
    print("Salary Group:", highest_group)
    print("Placement Rate:", valid_analysis.loc[highest_group, "Placement_Rate_%"], "%")
