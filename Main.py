import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset using pandas read_csv()
df = pd.read_csv('Employee_Data.csv')

# Display the first five rows
print("First five rows of the dataset:")
print(df.head())

# Get the shape of the data
print("\nDataset shape:")
print(df.shape)

# Descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())


# Selecting a column for visualization
selected_column = "Age"

# Plotting a histogram
plt.figure(figsize=(10, 6))
plt.hist(df[selected_column], bins=30, color='skyblue', edgecolor='black')
plt.title(f'Histogram of {selected_column}')
plt.xlabel(selected_column)
plt.ylabel('Frequency')
plt.show()
