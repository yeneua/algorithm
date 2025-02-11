T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ballons = [list(map(int, input().split())) for _ in range(N)]

    dr = [0,1,0,-1] # 우하좌상
    dc = [1,0,-1,0]

    max_sum = float('-inf')

    for i in range(N):
        for j in range(M):
            sum = ballons[i][j]
            for d in range(0,4):
                for k in range(ballons[i][j]):
                    nr = i+dr[d]*(k+1)
                    nc = j+dc[d]*(k+1)
                    if 0 <= nr < N and 0 <= nc < M:
                        sum += ballons[nr][nc]
            if max_sum < sum:
                max_sum = sum
    
    print(f'#{tc} {max_sum}')
