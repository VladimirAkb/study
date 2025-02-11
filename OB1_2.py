class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в магазин '{self.name}' по цене {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")

    def get_item_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' в магазине '{self.name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")


# Создание объектов класса Store
store1 = Store("Магазин 1", "Улица Ленина, 1")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2 = Store("Магазин 2", "Улица Пушкина, 2")
store2.add_item("апельсины", 1.2)
store2.add_item("груши", 0.9)

store3 = Store("Магазин 3", "Улица Чехова, 3")
store3.add_item("киви", 1.5)
store3.add_item("вишни", 2.0)

# Примеры использования методов
print(store1.get_item_price("яблоки"))  # Вывод: 0.5
store1.update_item_price("яблоки", 0.6)  # Обновляем цену
print(store1.get_item_price("яблоки"))  # Вывод: 0.6
store1.remove_item("бананы")              # Удаляем товар
print(store1.get_item_price("бананы"))   # Вывод: None
