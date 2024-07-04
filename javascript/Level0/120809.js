// 배열 두 배 만들기
function solution(numbers) {
  var answer = [];
  for (i in numbers) {
    answer.push(numbers[i] * 2);
  }
  return answer;
}
