"""Example 01 – Classes and objects."""


class Player:
    max_health = 100   # class attribute: shared by every player

    def __init__(self, name):
        self.name = name                   # instance attributes: one per player
        self.health = Player.max_health
        self.level = 1

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        if self.health == 0:
            print(f"💀 {self.name} has been defeated!")

    def heal(self, amount):
        self.health = min(Player.max_health, self.health + amount)

    def level_up(self):
        self.level += 1
        print(f"⭐ {self.name} reached level {self.level}!")

    def status(self):
        return f"{self.name} | Level {self.level} | ❤️ {self.health}/{Player.max_health}"


hero = Player("Ada")
villain = Player("Bug")

print(hero.status())
print(villain.status())

villain.take_damage(40)
hero.level_up()
hero.take_damage(15)
hero.heal(5)

print()
print(hero.status())
print(villain.status())

villain.take_damage(100)
print(villain.status())

print("\nEach object is separate:", hero is villain)
print("Type of hero:", type(hero))
