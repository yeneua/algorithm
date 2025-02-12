T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    photo = [list(map(int, input().split())) for _ in range(N)]

    max_object = -1

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    for i in range(N): # 행
        for j in range(M): # 열
            if photo[i][j] == 1:
                for d in range(4): # 방향(우하좌상)
                    count = 1
                    nr = i
                    nc = j
                    while True:
                        nr += dr[d]
                        nc += dc[d]
                        if 0 <= nr < N and 0 <= nc < M and photo[nr][nc]:
                            count += 1
                        else:
                            break
                    if max_object < count:
                        max_object = count
            else:
                continue

    print(f'#{tc} {max_object}')
