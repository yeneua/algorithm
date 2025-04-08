from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maps = [list(input()) for _ in range(N)]

    dr = [0,1,0,-1] # 우하좌상
    dc = [1,0,-1,0]
    
    # 물에서부터 거리
    q = deque()
    visited = [[-1] * M for _ in range(N)] # 물을 0으로 두기 위해서 -1로 둠
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'W':
                q.append((i,j))
                visited[i][j] = 0 # 큐에서 꺼내면서 visited + 1 해주기 위해 물을 0으로 둠
    
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            
            if visited[nr][nc] == -1: # 땅인 곳 찾기
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr,nc)) # 갈 수 있는 곳 푸시
                
    count = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'L':
                count += visited[i][j]
    
    print(f'#{tc} {count}')
