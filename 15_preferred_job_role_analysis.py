
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Count preferred job roles
job_role_counts = df["preferred_job_role"].value_counts()

# Print results
print("\nPreferred Job Role Analysis")
print(job_role_counts)

# Create chart
plt.figure(figsize=(10, 6))

bars = plt.barh(
    job_role_counts.index,
    job_role_counts.values
)

plt.title("Most Preferred Job Roles Among Students")
plt.xlabel("Number of Students")
plt.ylabel("Preferred Job Role")

# Add values to bars
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 1,
        bar.get_y() + bar.get_height()/2,
        str(int(width)),
        va="center"
    )

plt.tight_layout()
plt.show()
