import random
import time
# Generate Float Values
list_float = []
for i in range(100):
    list_float.append(random.random())

# print(list_float)

# Ludo - dice value 1-6 
num_list = []
for i in range(100):
    num_list.append(random.randint(1,6))


# print(num_list)

cards = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# print(random.choice(cards))


random.seed(123)
num_list = []
for i in range(50):
    num_list.append(random.randint(1,6))
print("Before", num_list)

random.seed(123)
num_list = []
for i in range(50):
    num_list.append(random.randint(1,6))
print("After ", num_list)

# random.shuffle(cards)
# print(cards)
# print(random.sample(cards, 2))
# time.sleep(5)
# print(random.choices(cards,k=3))