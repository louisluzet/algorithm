from collections import deque

graph = {
    'A': ['B', 'E', 'I'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C'],
    'E': ['A', 'F', 'H'],
    'F': ['E', 'G'],
    'G': ['F'],
    'H': ['E'],
    'I': ['A', 'J'],
    'J': ['I']
}
visited = {key: False for key in graph}


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


bfs(graph, visited, 'A')
