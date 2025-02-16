T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    counts = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_sum = 0
            for k in range(M):
                for l in range(M):
                    temp_sum += flies[i+k][j+l]
            counts.append(temp_sum)
    print(f'#{tc} {max(counts)}')