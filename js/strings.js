// 프로그래머스 "문자열 내 마음대로 정렬하기" 문제

// 내가 푼 풀이
function solution(strings, n) {
    const newArr = strings.map(i => i[n]);
    const idx = [...newArr];
    idx.sort();
    let answer = newArr.map(i => {
        return strings[idx.indexOf(i)];
    });
    return answer;
}
// 동일한 값일 경우 문자열 자체의 사전 순 정렬을 처리하지 못함

// 다른 사람의 풀이
function solution(strings, n) {
  return strings.sort((a, b) => {
    if (a[n] < b[n]) return -1;
    if (a[n] > b[n]) return 1;
    if (a[n] === b[n]) return a < b ? -1 : 1;
    return 0;
  });
}
// 정렬 조건에 함수를 주어 처리

// 또 다른 사람의 풀이
function solution(strings, n) {
    // strings 배열
    // n 번째 문자열 비교
    return strings.sort((s1, s2) => s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n]));
}

// 정렬 조건 학습
const arr = [2, 1, 6, 3, 5];
arr.sort((a, b) => {
  if (a > b) return 1;
  if (a < b) return -1;
});
console.log(arr);
