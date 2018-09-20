# Closest product pair in an array
#
# Input : arr[] = [2, 3, 5, 9]
#         x = 47
# Output : {5, 9}
#
# Input : arr[] = [2, 3, 5, 9]
#         x = 8
# Output : {2, 5}

def close_pair(my_list, sum):

    temp_result = sum
    ret_val = ()

    for index1 in range(len(my_list) - 1):
        first = my_list[index1]
        for index2 in range(len(my_list) - index1):
            second = my_list[index2 + index1]
            product = first + second
            temp = abs(sum - product)
            if temp != 0 and temp < temp_result:
                temp_result = temp
                ret_val = (first, second)

    return ret_val

#arr = [2, 3, 5, 9]
#print(close_pair(arr, 47))

#arr1 = [2, 3, 5, 9]
#print(close_pair(arr1, 8))

#arr2 = [2, 3, 5, 9, 10, 20, 33, 44, 55]
#print(close_pair(arr2, 27))

# Given an array containing both negative and positive integers.
# Find the contiguous sub-array with maximum sum.
# Input
# 2
# 3
# 1 2 3
# 4
# -1 -2 -3 -4
# Output
# 6
# -1
# Input:
# 5
# 4 5 6 -3 7
#
# Its Correct output is:
# 19


def cont_subarr_max_sum(my_list, count):

    max_sum = my_list[0]
    prev_max_sum = my_list[0]

    for i in range(1, count):

        max_sum = max(my_list[i], my_list[i] + max_sum)
        prev_max_sum = max(max_sum, prev_max_sum)

    return prev_max_sum


#arr3 = [1, 2, 3]
#print(cont_subarr_max_sum(arr3, 3))

#arr4 = [-1, -2, -3, -4]
#print(cont_subarr_max_sum(arr4, 4))

#arr5 = [-1, -2, 10, -3, -4, 9, 10]
#print(cont_subarr_max_sum(arr5, 7))


# Given an array of size n-1 and given that there are numbers
# from 1 to n with one missing, the missing number is to be found.

def find_missing_num(my_list, count):

    miss_num = None

    for i in range(count - 1):

        if my_list[i] != i + 1:
            miss_num = i + 1
            break
        if i + 1 == len(my_list):
            miss_num = my_list[i] + 1
            break

    return miss_num

def find_missing_num1(my_list, count):

    for i in range(count - 1):
        my_sum = sum(my_list)

    dest_sum = (count + 1) * count * 0.5

    return int(dest_sum - my_sum)

#arr6 = [1]
#print(find_missing_num(arr6, 2))
#print(find_missing_num1(arr6, 2))
#arr7 = [1, 2, 3, 4]
#print(find_missing_num(arr7, 5))
#print(find_missing_num1(arr7, 5))
#arr8 = [2]
#print(find_missing_num(arr8, 2))
#print(find_missing_num1(arr8, 2))


# Given an unsorted array of non-negative integers,
# find a continuous sub-array which adds to a given number.
# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10

def subarr_sum(array, s, n):
    start_i = 0
    my_sum = 0
    for i in range(n):
        if my_sum < s:
            my_sum = my_sum + array[i]
        if my_sum > s:
            while my_sum > s and start_i < i:
                my_sum = my_sum - array[start_i]
                start_i += 1
        if my_sum == s:
            print(start_i + 1, i + 1)
            return
    print(-1)
    print('====')
#
#
# arr12 = [1, 2, 100, 2, 2]
# subarr_sum(arr12, 4, 5)
#
# arr9 = [1, 2, 3, 7, 5]
# subarr_sum(arr9, 12, 5)
#
# arr10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# subarr_sum(arr10, 15, 10)
#
# arr11 = [135, 101, 170, 125, 79 ,159 ,163 ,65 ,106 ,146 ,82 ,28 ,162 ,92 ,196 ,143 ,28 ,37 ,192 ,5 ,103 ,154 ,93 ,183 ,22 ,117 ,119 ,96 ,48 ,127 ,172 ,139 ,70 ,113 ,68 ,100 ,36 ,95 ,104 ,12 ,123 ,134]
# subarr_sum(arr11, 468, 42)
#

