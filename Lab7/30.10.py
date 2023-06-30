import pandas as pd

file_name = input()

# Read in file_name as a dataframe
df = pd.read_csv(file_name, sep='\t')

# Output rows by descending Final scores
df_sorted = df.sort_values(by='Final', ascending=False)
print(df_sorted.to_string())

print("\nMax Scores:")
# Output the max scores of each assignment
max_scores = df.max(numeric_only=True)
print(max_scores.to_string())

print("\nMedian Scores:")
# Output the median scores of each assignment
median_scores = df.median(numeric_only=True)
print(median_scores.to_string())

print("\nAverage Scores:")
# Output the average scores of each assignment
average_scores = df.mean(numeric_only=True)
print(average_scores.to_string())

print("\nStandard Deviation:")
# Output the standard deviation of each assignment
std_dev_scores = df.std(numeric_only=True)
print(std_dev_scores.to_string())