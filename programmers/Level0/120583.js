// 중복된 숫자 개수
function solution(array, n) {
  var answer = 0;
  for (i in array) {
    if (array[i] == n) {
      answer += 1;
    }
  }
  return answer;
}
