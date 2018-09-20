# Let 1 represent ‘A’, 2 represents ‘B’, etc.
# Given a digit sequence, count the number of possible decodings of the given digit sequence.
#
# Examples:
#
# Input:  digits[] = "121"
# Output: 3
# // The possible decodings are "ABA", "AU", "LA"
#
# Input: digits[] = "1234"
# Output: 3
# // The possible decodings are "ABCD", "LCD", "AWD"
# An empty digit sequence is considered to have one decoding.
# It may be assumed that the input contains valid digits from 0 to 9
# and there are no leading 0’s, no extra trailing 0’s and no two or more consecutive 0’s.
# #
# This problem is recursive and can be broken in sub-problems.
# We start from end of the given digit sequence. We initialize the total count of decodings as 0.
# We recur for two subproblems.
# 1) If the last digit is non-zero, recur for remaining (n-1) digits and add the result to total count.
# 2) If the last two digits form a valid character (or smaller than 27),
#       recur for remaining (n-2) digits and add the result to total count.
#

# Given a digit sequence of length n
# returns count of possible decodings by replacing 1 with A, 2 woth B, ...26 with Z

def countDecoding_rec(digits, n):


    # base cases
    if n == 0 or n == 1:
        return 1

    # Initialize count
    count = 0

    if digits[n - 1] > '0':
        count = countDecoding_rec(digits, n - 1)

    if digits[n - 2] == '1' or digits[n - 2] == '2' and digits[n - 1] < '7':
        count += countDecoding_rec(digits, n - 2)

    return count


# A Dynamic Programming based
# function to count decodings
def countDecodingDP(digits, n):
    # A table to store results of subproblems
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 1

    for i in range(2, n + 1):

        count[i] = 0

        # If the last digit is not 0,
        # then last digit must add to
        # the number of words
        if digits[i - 1] > '0':
            count[i] = count[i - 1]

        # If second last digit is smaller
        # than 2 and last digit is
        # smaller than 7, then last two
        # digits form a valid character
        if digits[i - 2] == '1' or digits[i - 2] == '2' and digits[i - 1] < '7':
            count[i] += count[i - 2]

    return count[n]

print(countDecodingDP('123', 3))
print(countDecoding_rec('123', 3))