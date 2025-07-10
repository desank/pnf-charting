# config.py

# Replace "YOUR_API_KEY" with your actual Alpha Vantage API key
ALPHA_VANTAGE_API_KEY = "O2A3QY0576C6Y8GD"

# -- Chart Settings --
# The stock ticker symbol to chart (e.g., "AAPL" for Apple)
TICKER = "AAPL"

# -- PNF Settings --
# The size of each box in the P&F chart.
# This is the price movement required to draw a new X or O.
BOX_SIZE = 1.00

# The reversal amount. This is the number of boxes the price must move in the
# opposite direction to warrant a new column.
# A standard reversal is 3.
REVERSAL_AMOUNT = 3
