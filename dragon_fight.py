# TODO - fix player interactive mode: nice output statistic info
# TODO - add alert "Wrong input!" and ability to reenter the command
# TODO - class "Location"
# TODO - start shop location
# TODO - use_bomb def
# for commit message: was added store location, ability to buy and use bombs.

from random import randint


def main():
    print("All your progress will be lost if you stop the program.\n")
    welcome()
    # current_level = 0
    # current_location = 'store'
    hero = Hero()
    current_level = Level
    current_level.store(hero=hero)

    enemy = Dragon()
    print(info)

    level = Level(enemy)
    level.fight(hero, enemy)

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
              "Your goal is to get to north lands and destroy Dark Magic at Great Kingdom.\n\n"
              "The path will lead you to the goal.\n"
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

    def __init__(self, armor=False, wallet=100, bomb=0):
        super().__init__(Hero.default_health, Hero.attack_force,
                         Hero.default_stamina, Hero.shield)
        self.armor = armor
        self.wallet = wallet
        self.bomb = 0

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
        elif act == "B" or "b":
            self.use_bomb(other)

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

    def use_bomb(self, other):
        if self.bomb > 0:
            self.bomb -= 1
            other.health -= 10
        else:
            print("You haven't any bombs.")


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
        # self.current_level = current_level

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
        # current_location = Location(Location.location_list[current_level])
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
            # current_level += 1
        else:
            print('\nYour Hero died.')
        sep()

    def path(self):
        print('You went on the path.')

    @staticmethod
    def store(hero):
        print("You've come at local shop.\n"
              "King Arthur gave you come coins\n"
              "and now you can buy anything you need for your journey.\n")

        store_stock = "1. Bomb - 20 coins\n" \
                      "2. Resurrection cristal - 50 coins\n" \
                      "3. The armor - 100 coins\n"

        print(store_stock)
        print('To choose the item enter its serial number.\n'
              'To exit press enter.\n')

        inp = 1
        print('You have got', hero.wallet, 'coins.')
        while (inp == 1 or inp == 2 or inp == 3) and hero.wallet > 0:
            inp = int(input())
            if inp == 3 and hero.wallet >= 100:
                hero.armor = True
                hero.wallet -= 100
                print('You got the armor.')
            if inp == 2 and hero.wallet >= 50:
                hero.wallet -= 50
            if inp == 1 and hero.wallet >= 20:
                hero.bomb += 1
                hero.wallet -= 20
                print('You got the bomb.')

        print("You've left the store.\n")
        print("Now you're ready to go.")
        sep()


class Location:
    """List of locations:
        1. Store (start point)
        2. Field
        3. The oak forest
        N. Final location (final boss)"""
    def __init__(self, location_list):
        self.location_list = location_list

    location_list = ['store', 'field', 'forest']


info = ['[A] - to attack', '[S] - to rise a shield',
        '[DS] - to deactivate a shield', '[B] - to use a bomb']

main()
