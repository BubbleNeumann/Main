# TODO - fix player interactive mode: nice output statistic info
# TODO - add alert "Wrong input!" and ability to reenter the command
# TODO - class "Location"
# TODO - start shop location

from random import randint


def main():
    print("All your progress will be lost if you stop the program.\n")
    welcome()
    hero = Hero()
    dragon = Dragon()
    print(info)

    level = Level(dragon)
    level.fight(hero, dragon)

    waiting()


def sep():
    print('-----------------------------------------')


def waiting():
    wait = input("press enter to continue\n")


def welcome():
    title = str(input("Show introduction titles? [Y/N] - "))
    sep()
    if title == 'Y' or title == 'y':
        print("\nWelcome to Great Kingdom, brave knight!\n"
              "It's lend full of dangers, magic creatures and treasures.\n"
              "The Dark Master appropriated our north lands.\n"
              "King Arthur called you and asked you to kill him.\n"
              "Your goal is to get to north lands and destroy Dark Magic at Great Kingdom.\n"
              "Let's hit the road!\n")
        waiting()


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

    def __init__(self, armor=False, wallet=100,):
        super().__init__(Hero.default_health, Hero.attack_force,
                         Hero.default_stamina, Hero.shield)
        self.armor = armor
        self.wallet = wallet

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

    def intro(self):
        """dragon description"""
        print("")

    def stamina_refill(self):
        if self.stamina < Dragon.default_stamina:
            self.stamina = Dragon.default_stamina

    def fire_attack(self, other):
        """Special Dragon's move which causes more damage then usual attack."""


class Level:

    def __init__(self, enemy):
        self.enemy = enemy

    @staticmethod
    def echo_health(self, enemy):
        out = ''
        for i in range(enemy.health):
            out += '='
        while len(out) < enemy.default_health:
            out += '-'
        return out

    def what_to_do(self, other):
        """ The enemy analyses Hero's move, his stamina and health.
            Then decides should he attack or not.
            Possible action: fire attack, usual attack, rise a shield"""

    def fight(self, hero, enemy):
        sep()
        print('Get ready!\nFight starts!\n')
        while enemy.health > 0 and hero.health > 0:
            print("Dragon's health:", self.echo_health(self, enemy), "(", enemy.health, ')',
                  "\nHero's health/stamina:", hero.health, '/', hero.stamina, "\n")
            hero.keyboard_inp(enemy)
            if enemy.health > 0:
                enemy.attack(hero)
            hero.stamina_refill()
            enemy.stamina_refill()

        if enemy.health <= 0:
            print('\nYour Hero won!')
        else:
            print('\nYour Hero died.')
        sep()


class Location:
    """List of locations:
        1. Store (start point)
        2. Field
        3. The oak forest
        N. Final location (final boss)"""


info = ['[A] - to attack', '[S] - to rise a shield',
        '[DS] - to deactivate a shield']

location_list = ['store', 'field', 'forest']

main()
