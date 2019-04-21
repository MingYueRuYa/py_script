# student object
class Student():
    name = ''
    age  = 0

    def __init__(self, name, age):
        self.name   = name
        self.age    =  age
        print(self.name, self.age)


    def print_info(self):
        print('name:', self.name, 'age:', str(self.age))

