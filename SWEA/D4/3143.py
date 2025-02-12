T = int(input())
for tc in range(1, T+1):

    text, pattern = input().split()

    t = 0
    p = 0
    count = 0
    result = 0

    # 일치하는 문자열 개수 구하기
    while t < len(text):
        if text[t] != pattern[p]:
            t = t - p + 1
            p = 0
        else:
            t += 1
            p += 1
        if p == len(pattern):
            count += 1
            p = 0

    # + 남은 문자열 개수
    result = count + len(text)-len(pattern)*count
    print(f'#{tc} {result}')
