
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Count placement status
status_count = df["placement_status"].value_counts()

# Calculate percentage
status_percentage = (
    df["placement_status"].value_counts(normalize=True) * 100
)

# Combine results into a table
analysis = pd.DataFrame({
    "Students": status_count,
    "Percentage": status_percentage.round(2)
})

# Print results
print("\nPlacement Status Analysis")
print("=" * 45)
print(analysis)

# Bar chart
plt.figure(figsize=(9, 5))

bars = plt.bar(
    analysis.index,
    analysis["Students"]
)

plt.title("Student Placement Status Distribution")
plt.xlabel("Placement Status")
plt.ylabel("Number of Students")
plt.xticks(rotation=15)

# Add student counts on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        str(int(height)),
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()

# Pie chart
plt.figure(figsize=(8, 6))

plt.pie(
    analysis["Students"],
    labels=analysis.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Placement Status Percentage")
plt.tight_layout()
plt.show()
