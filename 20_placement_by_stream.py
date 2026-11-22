
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Identify placed students
df["is_placed"] = df["placement_status"].eq("Placed")

# Group by degree stream
analysis = df.groupby("stream").agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("is_placed", "sum")
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
)

print("\nPlacement Rate by Degree Stream")
print(analysis.round(2))

# Plot
plt.figure(figsize=(8, 5))

analysis["Placement_Rate_%"].plot(kind="bar")

plt.title("Placement Rate by Degree Stream")
plt.xlabel("Degree Stream")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
