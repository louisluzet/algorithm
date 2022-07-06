# 이코테 - 음료수 얼려먹기 문제

# 세로길이 N, 가로길이 M
n, m = map(int, input().split())

# N x M 2차원 배열 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y>= m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    # 상하좌우 모두 재귀적으로 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1
print(result)