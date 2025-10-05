// n의 배수 고르기
function solution(n, numlist) {
  var answer = [];
  for (i in numlist) {
    if (numlist[i] % n == 0) {
      answer.push(numlist[i]);
    }
  }
  return answer;
}
