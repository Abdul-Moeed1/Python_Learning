# from typing import List, Tuple, Dict, Set

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
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        break