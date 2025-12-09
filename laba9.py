import random                     # Імпортуємо модуль для генерації випадкових значень
import string                     # Імпортуємо модуль зі строковими константами (літери тощо)


def create_random_file(filename, lines_count=101, line_length=120):
    """Створює файл з випадковими літерами."""
    with open(filename, "w", encoding="utf-8") as f:          # Відкриваємо файл на запис
        for _ in range(lines_count):                          # Повторюємо потрібну кількість разів
            # Генеруємо рядок із line_length випадкових букв
            line = ''.join(random.choice(string.ascii_lowercase) for _ in range(line_length))
            f.write(line + "\n")                              # Записуємо рядок у файл з перенесенням


def count_pairs(filename, pairs_list_per_line):
    """Генератор, який рахує пари букв всередині рядків."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:      # Відкриваємо файл для читання
            for line_index, line in enumerate(f):              # Перебираємо рядки та їх індекси

                pairs = pairs_list_per_line[line_index]        # Отримуємо 3 пари для цього рядка
                pair_counts = {p: 0 for p in pairs}            # Створюємо словник лічильників пар

                words = line.strip().split()                   # "Розбиваємо" рядок на слова (фактично одне слово)

                for word in words:                             # Перебираємо всі слова (рядок)
                    word = word.lower()                        # Перетворюємо на нижній регістр
                    for i in range(len(word) - 1):             # Перебираємо всі позиції для пар літер
                        pair = word[i:i+2]                     # Беремо поточну пару букв
                        if pair in pair_counts:                # Якщо пара одна із потрібних
                            pair_counts[pair] += 1             # Збільшуємо лічильник

                yield pair_counts                              # Повертаємо результат для рядка

    except Exception as e:                                      # Обробка помилки читання файлу
        print(f"Помилка: {e}")                                 # Виводимо повідомлення про помилку
        return                                                 # Перериваємо виконання генератора


def main():
    FILE = "random_text.txt"                                  # Ім'я файлу з випадковими рядками

    create_random_file(FILE)                                  # Створюємо файл із випадковим текстом

    all_pairs = []                                            # Список усіх наборів пар для кожного рядка
    letters = string.ascii_lowercase                          # Усі малі англійські літери

    for _ in range(101):                                      # Для кожного з 101 рядка
        three_pairs = set()                                   # Будемо зберігати унікальні пари
        while len(three_pairs) < 3:                           # Треба отримати рівно 3 унікальні пари
            pair = random.choice(letters) + random.choice(letters)   # Генеруємо випадкову пару
            three_pairs.add(pair)                             # Додаємо її до множини
        all_pairs.append(list(three_pairs))                   # Додаємо список із 3 пар у загальний список

    result = count_pairs(FILE, all_pairs)                     # Отримуємо генератор підрахунку

    for i, res in enumerate(result, start=1):                 # Перебираємо результати генератора
        print(f"Рядок №{i}, пари {all_pairs[i-1]}: {res}")    # Виводимо номер рядка, пари та результат


if __name__ == "__main__":                                    # Точка входу при запуску
    main()                                                    # Викликаємо головну функцію
