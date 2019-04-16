stocks = {
    'GOOG': 434,
    'AAPL': 325,
    'FB': 54,
    'AMZN': 623,
    'F': 32,
    'MSFT': 549
}

# By default, alphabetically lowest keys
# are displayed by
print('\nDefault minimum key= ', min(stocks))

# Sorting by the stock prices ;
# the first arg of zip() is the stock prices
print('Minimum stock price :', min(zip(stocks.values(), stocks.keys())))
