import time
import tracemalloc

tracemalloc.start()

start_time = time.time()

start = time.perf_counter()

# open the existing file
file1 = open('example1.txt', 'r')

# read the content of existing file
content = file1.read()

# create a file for copying content
file2 = open('example_copy_1.txt', 'w')

# writing the content on new file
file2.write(content)

file1.close()
file2.close()

end_time = time.time()

end = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()

tracemalloc.stop()

print("Execution time[time]:", (end_time-start_time))
print("Execution time[perf_counter]:", (end-start))
print("Highest Consumed Memory: KB", peak/1000)
print("Currently Consumed Memory: KB", current/1000)