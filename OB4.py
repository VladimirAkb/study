from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

class Axe(Weapon):
    def attack(self):
        return "Боец наносит сокрушительный удар топором."

# Шаг 3: Класс бойца
class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"{self.name} выбирает {new_weapon.__class__.__name__.lower()}.")

    def attack(self):
        print(self.weapon.attack())

# Шаг 4: Класс монстра
class Monster:
    def __init__(self, health=100):
        self.health = health

    def take_damage(self, damage=100):
        self.health -= damage
        if self.health <= 0:
            print("Монстр побежден!")

# Шаг 5: Демонстрация боя
def main():
    fighter = Fighter("Боец", Sword())  # Боец начинает с меча
    monster = Monster()

    fighter.attack()
    monster.take_damage()

    fighter.change_weapon(Bow())  # Меняем оружие на лук
    fighter.attack()
    monster.take_damage()

    fighter.change_weapon(Axe())  # Меняем оружие на топор
    fighter.attack()
    monster.take_damage()

if __name__ == "__main__":
    main()
