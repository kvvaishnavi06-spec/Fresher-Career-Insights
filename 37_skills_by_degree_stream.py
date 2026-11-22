
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Split individual skills
skills_df = (
    df[["student_id", "stream", "skills"]]
    .dropna(subset=["skills"])
    .assign(skills=lambda x: x["skills"].str.split(";"))
    .explode("skills")
)

# Clean skill names
skills_df["skills"] = skills_df["skills"].str.strip()

# Remove empty values
skills_df = skills_df[skills_df["skills"] != ""]

# Avoid duplicate skill entries for same student
skills_df = skills_df.drop_duplicates(["student_id", "stream", "skills"])

# Count skills by stream
analysis = (
    skills_df.groupby(["stream", "skills"])
    .size()
    .reset_index(name="Student_Count")
)

# Calculate percentage within each stream
stream_totals = df.groupby("stream")["student_id"].nunique()

analysis["Percentage"] = analysis.apply(
    lambda row: round(
        row["Student_Count"] / stream_totals[row["stream"]] * 100, 2
    ),
    axis=1
)

# ----------------------------------------
# PRINT TOP 5 SKILLS FOR EACH STREAM
# ----------------------------------------

streams = sorted(analysis["stream"].unique())

print("\nTop 5 Skills by Degree Stream")
print("=" * 60)

for stream in streams:
    stream_data = (
        analysis[analysis["stream"] == stream]
        .sort_values("Student_Count", ascending=False)
        .head(5)
    )

    print(f"\n{stream}")
    print("-" * 40)
    print(stream_data[["skills", "Student_Count", "Percentage"]].to_string(index=False))

# ----------------------------------------
# CREATE CHARTS
# ----------------------------------------

for stream in streams:

    top_skills = (
        analysis[analysis["stream"] == stream]
        .sort_values("Student_Count", ascending=False)
        .head(5)
        .sort_values("Student_Count")
    )

    plt.figure(figsize=(8, 5))

    plt.barh(
        top_skills["skills"],
        top_skills["Student_Count"]
    )

    plt.title(f"Top 5 Skills - {stream}")
    plt.xlabel("Number of Students")
    plt.ylabel("Skills")

    plt.tight_layout()
    plt.show()
