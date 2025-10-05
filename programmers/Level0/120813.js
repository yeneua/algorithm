// 짝수는 싫어요
function solution(n) {
  var answer = [];
  for (i = 1; i <= n; i += 2) {
    answer.push(i);
  }
  return answer;
}
