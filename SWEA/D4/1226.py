from collections import deque

N = 16

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def find_start_point(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return (i,j)

def solve_maze(maze):
    sr, sc = find_start_point(maze)

    visited =[[0] * 16 for _ in range(16)]
    q = deque()

    q.append((sr,sc))
    visited[sr][sc] = 1

    while q:
        r,c = q.popleft()
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == 3:
                    return 1
                if visited[nr][nc] == 0 and maze[nr][nc] ==0:
                    q.append((nr,nc))
                    visited[nr][nc] = visited[r][c] + 1 # 방문표시 + 거리계산
    return 0


for _ in range(10):
    tc = input()
    maze = [list(map(int, input())) for _ in range(16)]
    print(f'#{tc} {solve_maze(maze)}')
