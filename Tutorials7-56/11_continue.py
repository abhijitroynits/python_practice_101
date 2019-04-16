# A continue statement takes the control back to the loop.
# A continue statement skips all the lines that occur after it.

numbersTaken = [2, 5, 12, 13, 17]

print('Jersey numbers still available - \n')
for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)