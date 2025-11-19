from Task import Task
class TaskManager:
    def __init__(self,tasks = None) :
        self.__tasks = []

    @property
    def tasks(self):
        return self.__tasks


    def add_task(self,title):
        new_task = Task(title)
        self.__tasks.append(new_task)
        return f' Задача {title} добавлена.'


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




