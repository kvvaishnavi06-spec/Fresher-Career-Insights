import pandas as pd

df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Check placement for each student
df["is_placed"] = (df["placement_status"] == "Placed").astype(int)

# Compare internship groups
result = df.groupby("internship_experience").agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("is_placed", "sum")
)

# Calculate placement percentage
result["Placement_Rate_%"] = (
    result["Placed_Students"] / result["Total_Students"] * 100
).round(2)

print("\nInternship vs Placement Analysis")
print(result)
