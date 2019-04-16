#  A class variable is shared by all the instances created from the class.
# An instance variable is unique for a given instance.


class Girl:

    gender = 'female'  # class variable

    def __init__(self, name):
        self.name = name   # instance variable

    def get_name(self):
        return self.name


firstGirl = Girl('Sandy')
print(firstGirl.gender)
print(firstGirl.get_name(),'\n')

secondGirl = Girl('Randy')
print(secondGirl.gender)
print(secondGirl.get_name())
