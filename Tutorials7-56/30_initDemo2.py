class Enemy:

    def __init__(self, e):
        self.energy = e

    def get_energy(self):
        return self.energy


jason = Enemy(100)
print('Jason\'s Initial energy: ', jason.get_energy())

sarah = Enemy(120)
print('Sarah\'s Initial energy: ', sarah.get_energy())

