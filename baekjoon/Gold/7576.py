from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

q = deque()
isPossible = True # 모든 토마토가 익는 게 가능한지 나타내는 flag 변수
days = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i,j))

while q:
    r, c = q.popleft()
    
    for d in range(4):
        nr = r+dr[d]
        nc = c+dc[d]
        
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        
        if tomato[nr][nc] == -1:
            continue
        
        if tomato[nr][nc] == 0:
            tomato[nr][nc] = tomato[r][c] + 1
            q.append((nr, nc))
        
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0: # 안 익은 토마토가 하나라도 있는 경우
            isPossible = False
        days = max(tomato[i][j], days)

if isPossible:
    print(days-1)
else:
    print('-1')