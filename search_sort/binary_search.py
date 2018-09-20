import sys


def binary_search(target, nums):
    """See if target appears in nums"""
    # We think of floor_index and ceiling_index as "walls" around
    # the possible positions of our target so by -1 below we mean
    # to start our wall "to the left" of the 0th index
    # (we *don't* mean "the last index")
    floor_index = -1
    ceiling_index = len(nums)

    # If there isn't at least 1 index between floor and ceiling,
    # we've run out of guesses and the number must not be present
    while floor_index + 1 < ceiling_index:
        # Find the index ~halfway between the floor and ceiling
        # We use integer division, so we'll never get a "half index"
        distance = ceiling_index - floor_index
        half_distance = distance / 2
        guess_index = floor_index + half_distance

        guess_value = nums[guess_index]
        if guess_value == target:
            return True

        if guess_value > target:
            # Target is to the left, so move ceiling to the left
            ceiling_index = guess_index
        else:
            # Target is to the right, so move floor to the right
            floor_index = guess_index

    return False



""" Node is defined as"""
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_array(n):

    array = list()
    if n.left is not None:
        array.extend(build_array(n.left))

    array.append(n)

    if n.right is not None:
        array.extend(build_array(n.right))

    return array


def checkIfArraySorted(array):
    i = 0

    if array is not None and len(array) > 0:
        while i < len(array) - 1:
            if array[i].data >= array[i + 1].data:
                return False
            i += 1
    else:
        return False

    return True


def checkBST(root, min, max):

    if root is None:
        return True

    if min <= root.data >= max:
        return False

    return checkBST(root.left, min, root.data) and checkBST(root.right, root.data, max)


root = node(4)
root.left = node(2)
root.right = node(6)
root.left.left = node(1)
root.left.right = node(3)
root.right.left = node(5)
root.right.right = node(7)
root.right.right.right = node(10)

ret_list = build_array(root)

print(len(ret_list))
print([item.data for item in ret_list])

print(checkIfArraySorted(ret_list))


print(checkBST(root, -sys.maxsize, sys.maxsize))