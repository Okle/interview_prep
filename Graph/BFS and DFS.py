from collections import deque

# BFS
def bfs(graph, start_node, end_node):


    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    # Keep track of what nodes we've already seen
    # so we don't process them twice
    nodes_already_seen = set([start_node])

    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()

        # Stop when we reach the end node
        if current_node == end_node:
            # Found it!
            break

        for neighbor in graph[current_node]:
            if neighbor not in nodes_already_seen:
                nodes_already_seen.add(neighbor)
                nodes_to_visit.append(neighbor)