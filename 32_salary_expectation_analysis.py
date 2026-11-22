
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Convert salary column to numeric
df["expected_monthly_salary_inr"] = pd.to_numeric(
    df["expected_monthly_salary_inr"], errors="coerce"
)

# Remove missing salary values for analysis
salary = df["expected_monthly_salary_inr"].dropna()

# Calculate salary KPIs
average_salary = salary.mean()
median_salary = salary.median()
minimum_salary = salary.min()
maximum_salary = salary.max()

# Print salary summary
print("\nSalary Expectation Analysis")
print("=" * 40)

print(f"Total Students          : {len(df)}")
print(f"Students with Salary Data: {len(salary)}")
print(f"Average Salary         : Rs. {average_salary:.2f}")
print(f"Median Salary         : Rs. {median_salary:.2f}")
print(f"Minimum Salary       : Rs. {minimum_salary:.2f}")
print(f"Maximum Salary       : Rs. {maximum_salary:.2f}")

print("=" * 40)

# Create histogram
plt.figure(figsize=(9, 5))

plt.hist(salary, bins=10, edgecolor="black")

plt.title("Student Expected Monthly Salary Distribution")
plt.xlabel("Expected Monthly Salary (INR)")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()

# Create box plot
plt.figure(figsize=(8, 4))

plt.boxplot(salary)

plt.title("Salary Expectation Box Plot")
plt.ylabel("Expected Monthly Salary (INR)")
plt.xticks([1], ["Students"])

plt.tight_layout()
plt.show()
