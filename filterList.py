# Write some code to find out the common values into these lists

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 8, 5, 10]

# 1. => Through numpy module
# import numpy as n
# print(n.intersect1d(list1, list2))

# 2. => Through for in loop
# filteredList = [e for e in list1 if e in list2]
# print(filteredList)

# 3. => Through using Python set Constructor
# set_list1 = set(list1)
# set_list2 = set(list2)
# filtered_set = set_list1 & set_list2
# filtered_list = list(filtered_set)
# print(filtered_list)
