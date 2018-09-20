from queue import *

# BFS without path
def isConnected(network, sender, recipient):

    nodes_to_visit = Queue()
    nodes_to_visit.put(sender)

    already_visited = set()
    while not nodes_to_visit.empty():

        node = nodes_to_visit.get()

        if node == recipient:
            return print('Found!!')
            break


        for next_node in network[node]:
            if next_node not in already_visited:
                already_visited.add(node)
                nodes_to_visit.put(next_node)

    return print('Not found!!')


def build_path(nodes_map, end):

    path = list()

    curr_node = end
    while curr_node:
        path.append(curr_node)
        curr_node = nodes_map.get(curr_node)

    path.reverse()
    return path



# BFS with path
def bfs_get_path(graph, start_node, end_node):
    nodes_to_visit = Queue()
    nodes_to_visit.put(start_node)

    # Keep track of what nodes we've already seen
    # so we don't process them twice
    # nodes_already_seen = set([start_node])

    # Keep track of how we got to each node
    # we'll use this to reconstruct the shortest path at the end
    how_we_reached_nodes = {start_node: None}

    while not nodes_to_visit.empty():

        current_node = nodes_to_visit.get()

        # Stop when we reach the end node
        if current_node == end_node:
            # Somehow reconstruct the path here
            return print(build_path(how_we_reached_nodes, end_node))

        for neighbor in graph[current_node]:
            if neighbor not in how_we_reached_nodes.keys():
                # nodes_already_seen.add(neighbor)
                nodes_to_visit.put(neighbor)
                # Keep track of how we got to this node
                how_we_reached_nodes[neighbor] = current_node

    return None



network = {
    'Min': ['William', 'Jayden', 'Omar'],
    'William': ['Min', 'Noam'],
    'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren': ['Jayden', 'Omar'],
    'Amelia': ['Jayden', 'Adam', 'Miguel'],
    'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam': ['Nathan', 'Jayden', 'William'],
    'Omar': ['Ren', 'Min', 'Scott']
}


isConnected(network, 'Jayden', 'Adam')
bfs_get_path(network, 'Jayden', 'Adam')

