# comments are notes for developers including yourself
# comments are ignored by the Runtime Environment

#  A docstring can span over a few lines.
#  Docstrings are written within triple quotes.
#  '''
#      line 1
#      line 2
#      line 3
#  '''

# The break statement stops your loop based on certain condition

magicNumber = 12

for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number.")
        break
    else:
        print(n)


# Find all multiples of 4 less than or equal to 100.
print()
for n in range(101):
    if (n % 4) == 0:
        print(n, end=' ')
