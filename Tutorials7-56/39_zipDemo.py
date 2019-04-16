# The zip() function is used to merge two or
# more equi-sized lists to create a list of tuples

first_names = ['Mark', 'Elon', 'Satya']
last_names = ['Zuckerberg', 'Musk', 'Nadella']
full_names = zip(first_names, last_names)

for a, b in full_names:
    print(a, b)

print()

# prints [] ; zip() doesn't create a persistent data structure
print(list(full_names))

