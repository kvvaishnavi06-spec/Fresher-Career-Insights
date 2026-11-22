
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Filter students who are seeking jobs
job_seekers = df[df["placement_status"] == "Seeking Job"]

# Count job seekers by degree stream
stream_count = job_seekers["stream"].value_counts()

# Display results
print("Students seeking jobs by stream:")
print(stream_count)

# Create chart
plt.figure(figsize=(10, 6))

bars = plt.bar(stream_count.index, stream_count.values)

plt.title("Job Seekers by Degree Stream")
plt.xlabel("Degree Stream")
plt.ylabel("Number of Students")

# Add values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 2,
        str(int(height)),
        ha="center"
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
