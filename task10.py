import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

# Load the data from a CSV file
# Assuming the CSV file is named 'stock_data.csv'
data = pd.read_csv('/home/pi/ee347/lab-4-advanced-python-group-15/task9.csv', parse_dates=['Date'], dayfirst=True)

# Define colors for each stock
colors = {
    'META': 'blue',
    'AAPL': 'grey',
    'AMZN': 'black',
    'NFLX': 'red',
    'NVDA': 'green',
    'GOOGL': 'orange'
}

# Calculate percentage changes for legend
initial_prices = {col: data[col].iloc[0] for col in data.columns if col != 'Date'}
percentage_changes = {col: f"+{(data[col].iloc[-1] - initial) / initial * 100:.2f}%" for col, initial in initial_prices.items()}

# Plotting
plt.figure(figsize=(14, 7))
for stock in data.columns:
    if stock != 'Date':  # Skip the 'Date' column for plotting
        plt.plot(data['Date'], data[stock], label=f"{stock} {percentage_changes[stock]}", color=colors[stock])

# Title and labels
plt.title('FAANG Performance')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.grid()

# Add legend with frame
plt.legend(loc='upper left', frameon=True)

# Show the plot
plt.tight_layout()
plt.show()
