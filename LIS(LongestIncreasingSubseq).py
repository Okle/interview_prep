# A naive Python implementation of LIS problem

""" To make use of recursive calls, this function must return
 two things:
 1) Length of LIS ending with element arr[n-1]. We use
 max_ending_here for this purpose
 2) Overall maximum as the LIS may end with an element
 before arr[n-1] max_ref is used this purpose.
 The value of LIS of full array of size n is stored in
 *max_ref which is our final result """

# global variable to store the maximum
global maximum

def _lis(arr, n):
    # to allow the access of global variable
    global maximum

    # Base Case
    if n == 1:
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    # Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]!!!
    #    IF arr[i-1] is smaller than arr[n-1], and max ending with
    #    arr[n-1] needs to be updated, then update it"""
    for i in range(1, n):
        # print('in loop i = ' + str(i))
        res = _lis(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1
            # print('i=' + str(i) + ' ; res=' + str(res) + '; maxEndingHere=' + str(maxEndingHere))

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere

def lis(arr):
    # to allow the access of global variable
    global maximum

    # lenght of arr
    n = len(arr)

    # maximum variable holds the result
    maximum = 1

    # The function _lis() stores its result in maximum
    _lis(arr, n)

    return maximum

# Dynamic programming Python implementation of LIS problem

# lis returns length of the longest increasing subsequence in arr of size n
def lis1(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            # print('i=' + str(i) + ' ; j=' + str(j))
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1


    return max(lis)

def lis_sum(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = list(arr)

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + arr[i]:
                lis[i] = lis[i] + arr[j]

    print(lis)
    return max(lis)


# end of lis function

# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
arr1 = [1, 101, 2, 3, 100, 4, 5]
print("Length of lis1 is", lis1(arr))
print("Length of lis is ", lis(arr))

print("Sum of lis is ", lis_sum(arr))
print("Sum of lis is ", lis_sum(arr1))

def long_incr_subarr(arr):

    sub_len = 1
    curr_len = 1
    temp = list()
    temp.append(arr[0])

    for i in range(len(arr)-1):

        if arr[i] < arr[i + 1]:
            curr_len += 1
            temp.append(arr[i + 1])
            sub_len = max(sub_len, curr_len)
        else:
            if len(arr) - i < sub_len:
                return temp
            else:
                temp = list()
                temp.append(arr[i + 1])
                curr_len = 1

    return temp


arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]
sub = long_incr_subarr(arr)
print(str(len(sub)))
print(sub)
arr = [12, 13, 1, 5, 4, 7, 8, 10, 10, 11]
sub = long_incr_subarr(arr)
print(str(len(sub)))
print(sub)


