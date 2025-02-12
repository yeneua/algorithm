T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    stone = list(map(int, input().split()))

    for _ in range(M):
        idx, round = map(int, input().split())
        for k in range(round-1):
            if idx+k <= N-1:
                stone[idx+k] = stone[idx-1]

    print(f'#{tc}', end=' ')
    for s in stone:
        print(s, end=' ')
    print()
