import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 10억

# 노드의 개수 및 간선 개수 입력받기
n, m = map(int, input().split())
start = int(input())  #시작 노드 입력받기

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # a에서 b로 가는 간선의 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
