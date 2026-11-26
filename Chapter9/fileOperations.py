# file = open("readfile.txt" , "r")
# content = file.readlines()
# print(content)
# file.close()


# with open("readfile.txt" , "r") as file:
#     content = file.read()
#     print(content)

# with open("poems.txt" , "r") as file:
#     content = file.read()
#     if "twinkle" in content:
#         print("Twinkle is present in the file")
#     else:
#         print("Twinkle is not present in the file")

with open("cat.txt" , "r+") as file:
    content = file.read()
    content = content.replace("dog" , "@")
    file.seek(0) 
    file.write(content)
