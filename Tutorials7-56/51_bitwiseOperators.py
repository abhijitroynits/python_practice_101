#  Binary AND
a = 50     # -> 110010
b = 25     # -> 011001

c = a & b  # -> 010000
print('50 AND 25 in decimal =', c)
print('50 AND 25 in binary =', bin(c).replace("0b", ""))

#  Binary OR
a = 50     # -> 110010
b = 25     # -> 011001

c = a | b  # -> 111011
print('50 OR 25 in decimal =', c)
print('50 OR 25 in binary =', bin(c).replace("0b", ""))

# Binary RIGHT SHIFT
x = 240      # -> 11110000
y = x >> 2   # -> 00111100
print('x >> 2 in decimal = ', y)
print('x >> 2 in binary = ', bin(y).replace("0b", ""))

# Binary LEFT SHIFT
x = 240      # -> 11110000
y = x << 2   # -> 11000000
print('x << 2 in decimal = ', y)
print('x << 2 in binary = ', bin(y).replace("0b", ""))
