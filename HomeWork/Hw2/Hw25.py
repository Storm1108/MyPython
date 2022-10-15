import random

num_list_start = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_list_rand = []
checklist = []
while len(num_list_rand) < len(num_list_start):
    temp_random = round(random.random() * (len(num_list_start) -1))
    if temp_random not in checklist:
        print(temp_random)
        num_list_rand.append(num_list_start[temp_random])
        checklist.append(temp_random)
print(num_list_start)
print(num_list_rand)
