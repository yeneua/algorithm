// 삼각형의 완성조건 (1)
function solution(sides) {
  var answer = 0;
  var sum = 0;
  sides.forEach((side) => {
    sum += side;
  });
  answer = sum - 2 * Math.max(...sides) > 0 ? 1 : 2; // 가장 큰 수 < 전체합 - 가장 큰 수 => 0 < 전체합 - 2 * 가장 큰 수
  return answer;
}
