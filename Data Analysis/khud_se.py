import seaborn as sns
import matplotlib.pyplot as plt

# sample data
data = {
    "Category": ["A", "B", "C"],
    "Values": [10, 20, 15]
}

# bar plot
sns.barplot(x="Category", y="Values", data=data)
plt.show()
