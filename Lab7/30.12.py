import matplotlib.pyplot as plt
import pandas as pd

file = input()

# Read in CSV file as a dataframe
df = pd.read_csv(file)

# Insert a column to the dataframe as the last column
# Label the column "Size", which contains half the values in column "Gross Potential"
df['Size'] = df['Gross Potential'] / 2

# Output dataframe
print(df)

# Create scatter plot
plt.scatter(df['Capacity'], df['Gross Potential'], marker='x', color='orange', s=df['Size'])

# Add axis labels and title
plt.xlabel('Capacity', fontsize=10)
plt.ylabel('Gross Potential', fontsize=10)
plt.title('Gross Potential vs Capacity', fontsize=16)

# Add gridlines
plt.grid(linestyle='--')

# Save figure as output_fig.png
plt.savefig('output_fig.png')