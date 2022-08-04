# 이코테 정렬

# 두 배열의 원소 교체 문제
n = 5
k = 3
a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]


def solution(n, k, a, b):
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    return sum(a)


print(solution(n, k, a, b))
