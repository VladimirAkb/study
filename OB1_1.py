class Task:
    def __init__(self, description, due_date):
        self.description = description  # Описание задачи
        self.due_date = due_date  # Срок выполнения задачи
        self.is_completed = False  # Статус задачи: выполнена или нет

    def mark_as_completed(self):
        """Отметить задачу как выполненную"""
        self.is_completed = True

    def __str__(self):
        """Возвращает строковое представление задачи"""
        status = "Выполнено" if self.is_completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список всех задач

    def add_task(self, description, due_date):
        """Добавить новую задачу"""
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        """Отметить задачу как выполненную по индексу"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Задача с таким индексом не найдена.")

    def show_current_tasks(self):
        """Показать список всех не выполненных задач"""
        print("Текущие задачи:")
        for task in self.tasks:
            if not task.is_completed:
                print(task)

    def show_all_tasks(self):
        """Показать список всех задач"""
        print("Текущие задачи:")
        for task in self.tasks:
            print(task)

# Пример использования
task_manager = TaskManager()

# Добавляем задачи
task_manager.add_task("Сделать домашку", "2025-01-30")
task_manager.add_task("Купить продукты", "2025-01-28")
task_manager.add_task("Позвонить другу", "2025-01-27")

# Отметить задачу как выполненную
#task_manager.mark_task_completed(1)

# Показать текущие (не выполненные) задачи
task_manager.show_current_tasks()

while True:
    #print("Выберите действие:")
    print("1. Добавить задачу")
    print("2. Выполнить задачу")
    print("3. Вывести список текущих задач")
    print("4. Вывести список всех задач")
    print("5. Выход")

    choice = input("Выберите действие (1-5): ")

    if choice == '1':
        # Новая задача
        task_name = input("Введите опсание задачи: ")
        task_date = input("Введите срок задачи в формате ГГГГ-ММ-ДД: ")
        task_manager.add_task(task_name, task_date)
    elif choice == '2':
        #len(task_manager.tasks)
        try:
            number = int(input("Введите номер выполненной задачи от 1 до " + str(len(task_manager.tasks))))
            #print(f"Вы ввели целое число: {number}")
            task_manager.mark_task_completed(number - 1)
        except ValueError:
            print("Невозможно преобразовать введенное значение в целое число. Пожалуйста, попробуйте еще раз.")
        #task_manager.mark_task_completed(1)
    elif choice == '3':
        task_manager.show_current_tasks()
    elif choice == '4':
        task_manager.show_all_tasks()
    elif choice == '5':
        print("Выход из программы. До свидания!")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите от 1 до 4.")