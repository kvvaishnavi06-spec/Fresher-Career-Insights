
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Count students by placement status
status_count = df["placement_status"].value_counts()

# Calculate percentages
status_percentage = (status_count / len(df) * 100).round(2)

# Create analysis table
status_analysis = pd.DataFrame({
    "Students": status_count,
    "Percentage": status_percentage
})

print("\nPlacement Status Analysis")
print(status_analysis)

# Create chart
plt.figure(figsize=(9, 5))

bars = plt.bar(status_count.index, status_count.values)

plt.title("Student Placement Status")
plt.xlabel("Placement Status")
plt.ylabel("Number of Students")
plt.xticks(rotation=20)

# Add student count above bars
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
