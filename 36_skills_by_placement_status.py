
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Keep only Placed and Seeking Job students
df = df[df["placement_status"].isin(["Placed", "Seeking Job"])].copy()

# Split individual skills
skills = (
    df[["student_id", "placement_status", "skills"]]
    .dropna(subset=["skills"])
    .assign(skills=lambda x: x["skills"].str.split(";"))
    .explode("skills")
)

# Clean skill names
skills["skills"] = skills["skills"].str.strip()

# Remove empty skills
skills = skills[skills["skills"] != ""]

# Avoid duplicate skills for the same student
skills = skills.drop_duplicates(["student_id", "skills"])

# Analyse skills by placement status
analysis = skills.groupby(["placement_status", "skills"]).size().reset_index(name="Student_Count")

# Calculate percentage within each placement group
group_totals = df.groupby("placement_status")["student_id"].nunique()

analysis["Percentage"] = analysis.apply(
    lambda row: round(
        row["Student_Count"] / group_totals[row["placement_status"]] * 100, 2
    ),
    axis=1
)

# ----------------------------------------
# PLACED STUDENTS
# ----------------------------------------

placed_analysis = (
    analysis[analysis["placement_status"] == "Placed"]
    .sort_values("Student_Count", ascending=False)
)

print("\nTop Skills Among Placed Students")
print("=" * 50)
print(placed_analysis.head(10).to_string(index=False))

# Chart - Placed students
top_placed = placed_analysis.head(10).sort_values("Student_Count")

plt.figure(figsize=(10, 6))

plt.barh(
    top_placed["skills"],
    top_placed["Student_Count"]
)

plt.title("Top 10 Skills Among Placed Students")
plt.xlabel("Number of Students")
plt.ylabel("Skills")

plt.tight_layout()
plt.show()

# ----------------------------------------
# SEEKING JOB STUDENTS
# ----------------------------------------

seeking_analysis = (
    analysis[analysis["placement_status"] == "Seeking Job"]
    .sort_values("Student_Count", ascending=False)
)

print("\nTop Skills Among Students Seeking Jobs")
print("=" * 50)
print(seeking_analysis.head(10).to_string(index=False))

# Chart - Seeking job students
top_seeking = seeking_analysis.head(10).sort_values("Student_Count")

plt.figure(figsize=(10, 6))

plt.barh(
    top_seeking["skills"],
    top_seeking["Student_Count"]
)

plt.title("Top 10 Skills Among Students Seeking Jobs")
plt.xlabel("Number of Students")
plt.ylabel("Skills")

plt.tight_layout()
plt.show()
