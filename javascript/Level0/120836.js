// 순서쌍의 개수
function solution(n) {
  var answer = 0;
  for (i = 0; i <= n; i++) {
    if (n % i == 0) {
      answer += 1;
    }
  }
  return answer;
}
