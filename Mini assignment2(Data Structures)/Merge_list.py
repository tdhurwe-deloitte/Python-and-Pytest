from itertools import product
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
all_combination = product(list1, list2)
new_list = []
for a, b in all_combination:
    new_list.append(a+b)
print(new_list)
