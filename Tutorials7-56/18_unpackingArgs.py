# This technique is useful when we are passing the items of a collection
# as arguments to a function


def health_calculator(age, apples_eaten_a_week, cigs_smoked_a_week):
    answer = (100 - age) + (apples_eaten_a_week * 3.5) - (cigs_smoked_a_week * 2)
    print('Health Rating: ' + str(answer))


your_data = [27, 20, 5]
health_calculator(your_data[0], your_data[1], your_data[2])

# Unpacking the argument list
health_calculator(*your_data)

