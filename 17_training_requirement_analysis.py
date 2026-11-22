
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Count training requirement
training_count = df["training_required"].value_counts()

print("\nTraining Requirement Analysis")
print(training_count)

# Calculate percentage
training_percentage = (
    df["training_required"].value_counts(normalize=True) * 100
)

print("\nTraining Requirement Percentage")
print(training_percentage.round(2))

# Plot chart
plt.figure(figsize=(8, 5))

training_count.plot(kind="bar")

plt.title("Student Training Requirements")
plt.xlabel("Training Required")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
