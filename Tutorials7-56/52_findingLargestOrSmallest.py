# The below trick is applicable to your custom Classes,
# Objects as well as complex data structures such as JSON
import heapq

grades = [32, 43, 654, 34, 132, 66, 99, 532]

# The 3 largest values in a list
print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'GOOG', 'price': 520.54},
    {'ticker': 'FB', 'price': 76.45},
    {'ticker': 'YHOO', 'price': 39.28},
    {'ticker': 'AMZN', 'price': 306.21},
    {'ticker': 'AAPL', 'price': 99.76}
]

# The two cheapest stocks
print(heapq.nsmallest(2, stocks, key=lambda stock:stock['price']))
