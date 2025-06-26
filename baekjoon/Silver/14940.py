from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

q = deque()
visited = [[-1] * M for _ in range(N)] # visited 배열 -1로 초기화 -> 시작(2)을 0으로 하기 위해서

for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            q.append((i,j)) # 시작점 추가
            visited[i][j] = 0

while q:
    r, c = q.popleft() # r, c : 현재 위치
    
    for d in range(4):
        nr = r+dr[d]
        nc = c+dc[d]
        
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        
        if maps[nr][nc] == 0:
            visited[nr][nc] = 0
            continue
        
        if visited[nr][nc] == -1:
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr,nc))

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0: # 원래 땅이 아닌 부분 0으로 표시
            visited[i][j] = 0

for row in visited:
    print(*row)
