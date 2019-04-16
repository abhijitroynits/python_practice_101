# Using range(), it's possible to loop without a list

for x in range(4):
    print('$' * x)

print()
for x in range(5):
    print("hello", end='..')

print()
for x in range(3,7):
    print(x, end='\t')

print()
for x in range(1,10,2):
    print(x, end='\t\t')

print('\n')
# A while loop runs as long as the condition is true
testVariable = 5

while testVariable < 10:
    print('testVariable=', testVariable)
    testVariable +=1