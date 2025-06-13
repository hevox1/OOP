class Human:
    # атрибуты уровня класса
    head = 1
    body = 1
    hands = 2
    # функция: конструктор
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def run(self):
        print(f"{self.name} is run")

    def __str__(self):
        return (f'name is {self.name},\n'
                f'age is {self.age},\n'
                f'head is {self.head}\n')

hum=Human('aldiar', 18)
hum.name = 'aldiar'
# hum.run()
# hum.foots=2
# print(hum,hum.foots)



class Raketa:
    toplivo = True
    kabina = 1
    korpus = 'ironMan'
    human = None
    def run(self, human):
        print(f'{human} is fly')

Raketa.run(hum.name)

