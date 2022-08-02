// 프로그래머스 행렬의 덧셈 문제

// 내가 푼 코드
function solution(arr1, arr2) {
    let answer = [];
    for(let i=0; i<arr1.length; i++){
        answer.push([]);
        for(let j=0; j<arr1[0].length; j++){
            let value = arr1[i][j] + arr2[i][j]
            answer[i].push(value);
        }
    }
    return answer;
}

// 다른 사람의 풀이
function sumMatrix(arr1, arr2) {
  return A.map((a,i) => a.map((b, j) => b + B[i][j]));
}