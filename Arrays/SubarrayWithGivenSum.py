
def getIndexSubArrOfSum(n, sum, array):

    for i in range(n):
        curr_sum = array[i]
        if curr_sum < sum:
            for j in range(i + 1, n):
                curr_sum = curr_sum + array[j]
                if curr_sum == sum:
                    return (i + 1, j + 1)
                elif curr_sum > sum:
                    break
    return (-1,)


def getIndexSubArrOfSum_htbl(n, sum, array):


    curr_sum = array[0]
    if curr_sum == sum:
        return (1,)

    i = 1
    start = 0
    while i <= n:

        # If curr_sum exceeds
        # the sum, then remove
        # the starting elements
        while curr_sum > sum and start < i - 1:
            curr_sum = curr_sum - array[start]
            start += 1

        # If curr_sum becomes
        # equal to sum, then
        # return true
        if curr_sum == sum:
            return (start + 1, i)

        # Add this element
        # to curr_sum
        if i < n:
            curr_sum = curr_sum + array[i]
        i += 1

    return (-1,)




arr1 = [1, 2, 3, 7, 5]
print(*getIndexSubArrOfSum(len(arr1), 12, arr1))
print(*getIndexSubArrOfSum_htbl(len(arr1), 12, arr1))
