# Sorting custom objects by any attribute that you want
from operator import attrgetter


class User:
    # Method to instantiate the object
    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    # Method to print string representation of the object
    def __repr__(self):
        return self.name + " : " + str(self.user_id)

# List of User objects
users = [
    User('Bucky', 43),
    User('Sally', 5),
    User('Tuna', 61),
    User('Brian', 2),
    User('Joby', 77),
    User('Amanda', 9)
]

# Default order in which the objects are sorted
# They are sorted in the manner they've been created(listed)
print('\nDefault order of objects: ')
for user in users:
    print(user)

print()
print('\nSorting objects by name: ')
for user in sorted(users, key=attrgetter('name')):
    print(user)

print()
print('\nSorting objects by id: ')
for user in sorted(users, key=attrgetter('user_id')):
    print(user)