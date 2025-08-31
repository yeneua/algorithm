from collections import deque

def get_combi_result(): # 빈 칸 중에서 벽을 세울 3개 조합을 찾는 함수
    def find_wall_combi(cnt, current, start):
        if cnt == 3:
            combi.append(current[:])
            return
        
        for k in range(start, len(empty)):
            current.append(empty[k])
            find_wall_combi(cnt+1, current, k+1)
            current.pop()
    combi = []
    find_wall_combi(0, [], 0)
    return combi

def bfs(lst): # bfs로 퍼져나가는 바이러스 계산 -> input으로 받은 maps를 새로 복사하지 않고 visited 배열을 사용해서 계산
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    q = deque()
    visited = [[0] * M for _ in range(N)]
        
    for virus_element in virus: # 초기 2(바이러스) 영역
        q.append(virus_element)
    
    while q:
        r, c = q.popleft()
        
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if maps[nr][nc] == 1: # 벽이면 continue
                continue
            if maps[nr][nc] == 2: # 이미 바이러스가 있는 칸이면 continue
                continue
            if (nr,nc) in lst: # 새로 벽을 세울 칸이면 continue
                continue
            if visited[nr][nc]: # 이미 방문
                continue
            
            q.append((nr,nc))
            visited[nr][nc] = 1
            
    return visited

def count_virus_zone(lst): # 바이러스가 퍼진 영역 개수 계산
    count = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                count +=1
                
    return count


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

result = 0

empty = [] # 빈 칸 개수
walls = [] # 벽
virus = [] # 바이러스

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            empty.append((i,j))
        elif maps[i][j] == 1:
            walls.append((i,j))
        elif maps[i][j] == 2:
            virus.append((i,j))

combi = get_combi_result()

for new_walls in combi:
    visited = bfs(new_walls)
    count = count_virus_zone(visited)
    result = max(result, len(empty)-3-count) # len(empty) : 초기 빈칸 개수, 3 : 새로 세우는 벽의 개수, count : 바이러스가 퍼져나간 칸의 개수ㄴ

print(result)