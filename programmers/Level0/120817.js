// 배열의 평균값
function solution(numbers) {
  var answer = 0;
  for (i in numbers) {
    answer += numbers[i];
  }
  answer = answer / numbers.length;
  return answer;
}
