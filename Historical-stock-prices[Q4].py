import pandas as pd
import matplotlib.pyplot as plt

# Load the stock price data from a CSV file (or any other source)
# Replace 'stock_prices.csv' with the path to your CSV file containing the stock price data
df = pd.read_csv('GOOG.csv')  # Assuming you have a CSV file with the required data

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)  # Specify dayfirst=True

# Define the start and end dates
start_date = '2023-01-01'
end_date = '2024-01-01'

# Filter the data between the specified dates
filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Date'], filtered_data['Close'], marker='o', linestyle='-')
plt.title('Historical Stock Prices of Alphabet Inc. between {} and {}'.format(start_date, end_date))
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
