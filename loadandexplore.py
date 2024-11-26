import pandas as pd

url = r"C:\Users\Davis\Desktop\datasets\gym_members_exercise_tracking.csv"

df = pd.read_csv(url)

# Display first few rows to inspect data
print(df.head())

# Explore the structure: Data types, missing values
print(df.info())
print(df.isnull().sum())
