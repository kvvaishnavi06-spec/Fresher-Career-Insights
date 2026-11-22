
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Split skills using semicolon
skills = (
    df["skills"]
    .dropna()
    .astype(str)
    .str.split(";")
    .explode()
    .str.strip()
)

# Remove empty values
skills = skills[skills != ""]

# Count individual skills
skill_count = skills.value_counts()

# Calculate percentage of students having each skill
skill_percentage = (skill_count / len(df)) * 100

# Create summary table
analysis = pd.DataFrame({
    "Student_Count": skill_count,
    "Percentage_of_Students": skill_percentage.round(2)
})

# Display results
print("\nIndividual Student Skill Analysis")
print("=" * 50)
print(analysis.to_string())

# Top 10 skills
top_10 = analysis.head(10)

# Chart 1 - Vertical bar chart
plt.figure(figsize=(10, 6))

bars = plt.bar(top_10.index, top_10["Student_Count"])

plt.title("Top 10 Skills Among Students")
plt.xlabel("Skills")
plt.ylabel("Number of Students")
plt.xticks(rotation=45, ha="right")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        int(height),
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()

# Chart 2 - Horizontal bar chart
plt.figure(figsize=(10, 6))

plt.barh(
    top_10.index[::-1],
    top_10["Student_Count"].values[::-1]
)

plt.title("Top 10 Student Skills")
plt.xlabel("Number of Students")
plt.ylabel("Skills")

plt.tight_layout()
plt.show()

