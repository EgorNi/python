from itertools import count, cycle
import time

for i in count(1):
    print(i)
    if i >= 20:
        break


my_list = ['one', 'two', 'three', 'four', 'five', 'go']
for i in cycle(my_list):
    print(i)
    time.sleep(0.2)
    if i == 'go':
        break
