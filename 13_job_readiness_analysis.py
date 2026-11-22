
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Step 2: Identify placed students
df["is_placed"] = (df["placement_status"] == "Placed").astype(int)

# Step 3: Group students by job readiness
analysis = df.groupby("job_readiness").agg(
    Total_Students=("student_id", "count"),
    Placed_Students=("is_placed", "sum")
)

# Step 4: Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
).round(2)

# Step 5: Print results
print("\nJob Readiness vs Placement Analysis")
print(analysis)

# Step 6: Create chart
plt.figure(figsize=(8, 5))

bars = plt.bar(
    analysis.index,
    analysis["Placement_Rate_%"]
)

plt.title("Placement Rate by Job Readiness")
plt.xlabel("Job Readiness")
plt.ylabel("Placement Rate (%)")

# Step 7: Display labels
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.5,
        f"{height:.2f}%",
        ha="center"
    )

plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
