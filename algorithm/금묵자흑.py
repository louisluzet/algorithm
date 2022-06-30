n ,k= input().split()
n = int(n)
k = int(k)
num_list = list(map(int, input().split()))
result = n//k
temp = n//k + n%k
while temp > k:
  result += temp//k
  temp = temp//k + temp%k
print(result+1)
