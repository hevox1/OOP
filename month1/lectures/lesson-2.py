# наследование, полиморфизм
# инкапсуляция

# супер класс (не от какого друого класса не наследуется)
class Robot:
    brain = True
    def __init__(self, name, model, color, destynation):
        self.name=name
        self.model=model
        self.color=color
        self.destynation=destynation
    def __str__(self):
        return (f'name is {self.name}\n'
                f'color is {self.color}\n'
                f'model is {self.model}')
    def desti(self):
        print(self.destynation)

robot = Robot("vlad", 'A4', 'blue', 'video')
# print(robot)
# print(robot.desti())


# дочерний класс
class Robot2(Robot):
    def __init__(self, name, model, color, destynation, fly):
        super().__init__(name, model, color, destynation) # 1 способ наследования
        Robot.__init__(self, name, model, color, destynation) # 2 способ наследования (лучше подходит для множественного)
        self.fly=fly
    def desti(self):
        self.fly=False
        print(self.fly)
robot2=Robot2('terminator', 'T1001', 'pink', 'отбирает одежду', True)
print(robot2.fly)
robot2.desti()
robot.desti()

class Robot3(Robot2):
    def desti(self):
        print(f'{self}, теперь он летает')

MegaTron=Robot3('transformer', 'desipticon', 'red', 'wars', False)
MegaTron.desti()











