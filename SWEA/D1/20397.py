T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    stone = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        for k in range(1, j+1):
            if 0 <= i-1-k < N and 0 <= i-1+k < N:
                if stone[i-1-k] == stone[i-1+k]:
                    stone[i-1-k] = int(not stone[i-1-k])
                    stone[i-1+k] = int(not stone[i-1+k])
    print(f'#{tc}',*stone)
