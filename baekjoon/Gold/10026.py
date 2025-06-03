from collections import deque

N = int(input())
image = [list(input()) for _ in range(N)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

# 적록색약이 아닌 사람
marker = 0
visited = [[0] * N for _ in range(N)]

# 적록색약인 사람
marker_check = 0
visited_check = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            color = image[i][j]
            q = deque()
            marker +=1 # 방문하지 않은 곳일때 marker += 1
            
            q.append((i,j))
            visited[i][j] = marker
            
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r+dr[d]
                    nc = c+dc[d]
                    
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    
                    if visited[nr][nc] == 0 and image[nr][nc] == color: # 방문한 적이 없고 같은 색일때(같은 구역)
                        q.append((nr,nc))
                        visited[nr][nc] = marker
        
        if visited_check[i][j] == 0:
            color_check = image[i][j]
            q = deque()
            marker_check += 1
            
            q.append((i,j))
            visited_check[i][j] = marker_check
            
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r+dr[d]
                    nc = c+dc[d]
                    
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    
                    if visited_check[nr][nc] == 0:
                        if color_check == 'B' and image[nr][nc] == 'B':
                            q.append((nr,nc))
                            visited_check[nr][nc] = marker_check
                        elif color_check == 'R':
                            if image[nr][nc] == 'R' or image[nr][nc] == 'G':
                                q.append((nr,nc))
                                visited_check[nr][nc] = marker_check
                        elif color_check == 'G':
                            if image[nr][nc] == 'G' or image[nr][nc] == 'R':
                                q.append((nr,nc))
                                visited_check[nr][nc] = marker_check
                                
print(marker, marker_check) # 마커의 값이 구역의 수
