// 가장 큰 수 찾기
function solution(array) {
  var answer = [];
  let number = 0;
  let index = 0;
  for (i = 0; i < array.length; i++) {
    if (array[i] < array[i + 1]) {
      number = array[i + 1];
      index = i + 1;
    }
  }
  answer.push(number, index);
  return answer;
}
