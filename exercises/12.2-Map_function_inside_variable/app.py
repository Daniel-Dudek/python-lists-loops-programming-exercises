names = ['Alice', 'Bob', 'Marry', 'Joe', 'Hilary', 'Stevia', 'Dylan']

def prepender(name):
    return "My name is: " + name
    
# Your code here
my_list = list(map(prepender, names))
print(my_list)