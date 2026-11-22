
import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

df["is_placed"] = df["placement_status"].eq("Placed")

total_students = df["student_id"].nunique()
placed_students = df.loc[df["is_placed"], "student_id"].nunique()
overall_rate = (placed_students / total_students) * 100

# ==========================================
# KPI SUMMARY
# ==========================================

print("\n" + "=" * 65)
print("          FINAL FRESHER CAREER INSIGHTS")
print("=" * 65)

print(f"Total Students       : {total_students}")
print(f"Placed Students     : {placed_students}")
print(f"Not Placed         : {total_students - placed_students}")
print(f"Overall Placement  : {overall_rate:.2f}%")

# ==========================================
# PLACEMENT BY STREAM
# ==========================================

stream_analysis = df.groupby("stream").agg(
    Total_Students=("student_id", "nunique"),
    Placed_Students=("is_placed", "sum")
)

stream_analysis["Placement_Rate_%"] = (
    stream_analysis["Placed_Students"]
    / stream_analysis["Total_Students"] * 100
).round(2)

print("\nPlacement Rate by Degree Stream")
print("-" * 65)
print(stream_analysis.sort_values(
    "Placement_Rate_%", ascending=False
).to_string())

# ==========================================
# PLACEMENT BY PREFERRED SECTOR
# ==========================================

sector_analysis = df.groupby("preferred_sector").agg(
    Total_Students=("student_id", "nunique"),
    Placed_Students=("is_placed", "sum")
)

sector_analysis["Placement_Rate_%"] = (
    sector_analysis["Placed_Students"]
    / sector_analysis["Total_Students"] * 100
).round(2)

print("\nPlacement Rate by Preferred Sector")
print("-" * 65)
print(sector_analysis.sort_values(
    "Placement_Rate_%", ascending=False
).to_string())

# ==========================================
# PLACEMENT BY JOB ROLE
# ==========================================

role_analysis = df.groupby("preferred_job_role").agg(
    Total_Students=("student_id", "nunique"),
    Placed_Students=("is_placed", "sum")
)

role_analysis["Placement_Rate_%"] = (
    role_analysis["Placed_Students"]
    / role_analysis["Total_Students"] * 100
).round(2)

top_roles = role_analysis.sort_values(
    "Placement_Rate_%", ascending=False
).head(5)

print("\nTop 5 Job Roles by Placement Rate")
print("-" * 65)
print(top_roles.to_string())

# ==========================================
# PLACEMENT STATUS
# ==========================================

status_counts = df["placement_status"].value_counts()

# ==========================================
# FINAL DASHBOARD
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(16, 11))

# Chart 1 - Placement Status
axes[0, 0].bar(
    status_counts.index,
    status_counts.values
)

axes[0, 0].set_title("Student Placement Status")
axes[0, 0].set_ylabel("Number of Students")
axes[0, 0].tick_params(axis="x", rotation=20)

# Chart 2 - Placement Rate by Stream
stream_sorted = stream_analysis.sort_values("Placement_Rate_%")

axes[0, 1].barh(
    stream_sorted.index,
    stream_sorted["Placement_Rate_%"]
)

axes[0, 1].set_title("Placement Rate by Degree Stream")
axes[0, 1].set_xlabel("Placement Rate (%)")

# Chart 3 - Placement Rate by Sector
sector_sorted = sector_analysis.sort_values("Placement_Rate_%")

axes[1, 0].bar(
    sector_sorted.index,
    sector_sorted["Placement_Rate_%"]
)

axes[1, 0].set_title("Placement Rate by Preferred Sector")
axes[1, 0].set_ylabel("Placement Rate (%)")
axes[1, 0].tick_params(axis="x", rotation=15)

# Chart 4 - Top 5 Job Roles
axes[1, 1].barh(
    top_roles.index,
    top_roles["Placement_Rate_%"]
)

axes[1, 1].set_title("Top 5 Job Roles by Placement Rate")
axes[1, 1].set_xlabel("Placement Rate (%)")
axes[1, 1].invert_yaxis()

# Main title
fig.suptitle(
    "Fresher Career Insights Dashboard",
    fontsize=18
)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# ==========================================
# SAVE DASHBOARD
# ==========================================

output_folder = "../Output"
os.makedirs(output_folder, exist_ok=True)

dashboard_path = os.path.join(
    output_folder,
    "46_final_career_insights_dashboard.png"
)

plt.savefig(dashboard_path, dpi=300, bbox_inches="tight")

print("\nDashboard saved successfully!")
print("File location:", dashboard_path)

plt.show()
