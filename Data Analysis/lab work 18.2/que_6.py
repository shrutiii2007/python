import matplotlib.pyplot as plt

companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
market_share = [30, 25, 20, 15, 10]

plt.pie(
    market_share,
    labels=companies,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Market Share of Companies")
plt.savefig("market_share.png")
plt.show()
