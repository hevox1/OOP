# инкапсуляци, git clone


class Emirlan:
    def __init__(self, name='Emirlan', age=18):
        self.__name=name
        self._age=age
    def __str__(self):
        return f'{self.__name}' \
               f'{self._age}'

    def run(self):
        self.__run()
        print(self.__name)
    def __run(self):
        print(self.__name, 'run')

    def __g(self):
        pass


e=Emirlan()

# e._age=11
# e._Emirlan__name='samir'

# e._run()

# print(e._Emirlan__name)
# e._Emirlan__run()





