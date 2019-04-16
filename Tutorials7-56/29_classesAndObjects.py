# Class definition


class Enemy:
    life = 5

    def attack(self):
        print('ouch!')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('Player is dead')
        else:
            print(str(self.life) + ' life left')


enemy1 = Enemy()
print('Initial life value for enemy1 = ' + str(enemy1.life))

enemy1.attack()
print('\nLifecheck for enemy1: ')
enemy1.checkLife()

enemy1.attack()
print('\nLifecheck for enemy1: ')
enemy1.checkLife()

enemy2 = Enemy()
print('\nInitial life value for enemy2 = ' + str(enemy2.life))

enemy2.attack()
enemy2.attack()
enemy2.attack()
print('\nLifecheck for enemy2: ')
enemy2.checkLife()

