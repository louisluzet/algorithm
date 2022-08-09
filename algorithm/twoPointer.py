array = [0, 900, 0, 200, 50, 150, 20, 30]
m = 420

array = list(reversed(array))
length = len(array)
sum = 0
end = 0
result = 0
for start in range(length):
  while sum <= m and end < length:
    sum += array[end]
    end += 1
  result = max(result, end - start)
print(result)