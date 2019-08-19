# TODO - fix player interactive mode: nice output statistic info
# TODO - add alert "Wrong input!" and ability to reenter the command
# TODO - welcome titles

from random import randint


def main():
    hero = Hero()
    dragon = Dragon()
    print(info)

    while dragon.health > 0 and hero.health > 0:
        print("Dragon's health:", dragon.health,
              "\nHero's health/stamina:", hero.health, '/', hero.stamina, "\n")
        hero.keyboard_inp(dragon)
        if dragon.health > 0:
            dragon.attack(hero)
        hero.stamina_refill()
        dragon.stamina_refill()

    if dragon.health <= 0:
        print('\nYour Hero won!')
    else:
        print('\nYour Hero died.')

    wait = input("press enter to exit")


class BattleUnit:
    def __init__(self, health, attack_force, stamina, shield):
        self.health = health
        self.attack_force = attack_force
        self.stamina = stamina
        self.shield = shield

    def attack(self, other):
        if self.stamina >= self.attack_force and not other.shield:
            other.health -= self.attack_force
            self.stamina -= self.attack_force

        elif self.stamina >= self.attack_force and other.shield:
            other.health -= self.attack_force // 2
            self.stamina -= self.attack_force

        elif self.stamina < self.attack_force:
            print('Your stamina level is too low.')


class Hero(BattleUnit):

    default_health = 10
    attack_force = 6
    default_stamina = 10
    shield = False

    def __init__(self):
        super().__init__(Hero.default_health, Hero.attack_force,
                         Hero.default_stamina, Hero.shield)

    def keyboard_inp(self, other):
        """Hero's move"""
        act = str(input())
        if act == "A" or act == "a":
            if self.stamina < 3:
                miss_probability = randint(0, 3)
            else:
                miss_probability = randint(0, 10)
            if miss_probability == 0:
                print("Your strike missed!")
            else:
                self.attack(other)
        elif act == "S" or act == "s":
            self.set_shield()
        elif act == "DS" or act == "ds":
            if self.shield:
                self.shield = False
            else:
                print('\nNothing to deactivate.')

    def stamina_refill(self):
        if self.shield:
            self.stamina += 2
        else:
            self.stamina += 6
        if self.stamina > 10:
            self.stamina = 10

    def set_shield(self):
        if not self.shield and self.stamina >= 3:
            self.shield = True
            self.stamina -= 3
            print("You've raised your shield.\n")
        elif not self.shield and self.stamina < 3:
            print('\nYour stamina level is too low to do it.')
        else:
            print('\nShield was already activated.')


class Dragon(BattleUnit):

    default_health = 15
    attack_force = 5
    default_stamina = 10
    shield = False

    def __init__(self):
        super().__init__(Dragon.default_health, Dragon.attack_force,
                         Dragon.default_stamina, Dragon.shield)

    def stamina_refill(self):
        if self.stamina < Dragon.default_stamina:
            self.stamina = Dragon.default_stamina

    def what_to_do(self, other):
        """ Dragon analyses Hero's move, his stamina and health.
            Then decides should he attack or not."""

    def fire_attack(self, other):
        """Special Dragon's move which causes more damage then usual attack."""


info = ['[A] - to attack', '[S] - to rise a shield',
        '[DS] - to deactivate a shield']
main()
