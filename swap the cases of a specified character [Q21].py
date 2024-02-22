import pandas as pd

# Sample DataFrame
data = {'CharacterColumn': ['Hello', 'World', 'Python', 'Pandas', 'DataFrames']}
df = pd.DataFrame(data)

# Specify the column to swap cases
column_name = 'CharacterColumn'

# Swap the cases of the specified column
df[column_name] = df[column_name].str.swapcase()

# Display the modified DataFrame
print("DataFrame with swapped cases:")
print(df)
