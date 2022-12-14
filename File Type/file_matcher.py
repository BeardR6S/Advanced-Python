import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('Text files:', file)

        if fnmatch.fnmatch(file, '*.rb'):
            print('Ruby files:', file)

        if fnmatch.fnmatch(file, '*.yml'):
            print("Yaml files: ", file)
            
        if fnmatch.fnmatch(file, "*.py"):
            print("Python files: ", file)


# list_files()

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennet 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print("Second Base Players: ", second_base_players)


"""
    def print_func():
        print('words')

    def return_func():
        words = 'words'
        return words
    
the first one will print to the console / terminal the second one will return a value, so you will have it to use later in the program, like this:

new_text = return_func()

#other code...

print(new_text)
"""