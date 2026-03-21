# Task 1: Sorting and Filtering Data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#task:-1.1
print("LOAD A DATASET:-")
df = pd.read_csv("sample_data.csv")
print(df.head())
print("----------------------------------------------------------")

#task:-1.2

print("SORT IN DESCENDING ORDER:-")
df_sorted = df.sort_values(by='age',ascending=False)
print(df_sorted.head())
print("----------------------------------------------------------")

#task:-1.3

print("FILTER ROWS WHERE AGE > 30:-")
filtered_df = df[df["age"] > 30]

print(filtered_df.head())
print("----------------------------------------------------------")

# Task 2: Aggregation and Grouping

#task:-2.1

print("GROUP THE DATASET:-")
grouped_df = df.groupby("gender")
print("=== Female Group ===")
print(grouped_df.get_group("Female"))
print("\n=== Male Group ===")
print(grouped_df.get_group("Male"))
print("----------------------------------------------------------")

#task:-2.2

print("CALCULATE AGGREGATE STATISTICS:-")

agg_stats = grouped_df.agg({
    'age': 'mean',
    'salary': 'sum',
    'fare': 'sum',
    'total_order_value': 'sum',
    'sales': ['mean','sum','count']  
})
print(agg_stats)
print("----------------------------------------------------------")

#task:- 2.3

print("GROUP WITH HIGHEST AVG VALUE:-")
best_group = df.groupby("gender")["sales"].mean().idxmax()
best_value = df.groupby("gender")["sales"].mean().max()

print("Group with Highest Average Sales:", best_group, "(", best_value, ")")
print("----------------------------------------------------------")

# Task 3: Data Visualization

#task 3.1

print("CREATING BAR CHART FOR GROUP COUNTS:")
group_counts = df['gender'].value_counts()
# Bar chart
plt.figure(figsize=(6,4))
plt.bar(group_counts.index, group_counts.values, color=['skyblue','pink'])
plt.title("Total Counts by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
print("----------------------------------------------------------")

#task 3.2
print("PIE CHART FOR SHOW THE PROPORTION OF CAT VAR:-")
cat_col = 'gender'  # Replace with any other categorical column if needed

# Count occurrences of each category
cat_counts = df[cat_col].value_counts()
print("Counts for each category:")
print(cat_counts)

# Create the pie chart
plt.figure(figsize=(6,6))
plt.pie(
    cat_counts,               
    labels=cat_counts.index,   
    autopct='%1.1f%%',        
    startangle=90,             
    colors=['lightblue','lightpink'], 
    explode=[0.05]*len(cat_counts)  
)
plt.title(f"Proportion of {cat_col.capitalize()}")
plt.show()

print("----------------------------------------------------------")

#task 3.3

print("SCATTER PLOT FOR 2 NUM COL(Age vs fare):-")
x_col = 'age'   
y_col = 'fare'  

plt.figure(figsize=(6,4))
plt.scatter(df[x_col], df[y_col], color='purple', alpha=0.6)
plt.title(f"{x_col.capitalize()} vs {y_col.capitalize()}")
plt.xlabel(x_col.capitalize())
plt.ylabel(y_col.capitalize())
plt.grid(True)
plt.show()

print("----------------------------------------------------------")

