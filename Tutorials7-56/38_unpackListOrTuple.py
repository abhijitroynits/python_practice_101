# This demo deals with unpacking a list and a tuple

data_items = ['December 25, 2016', 'Milk', 67.50]
date, product, cost = data_items  # Unpacking the list
print(date)


# Unpacking using * notation


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([1, 2, 4, 6, 8, 10, 12, 100])
drop_first_last([0, 2, 4, 10])
