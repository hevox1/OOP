# инкапсуляци, git clone


class Emirlan:
    def __init__(self, name='Emirlan', age=18):
        self.__name=name
        self.__age=age
    def __str__(self):
        return f'{self.__name}' \
               f'{self._age}'

    def run(self):
        self.__run()
        print(self.__name)
    def __run(self):
        print(self.__name, 'run')

    @property
    def emirlan(self):
        return f'{self.__name} {self.__age}'
    @emirlan.setter
    def emirlan(self, name, age):
        self.__name=name
        self.__age=age
    # @name.setter
    # def name(self, name):
    #     self.__name=name



e=Emirlan()

# e._age=11
# e._Emirlan__name='samir'

# e._run()

# print(e._Emirlan__name)
# e._Emirlan__run()


amir=Emirlan('Emirlan', 0)
# amir.set_emirlan('Amir', 12)
# print(amir.get_emirlan())
amir.emirlan
amir.emirlan=








