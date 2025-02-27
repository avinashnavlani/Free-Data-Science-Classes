
# Open file
file = open("example1.txt",'w+')

# write content on file
file.write("Welcome to free online class!")

# close the file
file.close()

file = open("example1.txt",'a+')
file.write("Hello Everyone!") # overwritten the existing content because of write mode but in append mode it will add the content to existing file.

print(file.tell()) # location of cursor
file.seek(0,0) # move your cursor
print(file.tell()) 
text = file.read()
print(text)