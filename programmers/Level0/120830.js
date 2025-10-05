// 양꼬치
function solution(n, k) {
  var answer = 0;
  drinks = Math.floor(n / 10); // 서비스 음료 개수
  if (k <= drinks) {
    answer = n * 12000;
  } else {
    answer = n * 12000 + (k - drinks) * 2000;
  }
  return answer;
}
