# graph = {
#   'A': ['B',  'E',  'I'],
#   'B': ['A',  'C'],
#   'C': ['B',  'D'],
#   'D': ['C'],
#   'E': ['A',  'F',  'H'],
#   'F': ['E',  'G'],
#   'G':  ['F'],
#   'H': ['E'],
#   'I': ['A',  'J'],
#   'J': ['I']
# };
# visited = {key: False for key in graph}

# def dfs(graph, visited, v):
#   visited[v] = True
#   print(v, end=" ")
#   for i in graph[v]:
#     if visited[i] == False:
#       dfs(graph, visited, i)

# dfs(graph, visited, 'A')

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i].append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)  # 좌
        dfs(x, y - 1)  # 하
        dfs(x + 1, y)  # 우
        dfs(x, y + 1)  # 상
        print(graph)
        return True
    return False

# 모든 노드에 대하여 음료 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
