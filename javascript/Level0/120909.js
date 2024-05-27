// 제곱수 판별하기
function solution(n) {
  var answer = 0;
  for (i = 1; i < n; i++) {
    if (n / i == i) {
      answer = 1;
      break;
    } else {
      answer = 2;
    }
  }
  return answer;
}
