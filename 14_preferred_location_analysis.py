import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Step 2: Count students by preferred location
location_counts = df["preferred_location"].value_counts()

# Step 3: Print results
print("\nPreferred Job Location Analysis")
print(location_counts)

# Step 4: Create chart
plt.figure(figsize=(9, 5))

bars = plt.bar(
    location_counts.index,
    location_counts.values
)

plt.title("Student Preferences by Job Location")
plt.xlabel("Preferred Location")
plt.ylabel("Number of Students")
plt.xticks(rotation=30)

# Step 5: Display values
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 2,
        str(int(height)),
        ha="center"
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()