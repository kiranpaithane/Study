l1 = [10,89,20,10,46,22,89,3]

# large = l1[0]
# smallest = l1[0]
# for i in range(1,len(l1)):
#     if l1[i]<large:
#         #second = large
#         large = l1[i]
# print(large)


empty_list = []

for i in l1:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)