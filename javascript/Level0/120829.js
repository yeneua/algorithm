// 각도기
function solution(angle) {
  var answer = 0;
  if (angle < 90) {
    answer = 1;
  } else if (angle == 90) {
    answer = 2;
  } else if (angle < 180) {
    answer = 3;
  } else {
    answer = 4;
  }
  return answer;
}

const solution = (angle) =>
  angle < 90 ? 1 : angle == 90 ? 2 : angle < 180 ? 3 : 4;
