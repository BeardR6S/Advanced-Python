"""
If you've never heard of a lambda, essentially what it is, is a tool that allows you to wrap up a function.
Usually, a smaller function and then easily pass it to other functions. 
Now functions inside of python are what are called first-class citizens which means that you can treat a function like any type of object. 
"""

full_name = lambda first, last: f'{first} {last}'

print(full_name('Kristine', 'Hudgens'))

def greeting(name):
    print(f'Hi, {name}, How are you today? Its time to execute order 66.')

greeting(full_name('Tiffany', 'Hudgens'))



