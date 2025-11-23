import json
from Task import Task
class TaskManager:
    def __init__(self,filename = "tasks.json") :
        self.__filename = filename
        self.__tasks = self.__load_tasks()

    @property
    def tasks(self):
        return self.__tasks


    def add_task(self,title):
        new_task = Task(title)
        self.__tasks.append(new_task)
        return f' Задача "{title}" добавлена.'


    def mark_task_done(self,title):
        for task in self.__tasks:
            if task.title == title:
                task.mark_done()
                return f'Задача "{title}" отмечена как выполненная'


    def show_tasks(self):

        result = []
        number = 1
        for task in self.__tasks:
            result.append(f'{number}.{task.title} - {task.is_done}')
            number +=1
        return "\n".join(result)

    # Сохранение и загрузка из JSON
    def save_to_file(self):
        
        tasks_list = []
        for task in self.__tasks:
            tasks_list.append({
                "title" : task.title,
                "is_done" : task.is_done
            })
        with open(self.__filename, "w",encoding='utf-8') as f:
            json.dump(tasks_list,f,ensure_ascii=False,indent=4)
    def __load_tasks(self):
        try:
            with open(self.__filename,"r",encoding="utf-8") as f:
                tasks_list = json.load(f)
        except FileNotFoundError:
            return []

        tasks = []
        for item in tasks_list:
            task = Task(item["title"])
            if item.get("is_done") == "Выполнено":
                task.mark_done()
            tasks.append(task)
        return tasks







