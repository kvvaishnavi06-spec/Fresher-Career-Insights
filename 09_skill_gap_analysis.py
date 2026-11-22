
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Step 2: Filter students seeking jobs
job_seekers = df[df["placement_status"] == "Seeking Job"]

# Step 3: Count training requirements
skill_count = job_seekers["training_required"].value_counts()

# Step 4: Calculate percentage
skill_percentage = (skill_count / len(job_seekers) * 100).round(2)

# Step 5: Combine into a table
skill_analysis = pd.DataFrame({
    "Students": skill_count,
    "Percentage": skill_percentage
})

# Step 6: Display results
print("\nStudent Skill Gap Analysis")
print(skill_analysis)

# Step 7: Create chart
plt.figure(figsize=(10, 6))

bars = plt.barh(skill_count.index, skill_count.values)

plt.title("Training Requirements Among Job Seekers")
plt.xlabel("Number of Students")
plt.ylabel("Training Required")

# Add labels to bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2,
             str(int(width)), va="center")

plt.tight_layout()
plt.show()
