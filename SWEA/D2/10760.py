T = int(input())

for tc in range(1,T+1):
    N,M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    dr = [0,1,1,1,0,-1,-1,-1] # 오른쪽부터 시계 방향
    dc = [1,1,0,-1,-1,-1,0,1]

    result = 0

    for i in range(N):
        for j in range(M):
            count = 0
            for d in range(8):
                if 0 <= i+dr[d] < N and 0 <= j+dc[d] < M:
                    if area[i][j] > area[i+dr[d]][j+dc[d]]:
                        count += 1
            if count >= 4:
                result += 1
                    

    print(f'#{tc} {result}')