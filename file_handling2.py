import os

# Open file
with open("example_dfhdsjfhdsjfh.txt",'w+') as file:
    print(file.tell())
    content = file.read()
    print(content)
    

print(file.closed)
print(content)
print(file.name)
print(file.mode)

# os.rename('example.txt', 'hello.txt')
# os.remove('hello.txt')

print(os.getcwd())
# print(os.mkdir('avinash'))
# print(os.rmdir('avinash'))