# class Website:
#     def __init__(self, title):
#         self.title = title
        
# ws = Website('My Website Title')
# # print(ws.title)
# print(ws.__dict__)

# ws_two = Website('Second Title')
# print(ws_two.__dict__)

class DifferentWebsite:
    title = 'My Class Title'
    """
    Showing class attribute
    """    

dw = DifferentWebsite()
print(dw.title)

dw_two = DifferentWebsite()
print(dw_two.__dict__) #returns {} rather then the title.

"""
can be changed to dw.__dict__ and it will return {}, title is specifically attached to Class DifferentWebsite.  
Its hard coded in.
"""