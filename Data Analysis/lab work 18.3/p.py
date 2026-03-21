
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class LibraryDashboard:

    def __init__(self):
        self.df = None

    def load_data(self, file_path):
        if not file_path.endswith(".csv"):
            raise ValueError("Only CSV files are allowed")

        self.df = pd.read_csv(file_path)
        self.df["Date"] = pd.to_datetime(self.df["Date"])
        self.df.dropna(inplace=True)

        print("Data loaded successfully")
        print(self.df.head())

    def calculate_statistics(self):
        most_borrowed = self.df["Book Title"].value_counts().idxmax()

        durations = np.array(self.df["Borrowing Duration (Days)"])
        avg_duration = np.mean(durations)
        std_duration = np.std(durations)

        busiest_day = self.df["Date"].dt.day_name().value_counts().idxmax()

        print("\n--- Statistics ---")
        print("Most Borrowed Book:", most_borrowed)
        print("Average Borrowing Duration:", round(avg_duration, 2))
        print("Borrow Duration Std Dev:", round(std_duration, 2))
        print("Busiest Day:", busiest_day)

    def filter_transactions(self, genre=None):
        if genre:
            return self.df[self.df["Genre"] == genre]
        return self.df

    def generate_report(self):
        print("\n--- Library Report ---")
        print("Total Transactions:", len(self.df))
        print("Unique Users:", self.df["User ID"].nunique())
        print("Popular Genre:", self.df["Genre"].value_counts().idxmax())

    def visualize(self):
        # Bar Chart
        self.df["Book Title"].value_counts().head(5).plot(kind="bar")
        plt.title("Top 5 Most Borrowed Books")
        plt.show()

        # Line Chart
        monthly = self.df.groupby(self.df["Date"].dt.to_period("M")).size()
        monthly.plot()
        plt.title("Monthly Borrowing Trend")
        plt.show()

        # Pie Chart
        self.df["Genre"].value_counts().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Genre Distribution")
        plt.ylabel("")
        plt.show()

        # Heatmap
        self.df["Day"] = self.df["Date"].dt.day_name()
        heatmap_data = pd.crosstab(self.df["Day"], self.df["Genre"])
        sns.heatmap(heatmap_data, annot=True, fmt="d")
        plt.title("Borrowing Activity Heatmap")
        plt.show()


if __name__ == "__main__":
    dashboard = LibraryDashboard()
    dashboard.load_data("library_transactions.csv")
    dashboard.calculate_statistics()
    dashboard.generate_report()
    dashboard.visualize()
