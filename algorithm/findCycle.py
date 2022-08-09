# 방향그래프
# s = ['LU', 'RD', 'LD', 'RU', 'LU']
# s = ['LU', 'M', 'RU', 'RD']
s = ['M', 'RD', 'LD', 'M', 'M']

s_dict = {'LU': 0, 'RU': 1, 'LD': 2, 'RD': 3, 'M': 4}

graph = [[] for _ in range(5)]
cycle = False
for i in range(1, len(s)):
    if s[i] == s[0]:
        cycle = True
        break
    graph[s_dict[s[i - 1]]].append(s[i])
print(graph)

if cycle:
    next = graph[s_dict[s[len(s) - 1]]]
    print(next[0])
else:
    print(s[0])
