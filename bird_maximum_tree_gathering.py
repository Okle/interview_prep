def find_max(arr, n, m):

    result = 0
    for i in range(m):
        result += arr[i]

    max_sum = result
    for j in range(m, n):
        result = result + arr[j] - arr[j - m]
        max_sum = max(max_sum, result)

    return max_sum

def calc_gather(arr, n, m):


    if m >= n:
        m = n
        return find_max(arr, len(arr), m)

    new_arr = arr[:] + arr[:m - 1]

    return find_max(new_arr, len(new_arr), m)



# arr = [5, 7, 8, 5, 7, 0, 4, 7, 0]
# print(calc_gather(arr, 9, 9))
arr = [3, 8, 4, 7, 8, 9, 5, 0, 8]
print(calc_gather(arr, 9, 7))