# TODO - add miss strikes
# TODO - fix player interactive mode
# TODO - add alert "Wrong input!" and ability to reenter the command


def main():
    hero = Hero()
    dragon = Dragon()
    print(info)

    while dragon.health > 0 and hero.health > 0:
        hero.keyboard_inp(dragon)
        dragon.attack(hero)
        print("Dragon's health/stamina:", dragon.health, '/', dragon.stamina,
              "\nHero's health/stamina:", hero.health, '/', hero.stamina)
        hero.stamina_refill()
        dragon.stamina_refill()

    if dragon.health <= 0:
        print('Your hero won!')
    else:
        print('Your hero died.')

    wait = input()


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

    default_health = 100
    attack_force = 6
    default_stammina = 15
    shield = False

    def __init__(self):
        super().__init__(Hero.default_health, Hero.attack_force,
                         Hero.default_stammina, Hero.shield)

    def keyboard_inp(self, other):
        """Hero's move"""
        act = str(input())
        if act == "A":
            self.attack(other)
        elif act == "S":
            if not self.shield:
                self.shield = True
                self.stamina -= 3
            else:
                print('\nShield was already activated.')
        elif act == "DS":
            if self.shield:
                self.shield = False
            else:
                print('\nNothing to deactivate.')

    def stamina_refill(self):
        if self.shield:
            self.stamina += 2
        else:
            self.stamina += 10
        if self.stamina > 15:
            self.stamina = 15


class Dragon(BattleUnit):

    default_health = 12
    attack_force = 5
    default_stamina = 10
    shield = False

    def __init__(self):
        super().__init__(Dragon.default_health, Dragon.attack_force,
                         Dragon.default_stamina, Dragon.shield)

    def stamina_refill(self):
        if self.stamina < Dragon.default_stamina:
            self.stamina = Dragon.default_stamina


info = ['[A] - to attack', '[S] - to rise a shield',
        '[DS] - to deactivate a shield']
main()
