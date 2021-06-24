from sys import exit
from random import randint
from textwrap import dedent
from death_art import *


class Weapon(object):

    weapon_list = ['rock', 'dagger', 'sword', 'shotgun', 'GODHAMMER']

    def player_weapon(self):
        choice = randint(0, 4)
        return Weapon().weapon_list[choice]

    def monster_weapon(self, lvl):
        weapon_name = Weapon().weapon_list[lvl]
        return weapon_name

    def dmg_pts(self, weapon):
        if weapon == 'rock':
            return randint(0, 3)
        elif weapon == 'dagger':
            return randint(2, 6)
        elif weapon == 'sword':
            return randint(5, 9)
        elif weapon == 'shotgun':
            return randint(4, 13)
        else:
            return randint(10, 16)


class Player(object):

    def __init__(self):
        self.name = self.ask_name()
        self.health = 50
        self.weapon = Weapon().player_weapon()
        self.defense = 0

    def ask_name(self):
        name = input("What is your name, brave soul?\n")
        return name

    def display_health(self):
        return 'HP:'+'*' * self.health + f" ({self.health})"

    def damage(self, dmg):
        dmg -= self.defense
        if dmg < 0:
            dmg = 0
        print(f"Enemy inflicted {dmg} damage points!")
        self.health -= dmg

    def combat_display(self):
        print(self.name)
        print(f"Weapon: {self.weapon}")
        print(self.display_health())
        print("")

    def attack(self):
        dmg_pts = Weapon().dmg_pts(self.weapon)
        return dmg_pts

    def defend(self):
        df_pts = 0
        if self.health > 12:
            df_pts = randint(3, 8)
        elif self.health >= 6:
            df_pts = randint(2, 6)
        else:
            df_pts = randint(0, 3)
        self.defense = df_pts
        return 0

    def dance(self):
        instakill = 0
        if randint(0, 9) > 7:
            instakill = 100
        else:
            print("Nice try, but this isn't a musical.")
        return instakill

    def combat_choice(self):
        choice = input("1) Attack, 2) Defend, 3) Dance >> ")
        if choice == '1':
            return self.attack()
        elif choice == '2':
            return self.defend()
        elif choice == '3':
            return self.dance()
        else:
            print('Pick a real choice, coward!')
            return self.combat_choice()


class Enemy(Player):

    def __init__(self, level):
        self.level = level
        self.name, self.health = self.monster_stats(level)
        self.weapon = Weapon().monster_weapon(level)

    def cruel_phrase(self):
        phrases = ['Prepare to be crushed and devoured, peon!',
                   'Hope you like the taste of blood, weakling!',
                   'You think you stand a chance? Pssshhhhh',
                   'You can\'t handle my brawn, child',
                   'Well, well, another eager victim',
                   'You\'re about to die, little one',
                   'I eat chickens like you for breakfast.',
                   'It\'s game over, bud.']
        loc = randint(0, len(phrases)-1)
        phrase = phrases.pop(loc)
        return phrase

    def monster_stats(self, lvl):
        names = ['Goblin',
                 'Witch',
                 'Werewolf',
                 'Demoness',
                 'Master p0wner (aka Satan)']
        healths = [6, 10, 16, 22, 30]
        name = names.pop(lvl)
        health = healths.pop(lvl)

        return name, health

    def damage(self, dmg):
        print(f"You inflicted {dmg} damage points!")
        self.health -= dmg

    def combat_choice(self):
        choice = randint(1, 10)
        if self.level == 0 or self.level == 1:
            if choice > 4:
                return self.defend()
            else:
                return self.attack()
        elif self.level == 2 or self.level == 3:
            if choice > 7:
                return self.defend()
            else:
                return self.attack()
        else:
            return self.attack()

    def combat_display(self):
        print(self.name)
        print(f"Weapon: {self.weapon}")
        print(self.display_health())
        print(self.cruel_phrase())
        print("")


class Room(object):

    def __init__(self, player):
        self.player = player
        self.level = enemy.level

    def has_food(self):
        food = randint(1, 10)
        if food > 6:
            print("You found a leather shoe. Beggars can't be choosers.\n(Health +5)")
            return 5
        else:
            print("Nothing but bones in here.\n (Health +0)")
            return 0

    def update(self, enemy_lvl):
        if enemy_lvl == -1:
            print(f"\n{hell}\nYou lost buddy. Enjoy your eternity in hell!")
            exit(0)
        elif enemy_lvl == 4:
            print(
                f"\n{unicorn}\nYou killed satan! Angels are singing your praises.")
            exit(0)
        else:
            enemy_lvl += 1
            player.health += self.has_food()
            next_enemy = Enemy(enemy_lvl)
            self.combat_sequence(next_enemy)

    def combat_sequence(self, enemy):
        intro_list = [f'{goblin}\nGoblins are the scum of the earth', f'\n{witch}\nYou killed the goblin.\n\n   Here\'s a witch. Dont get hexed',
                      f'\n{werewolf}\nDing, Dong the witch is dead.\n\n   Here\'s a werewolf. Werewolf Schmerwolf. Although he is kind of big...',
                      f'\n{demoness}\nDone with wolfy... Holy smokes!\n\n  They say this demoness is Satan\'s daughter. My bowels are quivering...',
                      f'\n{satan}\nWell, she\'s goblin scraps now.\n\n   Here he is, you\'re old college roommate, Prince of Darkness.\n   Still a total slob...']
        print(intro_list[enemy.level]+'\n')
        player.weapon = Weapon().player_weapon()
        while player.health > 0 and enemy.health > 0:
            print(f"""
            ===========================================================
            ========================= Chamber {enemy.level + 1} =======================
            ===========================================================""")
            player.combat_display()
            enemy.combat_display()
            player_move = player.combat_choice()
            enemy_move = enemy.combat_choice()
            enemy.damage(player_move)
            player.damage(enemy_move)

        if player.health < 1:
            self.update(-1)
        self.update(enemy.level)


print(f"""
             DEATH CHAMBER FIVE
{pentagram}
    (a p0wn or get p0wned action thriller)
""")

player = Player()
enemy = Enemy(0)

print(f"""

Congratulations, {player.name}!
You made it to the death chambers.
Prepare to have your organs disemboweled and your flesh
consumed by the demons of the underworld! You probably know
there are five chambers, each more brutal than the last.
Have fun and use the handicap rails as needed.

Good luck, mortal scum....
""")
input("(Press enter to get annihilated)")
print("")
chamber = Room(player)
chamber.combat_sequence(enemy)
