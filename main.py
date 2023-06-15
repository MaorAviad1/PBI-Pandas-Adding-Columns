import pandas as pd
from datetime import datetime

# Assuming df is your DataFrame and 'date' is your date column
df['date'] = pd.to_datetime(df['date'])

df.sort_values('date', inplace=True)

# Assuming 'sales', 'profit', 'quantity' are your relevant columns
for col in ['sales', 'profit', 'quantity']:
    # Calculate YoY (Year-over-Year) changes
    df['YoY_' + col] = df[col].pct_change(12) * 100  # Change to percent

    # Calculate YTD (Year-to-Date) sums
    df['YTD_' + col] = df[df['date'].dt.year == datetime.now().year][col].cumsum()

df.to_csv('new_data.csv', index=False)  # Save to a new CSV file
