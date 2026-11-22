import pandas as pd

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_student_survey_1000.csv")

# Total number of students
print("Total students:", len(df))

# Government and private job preferences
print("\nJob preference count:")
print(df["preferred_sector"].value_counts())

# Students from each stream
print("\nDegree stream count:")
print(df["stream"].value_counts())

# Placement status
print("\nPlacement status:")
print(df["placement_status"].value_counts())

# Average expected salary
print("\nAverage expected salary:")
print(df["expected_monthly_salary_inr"].mean())