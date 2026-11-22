import pandas as pd

df = pd.read_csv("../Dataset/chennai_fresher_student_survey_1000.csv")

# Analyse placement status
status_count = df["placement_status"].value_counts()

print("Student Placement Analysis")
print("=======================")
print(status_count)

# Calculate percentage
status_percentage = df["placement_status"].value_counts(normalize=True) * 100

print("\nPlacement Percentage:")
print(status_percentage.round(2))

# Government vs Private Job Preference

print("\nGovernment vs Private Job Preference")
print("=================================")

sector_count = df["preferred_sector"].value_counts()

print(sector_count)

sector_percentage = df["preferred_sector"].value_counts(normalize=True) * 100

print("\nSector Preference Percentage:")
print(sector_percentage.round(2))
print(df["stream"].value_counts())
# Job preference percentage

job_percentage = (
    df["preferred_sector"].value_counts(normalize=True) * 100
)

print("\nJob Preference Percentage:")
print(job_percentage.round(2))


# Degree stream percentage

stream_percentage = (
    df["stream"].value_counts(normalize=True) * 100
)

print("\nDegree Stream Percentage:")
print(stream_percentage.round(2))


# Placement status percentage

placement_percentage = (
    df["placement_status"].value_counts(normalize=True) * 100
)

print("\nPlacement Status Percentage:")
print(placement_percentage.round(2))