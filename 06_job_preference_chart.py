
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

preference_count = df["preferred_sector"].value_counts()

# Calculate percentages
percentage = preference_count / len(df) * 100

plt.figure(figsize=(10, 6))

bars = plt.bar(preference_count.index, preference_count.values)

plt.title("Job Sector Preferences Among Students", fontsize=15)
plt.xlabel("Preferred Job Sector")
plt.ylabel("Number of Students")

# Add labels above each bar
for bar, pct in zip(bars, percentage):
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 5,
        f"{int(height)} ({pct:.1f}%)",
        ha="center"
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.show()
