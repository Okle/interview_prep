from collections import defaultdict
from queue import *

# Complete the maxRegion function below.
def get_children(grid, key):

    children = list()
    for i in range(-1,2):
        for j in range(-1,2):
            x = key[0]
            y = key[1]
            if x + i >= 0 and x + i < len(grid) and y + j >= 0 and y + j < len(grid[0]):
                children.append((x + i, y + j))
    return children

def maxRegion_BFS(grid):

    visited = set()
    prev_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                childeren_to_visit = Queue()
                childeren_to_visit.put((i, j))
                count = check_cell(grid, visited, childeren_to_visit)
                prev_count = max(prev_count, count)

    return prev_count


def check_cell(grid, visited, childeren_to_visit):
    count = 0
    while not childeren_to_visit.empty():
        key = childeren_to_visit.get()
        if key not in visited:
            visited.add(key)
            if grid[key[0]][key[1]] == 1:
                count += 1
                for child in get_children(grid, key):
                    childeren_to_visit.put(child)

    return count


def maxRegion_DFS(grid):

    prev_count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                region_size = dfs_check_cell(grid, i, j)
                prev_count = max(prev_count, region_size)

    return prev_count

def dfs_check_cell(grid, row, column):

    if row < 0 or row >= len(grid) or 0 > column or column >= len(grid[0]):
        return 0

    if grid[row][column] == 0:
        return 0

    grid[row][column] = 0
    size = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != row or j != column:
                size = size + dfs_check_cell(grid, row + i, column + j)

    return size


grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
#grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
grid = [[1, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 0, 0, 1]]
# print(maxRegion_BFS(grid))
# print(maxRegion_DFS(grid))


# 1 0 1 1 0
# 1 1 0 0 1
# 0 1 1 1 0
# 0 0 0 0 1
# 1 1 1 0 0

class Node:

    def __init__(self, id):
        self.id = id
        self.children = dict()

    def __repr__(self):
        return str(self.id)


class Graph:
    def __init__(self, num_of_nodes):
        self.n = num_of_nodes
        self.nodes = [None] * num_of_nodes
        for i in range(num_of_nodes):
            self.nodes[i] = Node(i + 1)

    def connect(self, x, y):
        node_x = self.nodes[x]
        node_y = self.nodes[y]
        node_y.children[node_x.id] = node_x
        node_x.children[node_y.id] = node_y

    def find_all_distances_DFS(self, start):
        distance = [-1] * (self.n)
        visited = set()
        s_node = self.nodes[start]
        visited.add(s_node.id)
        distance[s_node.id - 1] = 0
        self.helper_DFS(s_node, distance, visited)

        distance = distance[:start] + distance[start + 1:]
        print(*distance)

    def helper_DFS(self, start_node, distance, visited):
        if start_node is not None and len(start_node.children) > 0:
            for child_id, child in start_node.children.items():
                if child.id not in visited:
                    distance[child.id - 1] = distance[start_node.id - 1] + 6
                    visited.add(child.id)
                    self.helper_DFS(child, distance, visited)

    def find_all_distances(self, start):
        distance = [-1] * (self.n)
        visited = set()
        s_node = self.nodes[start]
        next_to_visite = Queue()
        next_to_visite.put(s_node)
        distance[s_node.id - 1] = 0
        while not next_to_visite.empty():
            node = next_to_visite.get()
            if node.id not in visited:
                visited.add(node.id)
                for child_id, child in node.children.items():
                    if child.id not in visited:
                        next_to_visite.put(child)
                        distance[child.id - 1] = 6 + distance[node.id - 1]

        distance = distance[:start] + distance[start + 1:]
        print(*distance)


class Graph:

    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.n)]
        unvisited = set([i for i in range(self.n)])
        q = Queue()

        distances[root] = 0
        unvisited.remove(root)
        q.put(root)

        while not q.empty():
            node = q.get()
            children = self.edges[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.put(child)

        distances.pop(root)

        print(" ".join(map(str, distances)))

def test(n, m, arr, s):

    graph = Graph(n)
    for i in range(m):
        x, y = arr[i][0], arr[i][1]
        graph.connect(x - 1, y - 1)
    return graph.find_all_distances(s - 1)
#   return graph.find_all_distances_DFS(s - 1)




arr = [(1, 2), (1, 3)]
#print(* test(4, 2, arr, 1))


arr = [(1, 2), (1, 3), (3, 4), (2, 5)]
test(7, 4, arr, 2)






