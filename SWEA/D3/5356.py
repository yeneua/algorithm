T = int(input())

for tc in range(1, T+1):
    words = [list(input()) for _ in range(5)]
    result = ''

    # 다섯 줄 중 가장 긴 행 길이 저장
    N = 0
    for k in range(5):
        if N < len(words[k]):
            N = len(words[k])

    # 가장 긴 행 길이에 맞춰 나머지 행에 빈 문자열 append
    for k in range(5):
        if len(words[k]) < N:
            for _ in range(N-len(words[k])):
                words[k].append("")

    for j in range(N):
        for i in range(5):
            result += words[i][j]

    print(f'#{tc} {result}')

'''
제일 긴 행 길에 맞춰서
나머지 행에 공백 append
그리고 공백 제거
'''
