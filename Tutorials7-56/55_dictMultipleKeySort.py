from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Roberts'},
    {'fname': 'Bernie', 'lname': 'Zunks'},
    {'fname': 'Jenna', 'lname': 'Hayes'},
    {'fname': 'Sally', 'lname': 'Jones'},
    {'fname': 'Amanda', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Williams'},
    {'fname': 'Dean', 'lname': 'Hayes'},
    {'fname': 'Bernie', 'lname': 'Barbie'},
    {'fname': 'Tom', 'lname': 'Jones'}
]

# Sort by first name ; the lname's aren't
# in true alphabetical order though
print('\nSorting by first name(alone)')
for x in sorted(users, key=itemgetter('fname')):
    print(x)

# Sorting by first name, followed by each subroup(last name)
print('\nSorting by first name, and then by last name -')
for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)

