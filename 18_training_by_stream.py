
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Compare streams and training requirements
analysis = pd.crosstab(
    df["stream"],
    df["training_required"]
)

print("\nTraining Requirements by Degree Stream")
print(analysis)

# Find the most required training for each stream
print("\nTop Training Requirement by Stream")

for stream in analysis.index:
    top_skill = analysis.loc[stream].idxmax()
    count = analysis.loc[stream, top_skill]

    print(f"{stream}: {top_skill} ({count} students)")

# Visualize
analysis.plot(kind="bar", figsize=(10, 6))

plt.title("Training Requirements by Degree Stream")
plt.xlabel("Degree Stream")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.legend(title="Training Skill")
plt.tight_layout()
plt.show()
