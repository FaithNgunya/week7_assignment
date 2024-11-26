import pandas as pd

file_path = r"C:\Users\Davis\Desktop\datasets\gym_members_exercise_tracking.csv"
# Load the dataset into a DataFrame
df = pd.read_csv(file_path)


print(df.head())


numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())


object_cols = df.select_dtypes(include=['object']).columns
df[object_cols] = df[object_cols].fillna(df[object_cols].mode().iloc[0])


print(df)
