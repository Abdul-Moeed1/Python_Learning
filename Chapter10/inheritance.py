class Person:
    def greet(self):
        return "Hello Person!"
    
class Human:
    def greet(self):
        return "Hello Human!"

class Student( Human , Person):
    pass
    # def greet(self):
    #     return "Hello Student!"

s = Student()
print(s.greet()) 