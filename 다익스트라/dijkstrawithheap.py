import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

# 모든 간선 정보 입력받기
for _ in range(m):
    # a에서 b로 가는 간선의 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작노드로 가기 위한 최단경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    # distance[start]
