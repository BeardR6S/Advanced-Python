#frowned upon, but still being shown?
class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'

google = Invoice('Google', 100)

#"get process"

print(google.client)

#"setter process"

google.client = 'Yahoo'

print(google.client) 