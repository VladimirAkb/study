class User:
    def __init__(self, user_id, username, access_level):
        self.user_id = user_id
        self.username = username
        self.access_level = access_level

    def __str__(self):
        return f'ID: {self.user_id}, Username: {self.username}, Access Level: {self.access_level}'


class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1
        self.create_admin()

    def create_admin(self):
        admin = User(self.next_id, 'admin', 'admin')
        self.users.append(admin)
        self.next_id += 1

    def display_users(self):
        if not self.users:
            print("Список пользователей пуст.")
            return
        for user in self.users:
            print(user)

    def add_user(self, username, access_level):
        user = User(self.next_id, username, access_level)
        self.users.append(user)
        self.next_id += 1
        print(f"Пользователь {username} добавлен с ID {user.user_id} и уровнем доступа {access_level}.")

    def remove_user(self, user_id):
        if user_id == 1:
            print("Нельзя удалить администратора базы!")
            return
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")


def main():
    user_manager = UserManager()

    while True:
        print("\nМеню:")
        print("1 - Вывод списка пользователей с указанием уровня доступа")
        print("2 - Добавить пользователя с указанием уровня доступа")
        print("3 - Удалить пользователя по ID")
        print("4 - Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            user_manager.display_users()
        elif choice == '2':
            username = input("Введите имя пользователя: ")
            access_level = input("Введите уровень доступа (user/admin): ")
            user_manager.add_user(username, access_level)
        elif choice == '3':
            user_id = int(input("Введите ID пользователя для удаления: "))
            user_manager.remove_user(user_id)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
