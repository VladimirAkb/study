import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

class Mammal(Animal):
    def make_sound(self):
        return "Roar!"

class Reptile(Animal):
    def make_sound(self):
        return "Hiss!"

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} goes: {animal.make_sound()}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        data = {
            'animals': [{'name': animal.name, 'age': animal.age, 'type': animal.__class__.__name__} for animal in self.animals],
            'employees': [{'name': employee.name, 'type': employee.__class__.__name__} for employee in self.employees]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for animal_data in data['animals']:
                if animal_data['type'] == 'Bird':
                    animal = Bird(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Mammal':
                    animal = Mammal(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Reptile':
                    animal = Reptile(animal_data['name'], animal_data['age'])
                self.add_animal(animal)

            for employee_data in data['employees']:
                if employee_data['type'] == 'ZooKeeper':
                    employee = ZooKeeper(employee_data['name'])
                elif employee_data['type'] == 'Veterinarian':
                    employee = Veterinarian(employee_data['name'])
                self.add_employee(employee)

class Employee:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

def main():
    zoo = Zoo()

    # Создание объектов животных
    bird = Bird("Tweety", 2)
    mammal = Mammal("Leo", 5)
    reptile = Reptile("Snappy", 3)

    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    # Создание сотрудников
    zookeeper = ZooKeeper("John")
    veterinarian = Veterinarian("Alice")

    zoo.add_employee(zookeeper)
    zoo.add_employee(veterinarian)

    # Основное меню
    while True:
        print("\n1. Show animal sounds")
        print("2. Show employees")
        print("3. Add animal")
        print("4. Add employee")
        print("5. Save zoo data")
        print("6. Load zoo data")
        print("7. Exit")

        choice = input("Choose an action (1-7): ")

        if choice == '1':
            animal_sound(zoo.animals)
        elif choice == '2':
            for emp in zoo.employees:
                if isinstance(emp, ZooKeeper):
                    print(f"{emp.name} (ZooKeeper) can: {emp.feed_animal(bird)}")
                elif isinstance(emp, Veterinarian):
                    print(f"{emp.name} (Veterinarian) can: {emp.heal_animal(mammal)}")
        elif choice == '3':
            print("Choose animal type to add: 1. Bird 2. Mammal 3. Reptile")
            animal_choice = input("Enter choice (1-3): ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            if animal_choice == '1':
                zoo.add_animal(Bird(name, age))
            elif animal_choice == '2':
                zoo.add_animal(Mammal(name, age))
            elif animal_choice == '3':
                zoo.add_animal(Reptile(name, age))
        elif choice == '4':
            print("Choose employee type to add: 1. ZooKeeper 2. Veterinarian")
            emp_choice = input("Enter choice (1-2): ")
            name = input("Enter name: ")
            if emp_choice == '1':
                zoo.add_employee(ZooKeeper(name))
            elif emp_choice == '2':
                zoo.add_employee(Veterinarian(name))
        elif choice == '5':
            zoo.save_to_file("zoo_data.json")
            print("Zoo data saved.")
        elif choice == '6':
            zoo.load_from_file("zoo_data.json")
            print("Zoo data loaded.")
        elif choice == '7':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
```

### Описание программы:
### 1. **Класс `Animal`** - базовый класс для всех животных.
### 2. **Классы `Bird`, `Mammal`, `Reptile`** - подклассы, переопределяющие метод `make_sound()`.
### 3. **Функция `animal_sound()`** - принимает список животных и выводит звуки.
### 4. **Класс `Zoo`** - хранит животных и сотрудников, имеет методы для добавления и сохранения данных.
### 5. **Классы `ZooKeeper` и `Veterinarian`** - определяют сотрудников с специфическими методами.
### 6. **Сохранение и загрузка данных** - реализована с помощью JSON.
### 7. **Меню действий пользователя** - позволяет взаимодействовать с приложением, добавлять животных и сотрудников, и сохранять/загружать данные.

###