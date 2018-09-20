# Find all permutation of smaller string in a bigger one

def reset(string):

    temp_str = dict()

    for char in string:
        if char in temp_str.keys():
            temp_str[char] = temp_str[char] + 1
        else:
            temp_str[char] = 1

    return temp_str

def findAllPermutOfSinB(small_str, big_str):

    temp_str = reset(small_str)

    count = 0
    j = 0
    while j < len(big_str):

        found = True
        for i in range(j, len(small_str) + j):

            if i < len(big_str) and big_str[i] in temp_str.keys() and temp_str[big_str[i]] > 0:
                temp_str[big_str[i]] -= 1
            else:
                found = False
                break

        if found:
            for key, item in temp_str.items():
                if item != 0:
                    found = False
                    break
        if found:
            count += 1

        temp_str = reset(small_str)

        j += 1

    return count

# print(findAllPermutOfSinB('12', 's12k21jdhfjkds212'))

# print all permutation of the string. Duplicates allowed

def toString(List):
    return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute_backtrack(string, start, end):
    if start == end:
        print(toString(string))
    else:
        for i in range(start, end + 1):
            string[start], string[i] = string[i], string[start]
            permute_backtrack(string, start + 1, end)
            string[start], string[i] = string[i], string[start]  # backtrack


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('123')
for p in permutation(data):
    print(p)

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
#permute_backtrack(a, 0, n - 1)


def permutations(string):
        if len(string) == 0:
            return []

        if len(string) == 1:
            return string

        # get all permutations of length N-1
        perms = permutations(string[1:])
        char = string[0]
        result = []
        # iterate over all permutations of length N-1
        for perm in perms:
            # insert the character into every possible location
            for i in range(len(perm) + 1):
                result.append(perm[:i] + char + perm[i:])

        print(result)
        return result


# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


data = list('123')
for p in permutation(data):
    print(p)

