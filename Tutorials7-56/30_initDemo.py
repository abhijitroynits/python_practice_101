class Tuna:
    # Every time an object is created,
    # the __init()__ method is invoked by default

    def __init__(self):
        print('Tuna object instantiated')

    def swim(self):
        print('Tuna is swimming')


tuna = Tuna()
tuna.swim()
