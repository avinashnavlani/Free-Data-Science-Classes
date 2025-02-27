
# open the existing file
file1 = open('example1.txt', 'r')

# read the content of existing file
content = file1.read()

# create a file for copying content
file2 = open('example_copy.txt', 'w')

# writing the content on new file
file2.write(content)

file1.close()
file2.close()
