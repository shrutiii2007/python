import pandas as pd

df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue', 'Green', 'Red']
})

df['Color'] = df['Color'].astype('category')

print(df)
print(df.dtypes)


#task :- 2

print("task 2")

print("Unique categories:", df['Color'].nunique())
print(df['Color'].value_counts())


#task 3

print("task 3")

df['Size'] = ['Small', 'Medium', 'Large', 'Small', 'Large', 'Medium', 'Small']

df['Size'] = pd.Categorical(
    df['Size'],
    categories=['Small', 'Medium', 'Large'],
    ordered=True
)

sorted_df = df.sort_values('Size')
print(sorted_df)


#task 4

print("task :- 4")

df['Size'] = df['Size'].cat.rename_categories({
    'Small': 'S',
    'Medium': 'M',
    'Large': 'L'
})

print(df)

# Challenge

print("Challenge")

import matplotlib.pyplot as plt

size_counts = df['Size'].value_counts().sort_index()

plt.figure()
plt.bar(size_counts.index, size_counts.values)
plt.xlabel('Size')
plt.ylabel('Count')
plt.title('Count of Each Size Category')
plt.show()




