import pandas as pd

df = pd.read_csv("A3/employees.csv")

print("Shape of DataFrame:")
print(df.shape)

print("\nSummary of DataFrame:")
df.info()

print("\nDescriptive Statistics:")
print(df.describe())

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 3 rows:")
print(df.tail(3))\


average_salary = df["Salary"].mean()

print("Average Salary:", average_salary)

total_bonus = df["Bonus"].sum()

print("Total Bonus:", total_bonus)

youngest_age = df["Age"].min()

print("Youngest Employee Age:", youngest_age)

highest_rating = df["Rating"].max()

print("Highest Performance Rating:", highest_rating)


df_sorted_by_salary = df.sort_values(by="Salary", ascending=False)
print("\nDataFrame sorted by Salary (Descending):")
print(df_sorted_by_salary)

def categorize_rating(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

df["Performance"] = df["Rating"].apply(categorize_rating)
print(df[["Name", "Rating", "Performance"]])

print(df.isnull().sum())

df.rename(columns={"Employee ID": "ID"}, inplace=True)


experience_more_than_5_years = df[df["Years_of_Experience"] > 5]
print("\nEmployees with more than 5 years of experience:")
print(experience_more_than_5_years)

it_employees = df[df["Department"] == "IT"]
print("\nEmployees in IT Department:")
print(it_employees)


df["Tax"] = df["Salary"] * 0.10
print("\nDataFrame with Tax column:")
print(df)

df.to_csv("A3/employees_updated.csv", index=False)
print("\nUpdated DataFrame saved to 'employees_updated.csv'")