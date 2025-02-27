file = open("news.txt", "r")

content = file.read()

# count lines, words, characters
line_count = content.count('\n') + 1
word_Count = len(content.split(" "))
char_count = len(content)

print(line_count, word_Count, char_count)

file.close()