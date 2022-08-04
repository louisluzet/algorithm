def solution(n):
    answer = 0
    for i in range(2, n+1):
        count = 0
        root = int(i ** 0.5 + 1)
        for j in range(2, root):
            if i % j == 0:
                count = count + 1
        print(i, ' = ', count)
        if count != 0: answer = answer + 1
    return answer

print(solution(10))