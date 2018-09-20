
# The integers are in the range 1..n
# The list has a length of n+1

def find_duplicates(arr):

    s = set()

    for num in arr:

        if num is not None:

            if num in s:
                print(num)
            else:
                s.add(num)

def find_duplicates_1(arr):

    start_index = 0
    num = arr[start_index]

    while start_index < len(arr):

        if num is None:
            num = arr[start_index]
            if num == 0:
                num = None
                start_index += 1
        else:
            if arr[num] == 0:
                print(num)
                num = None
                start_index += 1
            else:
                arr[num], num = 0, arr[num]







arr = [1, 2, 2, 3, 4, 5, 5]
# find_duplicates(arr)
print()
# find_duplicates_1(arr)
print()
arr = [3, 4, 2, 3, 1, 5]
#arr = [1, 2, 1]
find_duplicates_1(arr)


