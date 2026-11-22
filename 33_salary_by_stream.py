
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Convert salary to numeric
df["expected_monthly_salary_inr"] = pd.to_numeric(
    df["expected_monthly_salary_inr"], errors="coerce"
)

# Salary analysis by degree stream
analysis = df.groupby("stream").agg(
    Total_Students=("student_id", "count"),
    Average_Salary=("expected_monthly_salary_inr", "mean"),
    Median_Salary=("expected_monthly_salary_inr", "median"),
    Minimum_Salary=("expected_monthly_salary_inr", "min"),
    Maximum_Salary=("expected_monthly_salary_inr", "max")
)

# Display results
print("\nSalary Expectation by Degree Stream")
print("=" * 60)
print(analysis.round(2))
print("=" * 60)

# Sort streams by average salary
analysis_sorted = analysis.sort_values(
    "Average_Salary", ascending=False
)

# Create average salary bar chart
plt.figure(figsize=(9, 5))

bars = plt.bar(
    analysis_sorted.index,
    analysis_sorted["Average_Salary"]
)

plt.title("Average Salary Expectation by Degree Stream")
plt.xlabel("Degree Stream")
plt.ylabel("Average Monthly Salary (INR)")

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

plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# Create median salary chart
plt.figure(figsize=(9, 5))

plt.bar(
    analysis.index,
    analysis["Median_Salary"]
)

plt.title("Median Salary Expectation by Degree Stream")
plt.xlabel("Degree Stream")
plt.ylabel("Median Monthly Salary (INR)")

plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
