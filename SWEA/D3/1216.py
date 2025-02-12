for _ in range(1, 11):
    tc = int(input())
    text = [list(input()) for _ in range(100)]

    max_length = 0

    for N in range(1, 101): # 회문 길이가 1 ~ 100 모두 탐색

        for i in range(100):
            for j in range(100-N+1):
                length = 0
                for k in range(N//2):
                    if text[i][j+k] != text[i][j+N-1-k]:
                        break
                else:
                    length = N
                if max_length < length:
                    max_length = length
        
        for j in range(100):
            for i in range(100-N+1):
                length = 0
                for k in range(N//2):
                    if text[i+k][j] != text[i+N-1-k][j]:
                        break
                else:
                    length = N
                if max_length < length:
                    max_length = length

    print(f'#{tc} {max_length}')