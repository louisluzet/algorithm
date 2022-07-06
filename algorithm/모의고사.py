from collections import defaultdict
answers = [1, 2, 3, 4, 5]
def solution(answers):
    answer = []
    test = defaultdict(list)
    test[1] = [1, 2, 3, 4, 5]
    test[2] = [2, 1, 2, 3, 2, 4, 2, 5]
    test[3] = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in test:
      
    return test

print(solution(answers))