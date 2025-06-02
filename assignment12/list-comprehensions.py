# list-comprehensions.py

import pandas as pd

# Task 3: List Comprehensions Practice

# Read the CSV file into a DataFrame
df = pd.read_csv("../csv/employees.csv")

# List comprehension to create a list of full names
# Each row in df.iterrows() is a tuple: (index, row)
full_names = [row['first_name'] + " " + row['last_name'] for _, row in df.iterrows()]

# Print the full names list
print("All Employee Names:")
print(full_names)

#  List comprehension to filter names containing the letter 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]

# Print the filtered list
print("\nNames Containing the Letter 'e':")
print(names_with_e)
