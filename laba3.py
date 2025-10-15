# Лабораторна робота №3

# порожній словник для збереження результатів
grades = {}

while True:
    name = input("Введіть ім'я студента (або 'завершити'): ")
    if name.lower() == "завершити":
        break

    grade_input = input(f"Введіть оцінку для {name}: ")

    if not grade_input.isdigit():
        print("Потрібно ввести число! Спробуйте ще раз.")
    else:
        grade = int(grade_input)

        if grade < 1 or grade > 12:
            print("Оцінка має бути від 1 до 12. Спробуйте ще раз.")
        else:
            grades[name] = grade

# підрахунки
if grades:
    all_grades = list(grades.values())
    avg = sum(all_grades) / len(all_grades)

    # категорії оцінок
    excellent = [name for name, g in grades.items() if 10 <= g <= 12]
    good = [name for name, g in grades.items() if 7 <= g <= 9]
    bad = [name for name, g in grades.items() if 4 <= g <= 6]
    failed = [name for name, g in grades.items() if 1 <= g <= 3]

    # виводимо
    print("\nСписок студентів та їх оцінок:")
    for name, grade in grades.items():
        print(f"{name}: {grade}")

    print(f"\nСередній бал по групі: {avg:.2f}")
    print(f"Відмінники (10-12): {len(excellent)}  {', '.join(excellent) if excellent else 'немає'}")
    print(f"Хорошисти (7-9): {len(good)}  {', '.join(good) if good else 'немає'}")
    print(f"Відстаючі (4-6): {len(bad)}  {', '.join(bad) if bad else 'немає'}")
    print(f"Незадовільно (1-3): {len(failed)}  {', '.join(failed) if failed else 'немає'}")
else:
    print("Не введено жодної оцінки.")
