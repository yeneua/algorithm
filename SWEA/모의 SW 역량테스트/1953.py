from collections import deque
 
T = int(input())
 
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
     
    tunnel = [list(map(int, input().split())) for _ in range(N)]
     
    dr = [0,1,0,-1] #우하좌상
    dc = [1,0,-1,0]
     
    pipe = {1:[0,1,2,3], 2:[1,3], 3:[0,2], 4:[0,3], 5:[0,1], 6:[1,2], 7:[2,3]}
 
    q = deque()
    visited = [[0]*M for _ in range(N)]
     
    def check_direction(d): # 파이프끼리 연결되어 있는지
        if d == 0: # 우 <-> 좌
            return 2
        elif d == 1: # 하 <-> 상
            return 3
        elif d == 2: # 좌 <-> 우
            return 0
        elif d == 3: # 상 <-> 하
            return 1
     
    r = R # r,c : 현재 위치
    c = C
 
    visited[r][c] = 1
    q.append((r,c))
     
    while q:
        r,c = q.popleft()
         
        for d in pipe[tunnel[r][c]]:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and tunnel[nr][nc] != 0 and check_direction(d) in pipe[tunnel[nr][nc]]: # 파이프끼리 방향 연결되어 있어야 함
                visited[nr][nc] = visited[r][c] + 1
                if visited[nr][nc] > L:
                    break
                q.append((nr,nc))
             
    result = 0
    for i in range(N):
        for j in range(M):
            if 1 <= visited[i][j] <= L:
                result += 1
         
    print(f'#{tc} {result}')
