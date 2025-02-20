from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def find_start_point(N, maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return (i,j)

def solve_maze(N, maze):

    # 방문 여부
    visited =[[0] * N for _ in range(N)]

    # 큐 생성
    q = deque()

    # 시작점 처리
    sr, sc = find_start_point(N, maze)  # 시작점
    q.append((sr,sc))
    visited[sr][sc] = 1

    while q:
        current = q.popleft()
        r = current[0]
        c = current[1]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] == 3:
                return visited[r][c] -1 # 방문 칸 수를 구하는 문제. 출발&도착 칸을 제외하고 지나간 0인 칸 수
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and maze[nr][nc] == 0:
                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {solve_maze(N,maze)}')
