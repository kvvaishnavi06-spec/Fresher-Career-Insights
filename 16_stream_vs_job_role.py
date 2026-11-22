
import pandas as pd

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Compare degree stream and preferred job role
analysis = pd.crosstab(
    df["stream"],
    df["preferred_job_role"]
)

print("\nJob Role Preference by Degree Stream")
print(analysis)

# Find the most preferred role for each stream
print("\nMost Preferred Job Role in Each Stream")

for stream in analysis.index:
    top_role = analysis.loc[stream].idxmax()
    student_count = analysis.loc[stream, top_role]

    print(f"{stream}: {top_role} ({student_count} students)")
