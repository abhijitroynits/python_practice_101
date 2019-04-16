# Let us create a few variables and functions
# The value of a variable depends on the order of function calls


def fun_a():
    print('fun_a() called; a = ', a)


def fun_b():
    a = 20 # local scope
    print('fun_b() called; a = ', a)


def fun_c():
    global a  # global scope
    a = -150
    print('fun_c() called; a = ', a)
    a = 88
    fun_d()


def fun_d():
    print('fun_d() called; a = ', a)


a = 102
fun_a()
fun_b()
fun_c()

