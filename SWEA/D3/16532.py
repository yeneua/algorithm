def find_start(maze,N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i,j
            
def check_route(maze,N):
    sr,sc = find_start(maze,N)

    stack = []
    visited = [[0] * N for _ in range(N)]

    dr = [0,1,0,-1] #우하좌상
    dc = [1,0,-1,0]

    r, c = sr,sc
    visited[r][c] = 1
    stack.append((r,c))

    while True:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and maze[nr][nc] != 1:
                visited[nr][nc] = 1
                stack.append((nr,nc))
                if maze[nr][nc] == 3:
                    return 1
        else:
            if stack:
                r,c = stack.pop()
            else:
                return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {check_route(maze,N)}')