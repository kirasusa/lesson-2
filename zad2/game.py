import random

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, incoming_damage):
        return max(0, incoming_damage - self.armor)

    def attack(self, enemy):
        if self.health <= 0:
            print(f"{self.name} не может атаковать, так как повержен.")
            return

        damage_dealt = self._calculate_damage(random.randint(0, self.damage))
        enemy.health -= damage_dealt

        print(f"{self.name} атакует {enemy.name} и наносит {damage_dealt} урона.")
        print(f"У {enemy.name} осталось {max(0, enemy.health)} здоровья.\n")


class Player(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print("Бой начинается!\n")
        turn = 0

        while self.player.health > 0 and self.enemy.health > 0:
            if turn % 2 == 0:
                self.player.attack(self.enemy)
            else:
                self.enemy.attack(self.player)

            if self.player.health <= 0:
                print(f"{self.player.name} проиграл! {self.enemy.name} победил!")
                break
            elif self.enemy.health <= 0:
                print(f"{self.enemy.name} проиграл! {self.player.name} победил!")
                break

            turn += 1


player = Player(name="Игрок", health=100, damage=20, armor=10)
enemy = Enemy(name="Враг", health=100, damage=20, armor=10)

game = Game(player, enemy)
game.start_battle()

