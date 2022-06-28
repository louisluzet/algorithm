# ------- test input ------------
# lottos = [0, 0, 0, 0, 0, 0];
# win_nums = [38, 19, 20, 40, 15, 25];

def find_result(num):
    if num <2:
        return 6
    elif num == 2:
        return 5
    elif num == 3:
        return 4
    elif num == 4:
        return 3
    elif num == 5:
        return 2
    else :
        return 1
def solution(lottos, win_nums):
    answer = [];
    cnt = 0; 
    result = 0;
    result = [i for i in lottos if i in win_nums];
    cnt = [i for i in lottos if i == 0]
    answer.append(find_result(len(result)));
    answer.append(find_result(len(result) + len(cnt)));
    answer.sort();
    return answer
