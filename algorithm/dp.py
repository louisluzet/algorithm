# 식량창고 문제
# n = 4
# array = [1, 3, 1, 5]

# d = [0] * 100

# d[0] = array[0]
# d[1] = max(array[0], array[1])
# for i in range(2, n):
#     d[i] = max(d[i - 1], d[i - 2] + array[i])

# print(d[n - 1])

# 1로 만들기 문제
# x = int(input())

# d = [0] * 30001
# for i in range(2, x+1):
#   # 현재의 수에서 1을 빼는 경우
#   d[i] = d[i-1] + 1
#   # 2로 나누어떨어지는 경우
#   if i % 2 == 0:
#     d[i] = min(d[i], d[i//2] + 1)
#     # 3으로 나누어떨어지는 경우
#   if i % 3 == 0:
#     d[i] = min(d[i], d[i//3] + 1)
#   if i % 5 == 0:
#     d[i] = min(d[i], d[i//5] + 1)

# print(d[x])

# 효율적인 화폐 구성 문제
# n, m = map(int, input().split())

# array = list(map(int, input().split()))

# d = [10001] * (m + 1)

# d[0] = 0
# for i in range(n):
#     for j in range(m + 1):
#         if d[j - array[i]] != 10001:
#             d[j] = min(d[j], d[j - array[i]] + 1)

# for i in range(m+1):
#   print(d[i])

# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])

# 금광 문제

# 테스트케이스 입력
for tc in range(int(input())):
  n, m = map(int, input().split())
  array = list(map(int, input().split()))
  dp = []
  index = 0
  for i in range(n):
    dp.append(array[index:index + m])
    index += m
  for j in range(1, m):
    for i in range(n):
      # 왼쪽 위에서 오는 경우
      if i == 0: left_up = 0
      else: left_up = dp[i-1][j-1]
      # 왼쪽 아래에서 오는 경우
      if i == n-1: left_down = 0
      else: left_down = dp[i+1][j-1]
      # 왼쪽에서 오는 경우
      left = dp[i][j-1]
      dp[i][j] = dp[i][j] + max(left, left_up, left_down)
  result = 0
  for i in range(n):
    result = max(result, dp[i][m-1])
  print(result)  