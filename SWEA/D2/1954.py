# 첫 번째 풀이
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    d = 0 # 방향
    r = 0 # 시작 행 좌표
    c = 0 # 시작 열 좌표
    i = 1 # 들어갈 숫자 1~N
    count = 0 # 이웃한 4칸 모두 0이 아닐 경우 빠져나오게 하기 위한 변수

    snail[r][c] = i # 시작 좌표에 시작값(1)

    while True:
        nr = r + dx[d] # 방향만큼 움직이기
        nc = c + dy[d] # 방향만큼 움직이기
        if nr < N and nc < N and snail[nr][nc] == 0: # 움직인 좌표가 N 범위 이내 and 값이 0으로 비어있는 경우
            i += 1
            snail[nr][nc] = i # 1 더한 값을 넣음
            r = nr # 좌표 업데이트
            c = nc # 좌표 업데이트
            count = 0
        else:
            d += 1 # 움직인 좌표가 범위를 벗어나거나 값이 이미 있는 경우 방향 바꾸기(우->하->좌->상)
            count += 1 # 이웃한 4칸 확인
        
        if d == 4: # 방향 인덱스가 4가 되면 0으로(우->하->좌->상)
            d = 0

        if count == 4: # 이웃한 4칸이 모두 값이 들어있으면(마지막 칸) 빠져나가기
            break

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()


# 두 번째 풀이(6/3)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    num = 1
    r = c = 0
    
    arr[r][c] = num
    num += 1
    
    while num <= N**2:
        for d in range(4):
            while True:
                nr = r+dr[d]
                nc = c+dc[d]
                
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    break
                
                if arr[nr][nc] != 0: # 이미 숫자가 들어가있다면 break
                    break
                
                arr[nr][nc] = num
                num += 1
                r, c = nr, nc
            
    print(f'#{tc}')
    for row in arr:
        print(*row)
