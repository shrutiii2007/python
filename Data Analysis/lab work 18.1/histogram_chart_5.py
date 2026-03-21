import matplotlib.pyplot as plt
import numpy as np

# Generate ages of 100 people (random data)
np.random.seed(42)  # for reproducibility
ages = np.random.randint(1, 80, 100)

# Create histogram
plt.figure(figsize=(8, 5))
plt.hist(ages, bins=10)

# Labels and title
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution of 100 People")

# Show plot
plt.show()


