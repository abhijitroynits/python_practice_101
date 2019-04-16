# Multiple Inheritance provides inheriting from more than one class


class Mario():
    def move(self):
        print('Mario is moving...')


class Diet():
    def eat(self):
        print('Mario eats mushroom')


class Life(Mario, Diet):
    pass


mario_life = Life()
mario_life.move()
mario_life.eat()

