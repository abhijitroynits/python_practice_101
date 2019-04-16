# A lambda is essentially a small anonymous function


def fun1(x):
    return lambda n: n*7 - x


def fun2(n):
    y = lambda n: 2*n
    return y(n)


print('fun1(28)(2)=', fun1(28)(2))
print('fun2(15)=', fun2(15))
