dig_list = [2, 0 , 4, 7, 8]
result =1
for i in range(0,len(dig_list),2):
    result *= dig_list[i]
result *= dig_list[-1]
if len(dig_list) == 0:
    result = 0
print(result)