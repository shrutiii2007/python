import matplotlib.pyplot as plt

# Data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 2, 3, 5, 6, 7, 8, 4, 9, 10, 1]

exam_scores = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
               42, 48, 58, 62, 68, 72, 52, 78, 82, 38]

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(hours_studied, exam_scores)

# Labels and title
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.title("Relationship Between Hours Studied and Exam Scores")

# Show grid
plt.grid(True)

# Display plot
plt.show()


