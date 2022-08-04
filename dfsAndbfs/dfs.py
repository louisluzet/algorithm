graph = {
  'A': ['B',  'E',  'I'],
  'B': ['A',  'C'],
  'C': ['B',  'D'],
  'D': ['C'],
  'E': ['A',  'F',  'H'],
  'F': ['E',  'G'],
  'G':  ['F'],
  'H': ['E'],
  'I': ['A',  'J'],
  'J': ['I']
};
visited = {key: False for key in graph}

def dfs(graph, visited, v):
  visited[v] = True
  print(v, end=" ")
  for i in graph[v]:
    if visited[i] == False:
      dfs(graph, visited, i)

dfs(graph, visited, 'A')
