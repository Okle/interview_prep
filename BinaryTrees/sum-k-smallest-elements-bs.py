# A Binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def addNodeToTree(root, node):

    if root is None:
        return

    if node.data > root.data:

        if root.right is None:
            root.right = node
        else:
            return addNodeToTree(root.right, node)

    else:

        if root.left is None:
            root.left = node
        else:
            return addNodeToTree(root.left, node)



def findSmallestKSum(root, k):

    if root is None or k.data <= 0:
        return 0

    k.data - 1
    res = findSmallestKSum(root.left, k)
    if 0 >= k.data:
        return res

    res += root.data
    k.data -= 1

    if 0 >= k.data:
        return res

    k.data - 1
    return res + findSmallestKSum(root.right, k)



arr = [20, 8, 4, 12, 10, 14, 22]
root = Node(20)
for i in range(1, len(arr)):
    addNodeToTree(root, Node(arr[i]))
print(findSmallestKSum(root, Node(3)))







