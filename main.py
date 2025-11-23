from TaskManager import TaskManager


if __name__ == '__main__':
    manager = TaskManager()

    while True:
        command = input("Введите команду(add/done/show/exit):")
        if command == "add":
            title = input("Введите название задачи:")
            print(manager.add_task(title))
        elif command == "done":
            title = input("Введите название задачи:")
            print(manager.mark_task_done(title))
        elif command == 'show':
            print(manager.show_tasks())
        elif command == "exit":
            manager.save_to_file()
            print("Выход из программы")
            break
        else:
            print("Неизвестная команда!")


