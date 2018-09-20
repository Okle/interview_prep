# O(n) solution for finding smallest
# subarray with sum greater than x

# Returns length of smallest subarray
# with sum greater than x. If there
# is no subarray with given sum, then
# returns n + 1
def smallestSubWithSum(arr, n, x):
    # Initialize current sum and minimum length
    curr_sum = 0
    min_len = n + 1

    # Initialize starting and ending indexes
    start = 0
    end = 0
    while (end < n):

        # Keep adding array elements while current
        # sum is smaller than x
        while (curr_sum <= x and end < n):
            curr_sum += arr[end]
            end += 1

        # If current sum becomes greater than x.
        while (curr_sum > x and start < end):

            # Update minimum length if needed
            if (end - start < min_len):
                min_len = end - start

                # remove starting elements
            curr_sum -= arr[start]
            start += 1

    return min_len
