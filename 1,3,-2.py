import random
new_list = []
dig_list = [random.randint(0, 10) for _ in range(3,11)]
index_list = [0,2,-2]
for i in index_list:
    new_list.append(dig_list[i])

print(dig_list)
print(new_list)