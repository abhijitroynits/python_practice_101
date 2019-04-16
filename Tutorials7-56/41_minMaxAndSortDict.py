import pprint

stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

# Sorting by the stock prices ;
# the first arg of zip() is the stock prices
print('\nMinimum stock price :', min(zip(stocks.values(), stocks.keys())))

# Similarly max stock price
print('Maximum stock price :', max(zip(stocks.values(), stocks.keys())))

# Sort ascending by price
print('\nSorted ascending by price: ')
pprint.pprint(sorted(zip(stocks.values(), stocks.keys())))

# Sort ascending by tickers(i.e., alphabetical sort)
print('\nSorted ascending by tickers: ')
pprint.pprint(sorted(zip(stocks.keys(), stocks.values())))
