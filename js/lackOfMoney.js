// 내가 푼 풀이
function solution(price, money, count) {
    let sum = 0;
    for(let i = 1; i <= count; i++) {
        sum += i * price;
    }
    return sum < money ? 0 : sum-money;
}

// 다른 사람의 풀이
function solution(price, money, count) {
    const tmp = price * count * (count + 1) / 2 - money;
    return tmp > 0 ? tmp : 0;
}
// 한줄로 전체 값 계산
