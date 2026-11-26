# from typing import List, Tuple, Dict, Set
from functools import reduce

# # Walrus operator is used to assign a value to a variable as part of an expression. It is represented by the symbol :=. The walrus operator allows you to both assign a value to a variable and return that value in a single expression.
# if ((n:=14)<18):
#     print(F"Sorry your cnic cannot be accepted because your age is {n} which is less than 18")
# else:
#     print(F"Your cnic is accepted because your age is {n} which is greater than 18")


# num : int = 54
# sentence : str = "I am learning python"

# def addition(num1:int,num2:int)->int:
#     return num1+num2

# myList : List[int] = [1,2,3,4,5]

# def httpStatus(statusCode:int)->str:
#     match statusCode:
#         case 200:
#             print("OK")
#         case 404:
#             print("Not Found")
#         case 500:
#             print("Internal Server Error")
#         case _:
#             print("Unknown Status Code")

# httpStatus(200)


# while True:
#     try:
#         num = int(input("Enter a number: "))
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
#     else:
#         break

# a = 30

# def myFunction():
#     global a
#     a = 20
#     print("Inside function:", a)

# print("Outside function:", a)
# myFunction()
# print("Outside function:", a)



l = ["hello" , "apple" , "world" , "cat"]

# index = 0
# for item in l:
#     print(f"at {index} index the element is {item}")
#     index += 1

# for i , item ,f in enumerate(l): 
#     print(f"at {i} index the element is {item}")

squaredList = [(i + i +i+i+i) for i in l ]
# print("::::".join(squaredList))
# for i in l:
#     squaredList.append(i + i +i+i+i)

# for i,item in enumerate(squaredList):
#     if(i==1 or i==2):
#         print(item)

# print(squaredList)


# square = lambda x : x ** 2
# print(square(4))

numList = [34 ,7 ,4,71,8,5,4,6 ,37 ,81]
def square(x):
    return x**2

def even(x):
    return (x%2 == 0)

def sum(a,b):
    return a+b

# Map
sql = map(square , numList)
print(list(sql))

# Filter
evenList= filter(even, numList)
print(evenList)
# l2= list(evenList)

print(reduce(sum , evenList))


