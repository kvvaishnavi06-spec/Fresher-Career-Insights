
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/chennai_fresher_students_cleaned.csv")

# Remove missing training requirements
training_df = df.dropna(subset=["training_required"]).copy()

# Count training requirements by stream
analysis = (
    training_df.groupby(["stream", "training_required"])
    .size()
    .reset_index(name="Student_Count")
)

# Calculate total students with training data in each stream
stream_totals = training_df.groupby("stream")["student_id"].nunique()

# Calculate percentage
analysis["Percentage"] = analysis.apply(
    lambda row: round(
        row["Student_Count"] / stream_totals[row["stream"]] * 100, 2
    ),
    axis=1
)

# ----------------------------------------
# PRINT TRAINING REQUIREMENTS BY STREAM
# ----------------------------------------

streams = sorted(analysis["stream"].unique())

print("\nSkill Gap Analysis by Degree Stream")
print("=" * 60)

for stream in streams:

    stream_data = (
        analysis[analysis["stream"] == stream]
        .sort_values("Student_Count", ascending=False)
    )

    print(f"\n{stream}")
    print("-" * 45)
    print(stream_data[["training_required", "Student_Count", "Percentage"]].to_string(index=False))

    # Identify top training requirement
    top_training = stream_data.iloc[0]

    print(
        f"\nTop Training Need: {top_training['training_required']} "
        f"({top_training['Student_Count']} students, "
        f"{top_training['Percentage']}%)"
    )

# ----------------------------------------
# CREATE ONE CHART FOR EACH STREAM
# ----------------------------------------

for stream in streams:

    stream_data = (
        analysis[analysis["stream"] == stream]
        .sort_values("Student_Count", ascending=True)
    )

    plt.figure(figsize=(9, 5))

    bars = plt.barh(
        stream_data["training_required"],
        stream_data["Student_Count"]
    )

    plt.title(f"Training Requirements - {stream}")
    plt.xlabel("Number of Students")
    plt.ylabel("Training Required")

    # Add values to bars
    for bar in bars:
        width = bar.get_width()
        plt.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            f" {int(width)}",
            va="center"
        )

    plt.tight_layout()
    plt.show()

# ----------------------------------------
# OVERALL TOP TRAINING NEED
# ----------------------------------------

overall = (
    training_df["training_required"]
    .value_counts()
)

print("\nOverall Training Requirements")
print("=" * 45)
print(overall.to_string())
