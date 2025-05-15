from collections import deque

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    fields = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int,input().split())
        fields[j][i] = 1
    
    dr = [0,1,0,-1] # 우하좌상
    dc = [1,0,-1,0]
    
    cabbage = 0
    q = deque()
    visited = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if fields[i][j]:
                cabbage += 1
                q.append((i,j))
                
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        fields[r][c] = 0
                        nr = r+dr[d]
                        nc = c+dc[d]
                        
                        if nr < 0 or nr >= N or nc < 0 or nc >= M:
                            continue
                        
                        if fields[nr][nc] and visited[nr][nc] == 0:
                            q.append((nr,nc))
                            visited[nr][nc]=1
            else:
                continue
    
    print(cabbage)

# 1이면(배추가 심어져있으면) 연결된 배추 q에 담고 꺼내면서 0으로 바꾸기
# 메모리 초과 해결 -> visited 배열 사용
