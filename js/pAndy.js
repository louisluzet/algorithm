// 프로그래머스 문자열 내 p와 y의 개수

//통과하지 못한 풀이
function solution(s){
    s = s.toLowerCase();
    if (s.includes("p") == false && s.includes("y") == false) {
        return true;
    } else {
        return s.match(/p/g).length === s.match(/y/g).length;
    }
}
// match보다 split로 분리해서 개수를 새는 것이 더 빠른가봄

// 통과한 풀이
function solution(s){
    s = s.toLowerCase();
    if (s.includes("p") == false && s.includes("y") == false) {
        return true;
    } else {
        return s.split("p").length === s.split("y").length;
    }
}