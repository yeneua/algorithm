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
            for d in range(4):
                if 0 <= i+dr[d] < N and 0 <= j+dc[d] < M:
                    sum += ballons[i+dr[d]][j+dc[d]]
            if max_sum < sum:
                max_sum = sum

    print(f'#{tc} {max_sum}')