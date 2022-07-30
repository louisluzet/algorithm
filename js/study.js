// 그리디
// 코인문제
// const coins = [500, 100, 50, 10];
// let money = 2370;
// let result = 0;

// coins.forEach((coin) => {
//   result = result + Math.floor((money / coin));
//   money = money % coin;
// });
// console.log(result)

// 정렬 - 숫자가 아닌 문자를 기준으로 하므로 주의
const array = [2, 3, 1, 14, 22];
array1 = array.sort((a, b) => a - b); //오름차순
array2 = array.sort((a, b) => b - a); //내림차순

