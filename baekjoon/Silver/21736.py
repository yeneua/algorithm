from collections import deque

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]

answer = 0

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            q = deque()
            visited = [[0] * M for _ in range(N)]
            
            q.append((i,j))
            visited[i][j] = 1
            
            while q:
                r,c = q.popleft()
                
                if campus[r][c] == 'P':
                    answer += 1
                
                for d in range(4):
                    nr = r+dr[d]
                    nc = c+dc[d]
                    
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] or campus[nr][nc] == 'X':
                        continue
                    
                    visited[nr][nc] = 1
                    q.append((nr,nc))

if answer == 0:
    print('TT')
else:
    print(answer)