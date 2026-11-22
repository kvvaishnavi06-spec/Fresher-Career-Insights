
import pandas as pd

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Total students in each stream
total_students = df.groupby("stream").size()

# Students seeking jobs in each stream
job_seekers = df[df["placement_status"] == "Seeking Job"]

seeking_count = job_seekers.groupby("stream").size()

# Combine both results into a single table
analysis = pd.DataFrame({
    "Total Students": total_students,
    "Job Seekers": seeking_count
})

# Replace missing values with zero
analysis = analysis.fillna(0)

# Calculate job seeking percentage
analysis["Job Seeking Rate (%)"] = (
    analysis["Job Seekers"] / analysis["Total Students"] * 100
).round(2)

# Sort by job seeking rate
analysis = analysis.sort_values(
    "Job Seeking Rate (%)",
    ascending=False
)

print("\nJob Seeking Rate by Stream")
print(analysis)
