class Parent:

    def __init__(self, last_name):
        self.last_name = last_name

    def talk(self):
        print(', you owe me.\n')


class Child(Parent):
    def __init__(self, first_name, parent):
        self.first_name = first_name
        self.parent = parent

    def get_full_name(self):
        return self.first_name + ' ' + self.parent.last_name

    def talk(self):  # Method overriding
        self.parent.talk()
        print('Let us settle it...the quickest in history!')


child_first = Child('Brian', Parent("O'Reilly"))
print(child_first.get_full_name(), end='')
child_first.talk()

