from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

result = -1

dr = [0,1,0,-1] # 우하좌상
dc = [1,0,-1,0]

q = deque()
visited = [[[0,0] for _ in range(M)] for _ in range(N)] # [벽 안부수고 가는 길, 벽 부수고 가는 길]

q.append((0,0,0))
visited[0][0][0] = 1

while q:
    r, c, wall = q.popleft()
    
    if (r,c) == (N-1, M-1):
        result =  visited[r][c][wall]
        break
    
    for d in range(4):
        nr = r+dr[d]
        nc = c+dc[d]
        
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        
        if maps[nr][nc] == 0 and visited[nr][nc][wall] == 0: # 벽이 아니면 그냥 진행(가던길로)
            visited[nr][nc][wall] = visited[r][c][wall] + 1
            q.append((nr,nc,wall))

        if wall == 0 and maps[nr][nc] == 1: # 벽을 부순 적이 없는데 벽이라면 부순다
            visited[nr][nc][1] = visited[r][c][0] + 1
            q.append((nr,nc,1))

print(result)
