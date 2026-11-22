
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Convert salary column to numeric
df["expected_monthly_salary_inr"] = pd.to_numeric(
    df["expected_monthly_salary_inr"], errors="coerce"
)

# Salary analysis by placement status
analysis = df.groupby("placement_status").agg(
    Total_Students=("student_id", "count"),
    Average_Salary=("expected_monthly_salary_inr", "mean"),
    Median_Salary=("expected_monthly_salary_inr", "median"),
    Minimum_Salary=("expected_monthly_salary_inr", "min"),
    Maximum_Salary=("expected_monthly_salary_inr", "max")
)

# Sort by average salary
analysis = analysis.sort_values("Average_Salary", ascending=False)

# Display results
print("\nSalary Expectation by Placement Status")
print("=" * 65)
print(analysis.round(2))
print("=" * 65)

# Average salary chart
plt.figure(figsize=(9, 5))

bars = plt.bar(
    analysis.index,
    analysis["Average_Salary"]
)

plt.title("Average Salary Expectation by Placement Status")
plt.xlabel("Placement Status")
plt.ylabel("Average Monthly Salary (INR)")
plt.xticks(rotation=15)

# Add salary labels
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"Rs. {height:,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()

# Median salary chart
plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index,
    analysis["Median_Salary"]
)

plt.title("Median Salary Expectation by Placement Status")
plt.xlabel("Placement Status")
plt.ylabel("Median Monthly Salary (INR)")
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()
