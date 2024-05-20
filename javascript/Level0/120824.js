// 짝수 홀수 개수
function solution(num_list) {
  var answer = [];
  var odd = 0;
  var even = 0;
  for (i in num_list) {
    if (num_list[i] % 2 == 1) {
      odd += 1;
    } else {
      even += 1;
    }
  }
  answer.push(even, odd);
  return answer;
}
