# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

print("Load the CSV file print")

tips = pd.read_csv("tips.csv")

print("Display first 5 rows")

print(tips.head())

print("Display dataset information")

print(tips.info())

# -----------------------------------
# Distribution Plots
# -----------------------------------

# Histogram of total bill
sns.histplot(tips["total_bill"])
plt.title("Histogram of Total Bill")
plt.show()

# KDE plot of total bill
sns.kdeplot(tips["total_bill"], fill=True)
plt.title("KDE Plot of Total Bill")
plt.show()

# Histogram + KDE
sns.displot(tips["total_bill"], kde=True)
plt.show()

# -----------------------------------
# Categorical Plots
# -----------------------------------

# Boxplot: total bill by day
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Total Bill by Day")
plt.show()

# Violin plot: tip by gender
sns.violinplot(x="sex", y="tip", data=tips)
plt.title("Tip Amount by Gender")
plt.show()

# Strip plot: tip by smoker
sns.stripplot(x="smoker", y="tip", data=tips, jitter=True)
plt.title("Tips by Smoker Status")
plt.show()

# -----------------------------------
# Relational Plots
# -----------------------------------

# Scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Total Bill vs Tip")
plt.show()

# Scatter plot with extra info
sns.scatterplot(
    x="total_bill",
    y="tip",
    hue="smoker",
    style="sex",
    data=tips
)
plt.title("Total Bill vs Tip with Smoker and Gender")
plt.show()

# Line plot: average tip by day
sns.lineplot(x="day", y="tip", data=tips)
plt.title("Average Tip by Day")
plt.show()

# -----------------------------------
# Matrix Plot
# -----------------------------------

# Find correlation
corr = tips.corr(numeric_only=True)

# Heatmap
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------------
# Regression Plot
# -----------------------------------

# Regression plot
sns.regplot(x="total_bill", y="tip", data=tips)
plt.title("Regression between Total Bill and Tip")
plt.show()

# lmplot
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips)
plt.show()
