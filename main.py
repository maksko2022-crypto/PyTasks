def show_tasks(tasks_list):
    if not tasks_list:
        print("\nСписок завдань порожній.") 
        return

    print("\n--- ТВОЇ ЗАВДАННЯ ---")
    for number, task in enumerate(tasks_list, start=1):
        if task["done"]:
            print(f"{number}. [✓ ВИКОНАНО] ~~{task['name']}~~")
        else:
            print(f"{number}. [ ] {task['name']}")


def add_task(tasks_list):
    new_task = input("Введи нове завдання: ").strip()
    if not new_task:
        print("Назва завдання не може бути порожньою.")
        return

    tasks_list.append({"name": new_task, "done": False})
    print("Успішно додано!")


def complete_task(tasks_list):
    if not tasks_list:
        print("\nНемає завдань, які можна позначити виконаними.")
        return

    show_tasks(tasks_list)
    task_number = input("Введи номер виконаного завдання: ").strip()
    if not task_number.isdigit():
        print("Введи номер зі списку.")
        return

    task_index = int(task_number) - 1
    if task_index < 0 or task_index >= len(tasks_list):
        print("Завдання з таким номером немає.")
        return

    tasks_list[task_index]["done"] = True
    print("Завдання позначено як виконане!")


my_tasks = []

while True:
    print("\n--- МЕНЮ ЗАВДАНЬ ---")
    print("1. Переглянути завдання")
    print("2. Додати завдання")
    print("3. Позначити завдання виконаним")
    print("0. Вийти")

    choice = input("Обери дію: ").strip()

    if choice == "1":
        show_tasks(my_tasks)
    elif choice == "2":
        add_task(my_tasks)
    elif choice == "3":
        complete_task(my_tasks)
    elif choice == "0":
        print("До зустрічі!")
        break
    else:
        print("Такого пункту меню немає. Спробуй ще раз.")

