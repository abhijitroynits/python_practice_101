# The map() function is used to apply some
# function on each item of a list

income = [10, 30, 75]
print('starting income =', income)


def double_income(dollars):
    return dollars * 2


revised_income = list(map(double_income, income))
print('revised_income =', revised_income)
