# ai hw 1 problem 1
import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {
    0: [5],
    1: [2,6],
    2: [1,3],
    3: [2,8],
    4: [9],
    5: [0,10],
    6: [1,11],
    7: [8],
    8: [3,7,13],
    9: [4,14],
    10: [5,15],
    11: [6,16],
    12: [13],
    13: [8,12,14],
    14: [9,13,19],
    15: [10,16,20],
    16: [11,15,17,21],
    17: [16],
    18: [19],
    19: [14,18,24],
    20: [15],
    21: [16,22],
    22: [21,23],
    23: [22,24],
    24: [19,23]
}
print("Breadth First Traversal: ")
bfs(graph, 0)