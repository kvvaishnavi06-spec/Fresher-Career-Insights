import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

analysis = df.groupby("degree_level").agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("placement_status", lambda x: (x == "Placed").sum())
)

analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
)

print("Placement Rate by Degree Level")
print(analysis.round(2))

plt.figure(figsize=(8, 5))

plt.bar(
    analysis.index,
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Degree Level")
plt.xlabel("Degree Level")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()