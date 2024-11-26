import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for better visual appeal
sns.set(style="whitegrid")

# Load your dataset into the DataFrame
df = pd.read_csv("C:\\Users\\Davis\\Desktop\\datasets\\gym_members_exercise_tracking.csv")

# Check the dataset structure
print(df.head())
print(df.info())

# Create a figure and set of subplots (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Line chart: Trend of BMI by Age
axes[0, 0].plot(df['Age'], df['BMI'], label="BMI by Age", color='b', linewidth=2)
axes[0, 0].set_title('Line Chart: BMI by Age', fontsize=14)
axes[0, 0].set_xlabel('Age', fontsize=12)
axes[0, 0].set_ylabel('BMI', fontsize=12)
axes[0, 0].legend()

# Bar chart: Comparison of Avg_BPM by Gender
sns.barplot(x='Gender', y='Avg_BPM', data=df, ax=axes[0, 1], palette="Set2")
axes[0, 1].set_title('Bar Chart: Avg BPM by Gender', fontsize=14)
axes[0, 1].set_xlabel('Gender', fontsize=12)
axes[0, 1].set_ylabel('Average BPM', fontsize=12)

# Histogram: Distribution of Weight (kg)
axes[1, 0].hist(df['Weight (kg)'], bins=20, color='skyblue', edgecolor='black')
axes[1, 0].set_title('Histogram: Distribution of Weight', fontsize=14)
axes[1, 0].set_xlabel('Weight (kg)', fontsize=12)
axes[1, 0].set_ylabel('Frequency', fontsize=12)

# Scatter plot: Relationship between Weight and Max_BPM
axes[1, 1].scatter(df['Weight (kg)'], df['Max_BPM'], color='darkorange', alpha=0.7)
axes[1, 1].set_title('Scatter Plot: Weight vs Max BPM', fontsize=14)
axes[1, 1].set_xlabel('Weight (kg)', fontsize=12)
axes[1, 1].set_ylabel('Max BPM', fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the combined plots
plt.show()
