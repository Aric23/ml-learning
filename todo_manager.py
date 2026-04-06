# Менеджер списка задач
tasks = []

print("📝 Менеджер задач")
print("Команды:")
print("  add <задача>  - добавить задачу")
print("  list          - показать все задачи")
print("  done <номер>  - отметить задачу выполненной")
print("  delete <номер>- удалить задачу")
print("  exit          - выйти")

while True:
    command = input("\nВведите команду: ").strip().lower()
    
    if command == "exit":
        print("До свидания!")
        break
    
    elif command == "list":
        if not tasks:
            print("📭 Список задач пуст")
        else:
            print("\n📋 Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")
    
    elif command.startswith("add "):
        new_task = command[4:]  # берём текст после "add "
        tasks.append(new_task)
        print(f"✅ Добавлена задача: {new_task}")
    
    elif command.startswith("done "):
        try:
            num = int(command[5:])  # берём номер
            if 1 <= num <= len(tasks):
                completed = tasks.pop(num - 1)
                print(f"🎉 Задача выполнена: {completed}")
            else:
                print(f"❌ Нет задачи с номером {num}")
        except ValueError:
            print("❌ Введите номер задачи")
    
    elif command.startswith("delete "):
        try:
            num = int(command[7:])
            if 1 <= num <= len(tasks):
                deleted = tasks.pop(num - 1)
                print(f"🗑️ Удалена задача: {deleted}")
            else:
                print(f"❌ Нет задачи с номером {num}")
        except ValueError:
            print("❌ Введите номер задачи")
    
    else:
        print("❌ Неизвестная команда")