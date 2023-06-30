import numpy as np

# Read two sets of exam scores of five students from user input
exam1 = np.array(input().split(), dtype=np.float64)
exam2 = np.array(input().split(), dtype=np.float64)

# Compute the average scores for each of the five students
average_scores = (exam1 + exam2) / 2

# Output the average scores
print("Average scores:", average_scores)

# Count the number of average scores that are >= 80
num_above_80 = np.count_nonzero(average_scores >= 80)

# Output the count
print("Number of students who received 80 and above:", num_above_80)