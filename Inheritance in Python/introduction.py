class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        
    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'
    
"""
Below is the AdminUser class inheriting the User privileges from the start.
Then you can add onto it.       
"""    
    
class AdminUser(User):
    def active_users(self):
        return '500'
    
tiffany = AdminUser('tiffany@devcamp.com', 'Tiffany', 'Hudgens')

kristine = User('Kristine@devcamp.com', 'Kristine', 'Hudgens')

print(tiffany.active_users())
# print(kristine.active_users())

"""
This is what you want.
Kristine does NOT have perms for that action.
"""

print(tiffany.active_users())
print(tiffany.greeting())

"""Tiffany AND Kristine should both be able to get the greeting as Tiffany has all perms that a normal user has AND more. Used this logic in pentesting.
"""
