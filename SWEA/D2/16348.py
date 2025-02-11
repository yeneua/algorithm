T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    text = [list(input()) for _ in range(N)]

    palindrome = []

    # 1. 행
    for i in range(N):
        for l in range(N-M+1): # 회문 검사 시작점
            for m in range(M//2): # 회문 검사
                if text[i][l + m] != text[i][l + M - 1 - m]:
                    break
            else:
                palindrome = text[i][l:l+M] # for문을 전부 통과하면 수행

    # 2. 열
    for j in range(N):
        for l in range(N-M+1):
            for m in range(M//2):
                if text[l+m][j] != text[l+M-1-m][j]:
                    break
            else:
                temp = [row[j] for row in text]
                palindrome = temp[l:l+M]

    result = ''.join(palindrome)
    print(f'#{tc} {result}')
