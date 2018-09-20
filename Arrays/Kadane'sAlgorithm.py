# Given an array containing both negative and positive integers.
# Find the contiguous sub - array with maximum sum.


count = 6
my_list = [1, 2, 3, -8, 1, 100]

max_sum = my_list[0]
prev_max_sum = my_list[0]

for i in range(1, count):
    max_sum = max(my_list[i], my_list[i] + max_sum)
    prev_max_sum = max(max_sum, prev_max_sum)

print(prev_max_sum)
