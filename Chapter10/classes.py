class Calculator:
    def __init__(self , number):
        self.number = number
    def square(self):
        return self.number ** 2
    def cube(self):
        return self.number ** 3
    def square_root(self):
        return self.number ** 0.5
    def __add__(self, other):
        return self.number + other.number
    def __len__(self):
        return self.number
    @staticmethod
    def greet():
        return "Hello, welcome to the calculator!"
    @property
    def name(self):
        return f"{self.firstName} {self.lastName}"
    @name.setter
    def name(self, name):
        names = name.split(" ")
        self.firstName = names[0]
        self.lastName = names[1]
        return 


num = Calculator(4)
num2 = Calculator(5)
# print(num + num2)
print(len(num))
# print("Square" , num.square())
# print(num.cube())
# print(num.square_root())
# print(num.greet())
# print(Calculator.greet())
# num.name = "John Doe Real Estate Investor"
# print(num.name)