# Sort 0's, 1's and 2's array
# Dutch National Flag Algorithm - 3 way partitioning

def sort012( my_list, n):
    lo = 0
    mid = 0
    hi = n - 1

    while mid <= hi:
        if my_list[mid] == 0:
            my_list[lo], my_list[mid] = my_list[mid], my_list[lo]
            lo += 1
            mid += 1
        elif my_list[mid] == 1:
            mid += 1
        else:
            my_list[mid], my_list[hi] = my_list[hi], my_list[mid]
            hi -= 1
    return my_list

my_list = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
# print(sort012(my_list, len(my_list)))

def sort_three_way_part(my_list):

    min_i = 0
    mid_i = 0
    max_i = len(my_list) - 1


    while mid_i <= max_i:

        if my_list[mid_i] == 0:
            # swap with min
            my_list[mid_i], my_list[min_i] = my_list[min_i], my_list[mid_i]
            mid_i += 1
            min_i += 1
        if my_list[mid_i] == 1:
            mid_i += 1
        if my_list[mid_i] == 2:
            # swap with max
            my_list[mid_i], my_list[max_i] = my_list[max_i], my_list[mid_i]
            max_i -= 1

    return my_list

#my_list = [1, 2, 2, 2, 0, 1]
#print(sort_three_way_part(my_list))


# Equilibrium point

def equilibrium(array, n):

    if n == 1:
        print(array[0])
        return

    if n == 2:
        print(-1)
        return

    left = 0
    right = sum(array[1:])
    eq = -1

    for eq_index in range(1, n - 1):

        left = left + array[eq_index - 1]
        right = right - array[eq_index]

        if left == right:
            eq = eq_index + 1
            break

    print(eq)

# arr = [1, 1, 3, 5, 2, 2, 1]
# equilibrium(arr, 7)

# For Input:
# 7
# 1 101 2 3 100 4 5 - answer - 106
# 4
# 10 5 4 3 - answer - 10

def max_sum_increasing_sub(array, n):
    

    curr_sum = array[0]
    max_sum = 0
    for i in range(1, n):

        if array[i] >= array[i - 1]:
            curr_sum += array[i]
        else:
            max_sum = max(max_sum, curr_sum)
            for j in range(i - 1, -1, -1):
                if array[i] < array[j]:
                    curr_sum -= array[j]
                else:
                    curr_sum += array[i]
                    break
        if i == len(array) - 1:
            max_sum = max(max_sum, curr_sum)
    print(max_sum)


arr = [1, 101, 2, 3, 100, 4, 5, 200]
#max_sum_increasing_sub(arr, 8)

# arr = [1, 2, 3, 4, 5, 6]
# for j in range(len(arr)-1, 2, -1):
#     print(arr[j])


def drop_count(arr, n):

    temp_arr = [0] * n

    i = 0
    curr_max = arr[i]
    curr_max_i = i
    while i < n:
        j = i + 1
        next_max = 0
        next_max_i = j
        while j < n:
            if next_max < arr[j]:
                next_max = arr[j]
                next_max_i = j
            if next_max >= curr_max:
                next_max_i = j
                break
            j = j + 1

        if next_max == 0:
            break

        curr_max = min(curr_max, next_max)

        for k in range(curr_max_i + 1, next_max_i):
            temp_arr[k] = curr_max - arr[k]

        curr_max = next_max
        curr_max_i = next_max_i
        i = next_max_i

    print(sum(temp_arr))


arr = [8, 8, 2, 4, 5, 5, 1]
drop_count(arr, 7)

# code

t = int(input())
for e in range(t):

    n = int(input())
    arr = [int(i) for i in input().split()]

    answer = 'No'
    for i in range(n):
        arr[i] = arr[i] ** 2

    arr.sort()

    for i in reversed(range(n)):
        j = 0
        k = i - 1
        while j < k:
            trsum = arr[j] + arr[k]
            if trsum == arr[i]:
                answer = 'Yes'
                break
            elif trsum < arr[i]:
                j += 1
            else:
                k -= 1

    print(answer)
