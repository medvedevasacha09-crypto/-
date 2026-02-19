# Батьківський клас
class Ludstvo:
    def __init__(self, population, planet):
        # _population — protected атрибут (рекомендовано не змінювати напряму)
        self._population = population

        # __planet — private атрибут (інкапсуляція)
        # Доступ до нього можливий тільки через getter/setter
        self.__planet = planet

    # Getter — метод для отримання значення приватного атрибуту
    def get_planet(self):
        return self.__planet

    # Setter — метод для зміни значення приватного атрибуту
    # Додаємо перевірку типу (інкапсуляція + контроль даних)
    def set_planet(self, new_planet):
        if isinstance(new_planet, str):
            self.__planet = new_planet

    # Метод для виводу інформації про об’єкт
    def info(self):
        return f"Людство проживає на планеті {self.__planet}, чисельність: {self._population}"

    # Метод поведінки
    def live(self):
        return "Людство розвивається та створює цивілізацію."


# Дочірній клас (наслідування)
class Civilization(Ludstvo):
    def __init__(self, population, planet, level):
        # Виклик конструктора батьківського класу
        super().__init__(population, planet)

        # Приватний атрибут рівня розвитку (інкапсуляція)
        self.__level = level

    # Getter для рівня розвитку
    def get_level(self):
        return self.__level

    # Setter з перевіркою допустимих значень
    def set_level(self, new_level):
        if new_level in ["низький", "середній", "високий"]:
            self.__level = new_level

    # Поліморфізм:
    # Перевизначаємо метод live(), який вже є у батьківському класі
    def live(self):
        return f"Цивілізація має {self.__level} рівень розвитку і активно прогресує."

    # Перевизначення методу info() з використанням super()
    def info(self):
        return f"{super().info()}, рівень розвитку: {self.__level}"


# --- Використання класів ---

# Створення об’єкта батьківського класу
humanity = Ludstvo(8000000000, "Земля")

# Виклик методів
print(humanity.info())
print(humanity.live())

print("-----")

# Створення об’єкта дочірнього класу
civil = Civilization(8000000000, "Земля", "високий")

# Виклик перевизначених методів (поліморфізм)
print(civil.info())
print(civil.live())
