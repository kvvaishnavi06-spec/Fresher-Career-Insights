
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Count individual skills for each student
df["Skills_Count"] = (
    df["skills"]
    .fillna("")
    .apply(lambda x: len([s.strip() for s in x.split(";") if s.strip()]))
)

# Categorize skill count
df["Skills_Group"] = pd.cut(
    df["Skills_Count"],
    bins=[-1, 2, 4, 6, 100],
    labels=["1-2 Skills", "3-4 Skills", "5-6 Skills", "7+ Skills"]
)

# Identify placed students
df["is_placed"] = df["placement_status"].eq("Placed")

# ----------------------------------------
# ANALYSIS
# ----------------------------------------

analysis = df.groupby(
    ["internship_experience", "Skills_Group"],
    observed=False
).agg(
    Total_Students=("student_id", "nunique"),
    Placed_Students=("is_placed", "sum")
)

# Calculate placement rate
analysis["Placement_Rate_%"] = (
    analysis["Placed_Students"] / analysis["Total_Students"] * 100
).round(2)

# Print full analysis
print("\nPlacement Rate by Internship Experience and Skills")
print("=" * 70)
print(analysis.to_string())

# ----------------------------------------
# CHART 1 - PLACEMENT RATE COMPARISON
# ----------------------------------------

chart_data = analysis["Placement_Rate_%"].unstack("internship_experience")

# Remove empty skill categories
chart_data = chart_data.dropna(how="all")

chart_data.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Placement Rate: Internship Experience vs Skills Count")
plt.xlabel("Skills Group")
plt.ylabel("Placement Rate (%)")
plt.xticks(rotation=0)
plt.legend(title="Internship Experience")

plt.tight_layout()
plt.show()

# ----------------------------------------
# CHART 2 - STUDENT COUNT
# ----------------------------------------

count_data = analysis["Total_Students"].unstack("internship_experience")

count_data = count_data.dropna(how="all")

count_data.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Student Count by Internship Experience and Skills")
plt.xlabel("Skills Group")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.legend(title="Internship Experience")

plt.tight_layout()
plt.show()

# ----------------------------------------
# HIGHEST PLACEMENT RATE
# ----------------------------------------

valid_analysis = analysis.dropna(subset=["Placement_Rate_%"])

if not valid_analysis.empty:
    highest = valid_analysis["Placement_Rate_%"].idxmax()

    print("\nHighest Placement Rate Combination")
    print("-" * 50)
    print("Internship:", highest[0])
    print("Skills Group:", highest[1])
    print("Placement Rate:", valid_analysis.loc[highest, "Placement_Rate_%"], "%")
