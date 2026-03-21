import pandas as pd

fruits = pd.DataFrame({
    "Region": ["North", "North", "South", "South", "East", "East"],
    "Fruit": ["Apple", "Banana", "Apple", "Banana", "Apple", "Banana"],
    "Price": [120, 60, 110, 55, 130, 65]
})

print(fruits)

print("---------------------------------------")

pivot_fruits = pd.pivot_table(
    fruits,
    index="Region",
    columns="Fruit",
    values="Price",
    aggfunc="mean"
)

print(pivot_fruits)



