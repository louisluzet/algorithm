def main() :
  result = []
  num = int(input())
  arr = list(map(int ,input().split()))
  arr.sort()
  for i in arr:
    if len(result) == 0 : result.append(i)
    if i not in result: result.append(i)
  if len(result) >= 3: print('YES')
  else: print('NO')
main()