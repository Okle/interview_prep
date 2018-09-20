def longestZigZag(arr):

    n = len(arr)

    if n == 0:
        return 0
    if n == 1:
        return 1

    v = [0] * (n - 1)

    for i in range(1, n):
        v.append(arr[i] - arr[i-1])

    n = len(v)
    first = 0
    while first < n and v[first] == 0:
        first += 1

    if first == n:
        return 1

    first_val = v[first]
    count = 2

    for i in range(first, n):

        if v[i] * first_val < 0:

            first_val *= -1
            count += 1

    return count

arr_0 = [1, 5, 3, 4, 6, 8, 5, 7, 5, 6, 3]
print(longestZigZag(arr_0))


arr = [1, 7, 4, 9, 2, 5]
print(longestZigZag(arr))

arr1 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
print(longestZigZag(arr1))

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(longestZigZag(arr2))

arr3 = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
print(longestZigZag(arr3))

arr4 = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23, 22, 617, 462, 459, 24]
print(longestZigZag(arr4))


