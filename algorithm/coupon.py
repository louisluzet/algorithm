t = int(input())
arr = [list(map(int, input().split())) for i in range(t)]
result = []
for i in arr:
  temp = 0
  if i[0] >= 5:
    temp +=