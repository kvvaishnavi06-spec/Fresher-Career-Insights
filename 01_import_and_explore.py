import pandas as pd
from pathlib import Path

# Load the dataset relative to this Python file.
project_folder = Path(__file__).resolve().parent.parent
dataset_path = project_folder / "Dataset" / "chennai_fresher_student_survey_1000.csv"

df = pd.read_csv(dataset_path)

print("\n--- FIRST 5 STUDENTS ---")
print(df.head())

print("\n--- DATASET SIZE ---")
print("Total students:", len(df))
print("Total columns:", len(df.columns))
print("Shape:", df.shape)

print("\n--- DATASET INFORMATION ---")
df.info()

print("\n--- JOB PREFERENCE COUNTS ---")
print(df["preferred_sector"].value_counts())

print("\n--- DEGREE STREAM COUNTS ---")
print(df["stream"].value_counts())

# ==============================
# DATA CLEANING - QUALITY CHECKS
# ==============================

# 1. Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 2. Check duplicate rows
print("\n--- Duplicate Rows ---")
print("Duplicate rows:", df.duplicated().sum())

# 3. Check duplicate student IDs
print("\n--- Duplicate Student IDs ---")
print("Duplicate IDs:", df["student_id"].duplicated().sum())


# ==============================
# DATA CLEANING - VALIDATION
# ==============================

# 1. Check invalid ages
print("\n--- Invalid Ages ---")
print(df[(df["age"] < 18) | (df["age"] > 30)])

# 2. Check invalid CGPA
print("\n--- Invalid CGPA ---")
print(df[(df["cgpa"] < 0) | (df["cgpa"] > 10)])

# 3. Check invalid salary
print("\n--- Invalid Salary ---")
print(df[df["expected_monthly_salary_inr"] < 0])

# 4. Check graduation year
print("\n--- Invalid Graduation Year ---")
print(df[(df["graduation_year"] < 2020) |
          (df["graduation_year"] > 2030)])

# ==============================
# STEP 4 - DATA STANDARDIZATION
# ==============================

# Create a copy of original dataset
df_clean = df.copy()

# 1. Remove unnecessary spaces from text columns
text_columns = df_clean.select_dtypes(include="str").columns

for col in text_columns:
    df_clean[col] = df_clean[col].str.strip()

# 2. Standardize selected categorical columns
categorical_columns = [
    "degree_level",
    "stream",
    "preferred_sector",
    "preferred_job_role",
    "preferred_location",
    "internship_experience",
    "government_exam_interest",
    "private_job_interest",
    "preferred_work_mode",
    "job_readiness",
    "training_required",
    "placement_status"
]

for col in categorical_columns:
    df_clean[col] = df_clean[col].str.title()

# 3. Clean skills column
df_clean["skills"] = df_clean["skills"].str.replace(
    " ;", ";", regex=False
)

# 4. Display cleaned data
print("\n--- CLEANED DATA ---")
print(df_clean.head())

# 5. Check spaces in text
print("\n--- CLEANING COMPLETED ---")
print("Total rows:", df_clean.shape[0])
print("Total columns:", df_clean.shape[1])

# 6. Save cleaned dataset
df_clean.to_csv(
    "../Dataset/chennai_fresher_students_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")

