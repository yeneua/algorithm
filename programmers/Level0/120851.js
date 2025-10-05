// 숨어있는 숫자의 덧셈 (1)
function solution(my_string) {
  var answer = 0;
  for (i = 0; i < my_string.length; i++) {
    if (!isNaN(my_string[i])) {
      answer += Number(my_string[i]); // string을 숫자형으로 변환
    }
  }
  return answer;
}
