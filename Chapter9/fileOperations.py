# file = open("readfile.txt" , "r")
# content = file.readlines()
# print(content)
# file.close()


with open("readfile.txt" , "r") as file:
    content = file.read()
    print(content)