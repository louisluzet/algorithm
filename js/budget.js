// 프로그래머스 예산 문제
d = [1, 3, 2, 4, 5];
budget = 9;
function solution(d, budget) {
    d.sort();
    let count = d.reduce((cnt=0, i) => {
        if (budget > 0) {
          budget = budget - i;
          cnt++;
          console.log(cnt);
        }
        return cnt;
    });
    return count;
}
console.log(solution(d, budget));