T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    dr_across = [-1,1,1,-1] # 우상, 우하, 좌하, 좌상
    dc_across = [1,1,-1,-1]

    counts = []

    # 십자
    for i in range(N):
        for j in range(N):
            temp_sum = flies[i][j]
            for d in range(4):
                for k in range(1, M):
                    nr = i+dr[d]*k
                    nc = j+dc[d]*k
                    if 0 <= nr < N and 0 <= nc < N:
                        temp_sum += flies[nr][nc]
            temp_sum_across = flies[i][j]

            for d in range(4): # 대각선
                for k in range(1, M):
                    nr = i+dr_across[d]*k
                    nc = j+dc_across[d]*k
                    if 0 <= nr < N and 0 <= nc < N:
                        temp_sum_across += flies[nr][nc]
            counts.append(temp_sum)
            counts.append(temp_sum_across)

    print(f'#{tc} {max(counts)}')