# A for loop can be used to iterate over a collection

foods = ['bacon', 'tuna', 'ham', 'sausages', 'beef']

for f in foods:
    print("Food item," + f + ",has " + str(len(f)) + " characters. ")

# Food excluding sausages and beef
print()
for f in foods[:3]:
    print("Food item," + f + ",has " + str(len(f)) + " characters. ")
