# i = 0
# list = ["apple",5,"END2" ,True, "banana", "cherry"]
# while(i<len(list)):
#     print(list[i])
#     i += 1

# for i in range(2 ,3):
#     print(i)

# for i in list:
#     print(i)
#     if(i == "END"):
#         print("Loop is DESTROYED")
#         break
# else:
#     print("Loop is completed")

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")

# list = ["ali" , "bilal" , "ahmed" , "abdullah" , "harry" , "nabeel"]
# for i in list:
#     if(i.startswith("a") or i.startswith("A")):
#         print(f"Hello {i}")

num = int(input("Enter a number: "))

# for i in range(num):
#     for j in range(num-i):
#         print(" ", end="")
#     for j in range(((i+1)*2)-1):
#         print("*", end="")
#     print("")

for i in range(num):
    print("*" * (i + 1))


