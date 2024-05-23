// 머쓱이보다 키 큰 사람
function solution(array, height) {
  var answer = 0;
  for (i in array) {
    if (height < array[i]) answer += 1;
  }
  return answer;
}
