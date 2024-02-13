import pandas as pd
import numpy as np

# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.

## YOUR CODE HERE ##
morg_df = pd.read_csv("/Users/adhdtreamentii/Desktop/UChicago 2024/UChicago Winter 24/MACSS-30100/Q0/Programming/tt7-volt-1/data/morg_d07_strings.csv", index_col="h_id")


# TASKS 2-6
# For each of the tasks, print the value requested in the task.

## YOUR CODE HERE ##
task2 = morg_df["age"]

task3 = morg_df.loc["1_2_2"]

task4 = morg_df.iloc[:4]

# Check missing
missing1 = any(morg_df.loc[:, "hours_worked_per_week"].isna())
missing2 = any(morg_df.loc[:, "age"].isna())


#task5

missing_value_columns = {}

for column in morg_df.columns:
    if morg_df[column].isna().any():
        missing_value_columns[column] = 0

print(missing_value_columns)


#task6
morg_df.fillna(missing_value_columns, inplace=True)


### Task 7
### convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]

                                                                 
## YOUR CODE HERE ##
morg_df.loc[:, "gender"] = morg_df.loc[:, "gender"].astype("category")
morg_df.loc[:, "race"] = morg_df.loc[:, "race"].astype("category")
morg_df.loc[:, "ethnicity"] = morg_df.loc[:, "ethnicity"].astype("category")
morg_df.loc[:, "employment_status"] = morg_df.loc[:, "employment_status"].astype("category")
      
# Example use of cut()
boundaries = range(16, 89, 8)
morg_df.loc[:, "age_bin"] = pd.cut(morg_df.loc[:, "age"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

### Task 8

## YOUR CODE HERE ##
print(morg_df.loc[:, "hours_worked_per_week"].min())
print(morg_df.loc[:, "hours_worked_per_week"].max())

hwpw_boundaries = range(0, 100, 11)
morg_df.loc[:, "hours_worked_per_week_bin"] = pd.cut(morg_df.loc[:, "hours_worked_per_week"],
                                                     bins = hwpw_boundaries,
                                                     labels = range(len(hwpw_boundaries)-1),
                                                    include_lowest=True, right=False)

print("Morg columns types after Task 8")
print(morg_df.dtypes)


### Tasks 9-13
#task 9
task_9_df = morg_df[morg_df['hours_worked_per_week'] >= 35]
print(task_9_df)

#task 10
task_10_df = morg_df[morg_df['employment_status'] != "Working"]  
print(task_10_df)

#task 11
task_11_df = morg_df[(morg_df['hours_worked_per_week'] >= 35) | (morg_df['earnings_per_week'] > 1000)]

#task 12
task_12_df = morg_df.loc[:,"race"].value_counts()
print(task_12_df[:5])

#task 13
task_13_df = morg_df.groupby("race").size().sort_index()
print(task_13_df)

### Task 14

students = pd.read_csv("/Users/adhdtreamentii/Desktop/UChicago 2024/UChicago Winter 24/MACSS-30100/Q0/Programming/tt7-volt-1/data/students.csv")
extended_grades = pd.read_csv("/Users/adhdtreamentii/Desktop/UChicago 2024/UChicago Winter 24/MACSS-30100/Q0/Programming/tt7-volt-1/data/extended_grades.csv")


# merge data
merged_df = pd.merge(students, extended_grades, on="UCID")

# regroup data
grade_counts = merged_df.groupby(['Major', 'Grade']).size()

# reset index
grade_counts_df = grade_counts.reset_index(name='Count')

print(grade_counts_df)
