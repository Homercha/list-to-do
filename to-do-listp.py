tasks = []

while True:
    print("\n1. Додати завдання")
    print("2. Показати список")
    print("3. Видалити завдання")
    print("4. Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        task = input("Введіть завдання: ")

        if task.strip():
            tasks.append(task)
            print("Завдання додано.")
        else:
            print("Завдання не може бути порожнім.")

    elif choice == "2":
        print("\nСписок завдань:")

        if len(tasks) == 0:
            print("Список порожній.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("Немає завдань для видалення.")
        else:
            try:
                number = int(input("Номер завдання: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f"Завдання '{removed}' видалено.")
                else:
                    print("Невірний номер.")

            except ValueError:
                print("Потрібно ввести число.")

    elif choice == "4":
        print("До побачення!")
        break

    else:
        print("Невірний вибір.")
