from collections import defaultdict
def solution(id_list, report, k):
    answer = [];
    item = defaultdict(set);
    cnt = defaultdict(int);
    report = list(set(report));
    
    for i in report:
        a, b = i.split();
        item[a].add(b);
        cnt[b] += 1;
    for i in id_list:
        result = 0;
        for j in item[i]:
            if cnt[j] >= k:
                result += 1;
        answer.append(result);
    
    return answer