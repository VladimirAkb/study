import random
import time


# Класс героя
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        """Инициализация героя"""
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Атака противника"""
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)  # Разброс урона
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        """Проверяет, жив ли герой"""
        return self.health > 0


# Класс игры
class Game:
    def __init__(self):
        """Создание игрока и компьютера"""
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        """Запуск игры"""
        print("\n⚔️ Битва начинается! ⚔️\n")

        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)  # Ход игрока
            if not self.computer.is_alive():
                print(f"\n🏆 {self.player.name} победил!\n")
                break

            time.sleep(1)  # Пауза перед ходом компьютера

            self.computer.attack(self.player)  # Ход компьютера
            if not self.player.is_alive():
                print(f"\n💀 {self.player.name} пал в битве. Победил {self.computer.name}!\n")
                break

            print(f"\n❤️ {self.player.name}: {self.player.health} | {self.computer.name}: {self.computer.health}\n")
            time.sleep(1)

        print("🎮 Игра окончена!")


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.start()
