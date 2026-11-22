
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Average expected salary by preference
salary_analysis = df.groupby("preferred_sector")[
    "expected_monthly_salary_inr"
].mean().round(2)

# Display results
print("\nAverage Expected Monthly Salary by Job Preference")
print(salary_analysis)

# Create chart
plt.figure(figsize=(9, 5))

bars = plt.bar(salary_analysis.index, salary_analysis.values)

plt.title("Average Expected Monthly Salary by Job Preference")
plt.xlabel("Job Sector Preference")
plt.ylabel("Expected Salary (INR per Month)")

# Add salary labels
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 300,
        f"₹{height:,.0f}",
        ha="center"
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
