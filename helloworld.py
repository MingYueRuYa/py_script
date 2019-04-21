print('hello world')

def add(x, y):
   return x+1, y+1


x, y = add(1, 2)
#print(x, y)

def sub(x, y=1):
   return x-y

#print(sub(2))

#import student
from student import Student

obj = Student('linux', 23)
obj.print_info()
print(obj.__dict__)
