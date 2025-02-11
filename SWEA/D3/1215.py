for tc in range(1, 11):
    N = 8
    M = int(input())
    text = [list(input()) for _ in range(N)]

    result = 0

    # 1. 행
    for i in range(N):
        for l in range(N-M+1):
            for m in range(M//2):
                if text[i][l+m] != text[i][l+M-1-m]:
                    break
            else:
                result += 1
    # 2. 열
    for j in range(N):
        for l in range(N-M+1):
            for m in range(M//2):
                if text[l+m][j] != text[l+M-1-m][j]:
                    break
            else:
                result += 1

    print(f'#{tc} {result}')
