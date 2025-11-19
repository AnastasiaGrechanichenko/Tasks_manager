class Task:


    def __init__(self,title,is_done = False):
        self.__title=title
        self.__is_done = "Не выполнено"


    @property
    def is_done(self):
        return self.__is_done


    @property
    def title(self):
        return self.__title

    def mark_done(self):
        self.__is_done = "Выполнено"
        return f'Задача "{self.__title}" отмечена как выполненная'




