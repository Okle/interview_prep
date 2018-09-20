# Given an array, find the subarray
# (containing at least k numbers) which has the largest sum.
#
# Examples:
#
# Input : arr[] = {-4, -2, 1, -3}
#             k = 2
# Output : -1
# The sub array is {-2, 1}
#
# Input : arr[] = {1, 1, 1, 1, 1, 1}
#             k = 2
# Output : 6
# The sub array is {1, 1, 1, 1, 1, 1}

def LSS_k(arr, k):

    n = len(arr)
    sums = LSS_(arr)


    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]


    sum_of_ks = [0]*len(arr)
    sum_of_ks[k - 1] = curr_sum

    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        sum_of_ks[i] = curr_sum

    max_res = sum_of_ks[k - 1]
    print(sums)
    print(sum_of_ks)
    for i in range(k, n):
        max_res = max(max_res, max(sum_of_ks[i] + sums[i - k], sum_of_ks[i]))


    return max_res

def LSS(arr):

    n = len(arr)
    sums = [0] * n
    sums[0] = arr[0]

    for i in range(1, n):

        curr_sum = arr[i] + sums[i - 1]
        if arr[i] > curr_sum:
            sums[i] = arr[i]
        else:
            sums[i] = curr_sum

    return max(sums)

def LSS_(arr):

    n = len(arr)
    sums = [0] * n
    sums[0] = arr[0]

    for i in range(1, n):

        sums[i] = max(arr[i], arr[i] + sums[i - 1])

    return sums

# Sliding Window Maximum
def max_window(arr, k):

    index = 0
    while index < len(arr) - k:

        print(max(arr[index : index + k]))
        index += k



arr = [1, 2, -1, 3, -9, 8, 7]
# print(LSS(arr))
# print(LSS_(arr))
#
#
# arr = [-4, -2, 1, -3]
# print(LSS(arr))
# print(LSS_(arr))


arr = [-1, 2, -3, 4]
print(LSS_k(arr, 3))

# arr = [10, -10]
# print(LSS_k(arr, 1))

#
# print("=====")
# arr = [1, 2, -1, 3, -9, 8, 7]
# max_window(arr, 2)