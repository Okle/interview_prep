def findPair(arr, sum):

    pairSet = set()

    for i in range(len(arr)):
        comp = sum - arr[i]
        if comp in pairSet:
            return True
        else:
            pairSet.add(comp)

    return False




arr = [1,2,3,9]

arr1 = [1,2,4,4]

print(findPair(arr, 8))
print(findPair(arr1, 8))

