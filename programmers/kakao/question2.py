# 2026 카카오그룹 신입크루 공채 1차 코딩테스트

import math

def solution(signals):
    answer = 0
    scope = []
    colors = []

    for signal in signals:
        scope.append(sum(signal))

        temp = []

        for k in range(len(signal)):
            if k == 0:
                temp.extend(['G'] * signal[0])
            elif k == 1:
                temp.extend(['Y'] * signal[1])
            elif k == 2:
                temp.extend(['R'] * signal[2])
        colors.append(temp)

    for i in range(math.prod(scope)):
        temp = ''
        for j in range(len(signals)):
            second = i % scope[j]
            color = colors[j][second]
            temp += color
        if temp == 'Y' * len(signals):
            answer = i + 1
            break
    else:
        answer = -1

    return answer