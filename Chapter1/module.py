import pyjokes

# THIS IS A TEST FILE FOR THE PYJOKES MODULE
joke = pyjokes.get_joke()
print(joke)
print('''
How Python Achieves Project-Level Isolation

Even though pip doesn't create a node_modules folder automatically, Python developers still keep projects strictly separated using Virtual Environments (.venv).
''')

# import pyttsx3
# engine = pyttsx3.init()

# engine.say("I will speak this text")
# engine.runAndWait()

import os

# # List contents of the current directory
# contents = os.listdir()
# print(contents)

# # List contents of a specific directory
# path = "/"
# for item in os.listdir(path):
#     print(item)
