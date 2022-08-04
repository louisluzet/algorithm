# 이코테 이진 탐색 중 파라메트릭 활용 문제

#떡볶이 떡 만들기

n = 4
m = 5
array = [19, 15, 10, 17]

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
