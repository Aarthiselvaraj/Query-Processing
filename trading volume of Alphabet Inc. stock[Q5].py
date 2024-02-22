import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('GOOG.csv')

# Convert the 'Date' column to datetime format with dayfirst=True
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Filter the DataFrame for the desired date range
start_date = '2023-01-01'
end_date = '2023-12-31'
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Create a bar plot of trading volume
plt.figure(figsize=(10, 6))
plt.bar(filtered_df['Date'], filtered_df['Volume'], color='skyblue')
plt.title('Trading Volume of Alphabet Inc. Stock')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
