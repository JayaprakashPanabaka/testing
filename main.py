# Question 1: Install Pandas and Create Your First DataFrame
# Description: Install the Pandas library and create a simple DataFrame from a dictionary. 
# Print the DataFrame.

# Step 1: Install Pandas (Uncomment if not already installed)
# !pip install pandas

# Step 2: Import Pandas
import pandas as pd
import numpy as np

# Step 3: Create a DataFrame
data = {
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Step 4: Print the DataFrame

print(df)