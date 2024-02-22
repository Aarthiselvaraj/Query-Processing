import pandas as pd

# Sample DataFrame
data = {'Column1': ['apple', 'banana', 'orange', 'grape', 'watermelon']}
df = pd.DataFrame(data)


substring = 'orange'


index = df['Column1'].str.find(substring)


print("Index of '{}' in DataFrame column: {}".format(substring, index.tolist()))
