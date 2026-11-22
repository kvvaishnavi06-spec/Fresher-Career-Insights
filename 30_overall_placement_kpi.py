
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# STEP 30: OVERALL PLACEMENT KPI SUMMARY
# ----------------------------------------

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Total number of students
total_students = len(df)

# Count students by placement status
placement_counts = df["placement_status"].value_counts()

# Number of students placed
placed_students = placement_counts.get("Placed", 0)

# Number of students not placed
not_placed_students = total_students - placed_students

# Overall placement percentage
placement_rate = (placed_students / total_students) * 100

# Other student status counts
seeking_job = placement_counts.get("Seeking Job", 0)
preparing_exams = placement_counts.get("Preparing For Exams", 0)
higher_studies = placement_counts.get("Higher Studies", 0)

# ----------------------------------------
# PRINT KPI SUMMARY
# ----------------------------------------

print("=" * 50)
print("       OVERALL PLACEMENT KPI SUMMARY")
print("=" * 50)

print(f"Total Students           : {total_students}")
print(f"Students Placed         : {placed_students}")
print(f"Students Not Placed     : {not_placed_students}")
print(f"Overall Placement Rate  : {placement_rate:.2f}%")

print("-" * 50)

print(f"Seeking Job            : {seeking_job}")
print(f"Preparing For Exams    : {preparing_exams}")
print(f"Higher Studies        : {higher_studies}")

print("=" * 50)

# ----------------------------------------
# CREATE KPI CHART
# ----------------------------------------

kpi_labels = ["Placed", "Not Placed"]
kpi_values = [placed_students, not_placed_students]

plt.figure(figsize=(8, 5))

plt.bar(kpi_labels, kpi_values)

plt.title("Overall Placement KPI - Chennai Freshers")
plt.xlabel("Placement Status")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.show()

# ----------------------------------------
# PLACEMENT STATUS PIE CHART
# ----------------------------------------

status_labels = [
    "Placed",
    "Seeking Job",
    "Preparing For Exams",
    "Higher Studies"
]

status_values = [
    placed_students,
    seeking_job,
    preparing_exams,
    higher_studies
]

plt.figure(figsize=(8, 6))

plt.pie(
    status_values,
    labels=status_labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Overall Student Placement Status")

plt.tight_layout()
plt.show()
