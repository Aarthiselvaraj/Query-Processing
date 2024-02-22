import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
alphabet_stock_data = pd.read_csv('GOOG.csv')

# Convert the 'Date' column to datetime format with dayfirst=True
alphabet_stock_data['Date'] = pd.to_datetime(alphabet_stock_data['Date'], dayfirst=True)

# Filter the DataFrame for the desired date range
start_date = '2023-01-01'
end_date = '2023-12-31'
filtered_data = alphabet_stock_data[(alphabet_stock_data['Date'] >= start_date) & (alphabet_stock_data['Date'] <= end_date)]

# Create a scatter plot of trading volume and stock prices
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['Date'], filtered_data['Volume'], color='blue', label='Volume')
plt.scatter(filtered_data['Date'], filtered_data['Close'], color='red', label='Close Price')
plt.title('Trading Volume and Stock Prices of Alphabet Inc. Stock')
plt.xlabel('Date')
plt.ylabel('Volume/Close Price')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
