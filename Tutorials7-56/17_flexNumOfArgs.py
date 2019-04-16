# This principle is applicable whenever
# the number of args to be passed isn't pre-decided
# The parameters are notated as 'args' for historical reasons;
# any other name can be used just fine


def add_numbers(*args):
    total = 0
    for i in args:
        total += i

    print("Sum of elements in " + str(args) + " = " + str(total))


add_numbers()
add_numbers(-5)
add_numbers(1, 2, 3, 4)
add_numbers(-3, -2, -1, 0, 1, 2, 3, 4)
