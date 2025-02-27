import os
import shutil
# # Open file
# with open("example_dfhdsjfhdsjfh.txt",'w+') as file:
#     print(file.tell())
#     content = file.read()
#     print(content)
    

# print(file.closed)
# print(content)
# print(file.name)
# print(file.mode)

# os.rename('example_copy copy.txt', 'hello.txt')
# os.remove('hello.txt')

# print(os.getcwd())
# print(os.listdir())
# # print(os.mkdir('avinash'))
# print(shutil.rmtree('pack1'))

print(os.path.exists("hello.txt"))
print(os.path.isdir('sciops'))
print(os.path.isfile('sciops'))
print(os.environ.get("HOME"))

print(os.environ.get("PATH"))
os.environ["MY_PATH_VAR"] = "/home/avinash/online class project"
print(os.environ.get("MY_PATH_VAR"))