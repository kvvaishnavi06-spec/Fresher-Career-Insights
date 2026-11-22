
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Count students by job preference
preference_count = df["preferred_sector"].value_counts()

print("--- JOB PREFERENCE COUNT ---")
print(preference_count)

# Calculate percentages
preference_percentage = (
    df["preferred_sector"].value_counts(normalize=True) * 100
).round(2)

print("\n--- JOB PREFERENCE PERCENTAGE ---")
print(preference_percentage)

# Create summary table
summary = pd.DataFrame({
    "Student_Count": preference_count,
    "Percentage": preference_percentage
})

print("\n--- FINAL SUMMARY ---")
print(summary)
