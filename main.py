my_list = [1, 3,0,0,14,12,0,3,5]

zero_quantity = my_list.count(0)

new_list = [x for x in my_list if x!=0] + [0]*zero_quantity
print(new_list)