# A iterative python program to find LCA of two nodes n1 and n2 in binary search tree BST

# A Binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca_iter(root_node, n1, n2):

    while root_node is not None:

        # If both n1 and n2 are smaller than root, then LCA lies in left
        if root_node.data > n1 and root_node.data > n2:
            root_node = root_node.left

        # If both n1 and n2 are greater than root, then LCA lies in right
        elif root_node.data < n1 and root_node.data < n2:
            root_node = root_node.right

        else:
            break

    return root_node

# Let us construct the BST shown in the figure
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10
n2 = 14
t = lca_iter(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

n1 = 14
n2 = 8
t = lca_iter(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

n1 = 10
n2 = 22
t = lca_iter(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

print('++++++++++')


# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca_rec(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if root.data > n1 and root.data > n2:
        return lca_rec(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if root.data < n1 and root.data < n2:
        return lca_rec(root.right, n1, n2)

    return root


n1 = 10
n2 = 14
t = lca_rec(root, n1, n2)
print("LCA of %d and %d is %d" %(n1, n2, t.data))

n1 = 14
n2 = 8
t = lca_rec(root, n1, n2)
print("LCA of %d and %d is %d" %(n1, n2 , t.data))

n1 = 10
n2 = 22
t = lca_rec(root, n1, n2)
print("LCA of %d and %d is %d" %(n1, n2, t.data))

print('++++++++++')


def build_array(n):

    array = list()
    if n.left is not None:
        array.extend(build_array(n.left))

    array.append(n)

    if n.right is not None:
        array.extend(build_array(n.right))

    return array

def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right

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


# ret_list = build_array(root)

# print(len(ret_list))
# print([item.data for item in ret_list])
# print(checkIfArraySorted(ret_list))
# print(checkBST(root, -sys.maxsize, sys.maxsize))


# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
def findPath_rec(root_node, path, k):

    # Baes Case
    if root_node is None:
        return False

    # Store this node in path vector. The node will be
    # removed if not in path from root to k
    path.append(root_node.data)

    # See if the k is same as root's key
    if root_node.data == k:
        return True

    # Check if k is found in left or right sub-tree
    if ((root_node.left != None and findPath_rec(root_node.left, path, k)) or
            (root_node.right != None and findPath_rec(root_node.right, path, k))):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False
    path.pop()
    return False

def binary_tree_LCA(root_node, n1, n2):

    path1 = []
    findPath_rec(root_node, path1, n1)

    path2 = []
    findPath_rec(root_node, path2, n2)

    for temp1 in reversed(path1):
        for temp2 in reversed(path2):
            if temp1 == temp2:
                return temp1


    return None


n1 = 10
n2 = 14
t = binary_tree_LCA(root, n1, n2)
print("LCA of %d and %d is %s" %(n1, n2, str(t)))

n1 = 14
n2 = 8
t = binary_tree_LCA(root, n1, n2)
print("LCA of %d and %d is %s" %(n1, n2, str(t)))

n1 = 10
n2 = 22
t = binary_tree_LCA(root, n1, n2)
print("LCA of %d and %d is %s" %(n1, n2, str(t)))

print('++++++++++++')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


n1 = 4
n2 = 5
t = binary_tree_LCA(root, n1, n2)
print("LCA of %d and %d is %s" %(n1, n2, str(t)))

n1 = 4
n2 = 6
t = binary_tree_LCA(root, n1, n2)
print("LCA of %d and %d is %s" %(n1, n2, str(t)))

n1 = 3
n2 = 4
t = binary_tree_LCA(root, n1, n2)
print("LCA of %d and %d is %s" %(n1, n2, str(t)))

n1 = 2
n2 = 4
t = binary_tree_LCA(root, n1, n2)
print("LCA of %d and %d is %s" %(n1, n2, str(t)))


print('+++++++++')

def show_left(root):

    if root == None:
        return

    print(root.data)

    if root.left == None:
        return

    show_left(root.left)

    if root.right == None:
        return

    show_left(root.right.left)



show_left(root)


