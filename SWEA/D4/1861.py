# 첫 번째 풀이
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    dr = [0,1,0,-1] # 우하좌상
    dc = [1,0,-1,0]

    max_count = 0
    max_value = 0

    for r in range(N):
        for c in range(N): # r,c : 방 시작 번호
            q = deque()
            visited = [[0] * N for _ in range(N)] # 방문 여부

            # 시작점 처리
            count = 1
            q.append((r,c))
            visited[r][c] =1

            while q: # bfs로 구현
                now_r,now_c = q.popleft() # now_r, now_c 현재 이동 위치
                for d in range(4): # nr, nc : 다음 위치
                    nr = now_r + dr[d]
                    nc = now_c + dc[d]

                    if 0 <= nr < N and 0 <= nc < N:
                        if rooms[now_r][now_c] + 1 == rooms[nr][nc]:
                            q.append((nr,nc))
                            visited[nr][nc] = visited[now_r][now_c] + 1
                            count += 1

            if max_count < count: # 이동할 수 있는 방 개수
                max_count = count
                max_value = rooms[r][c]

            if max_count == count: # 시작 번호
                if max_value > rooms[r][c]:
                    max_value = rooms[r][c]

    print(f'#{tc} {max_value} {max_count}')


# 두 번째 풀이
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    # 해당 숫자에서 갈 수 있으면 1을 기록
    # 값을 인덱스로 활용
    # 연속된 1의 길이가 가장 긴 곳이 정답
    visited = [0] * (N * N+1)

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    for r in range(N):
        for c in range(N):
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < N and rooms[r][c] + 1 == rooms[nr][nc]:
                    visited[rooms[r][c]] = 1
                    break # 한방향만 확인하면 되니까 조건에 맞는 원소 찾으면 break

    max_cnt = 0
    cnt = 0
    start = 0

    for i in range(1,N*N+1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt # 현재 인덱스 위치 i에서 연속된 1의 개수(cnt)만큼 빼주면 시작점이 나옴
            cnt = 0
    print(f'#{tc} {start} {max_cnt+1}')


# 세 번째 풀이(4/6)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    results = [] # 결과를 담을 리스트 (이동 방 개수, 방 번호)
    
    for i in range(N):
        for j in range(N):
            r, c = i, j
            count = 1
            dir = 0
            while dir < 4: # 4방향 모두 검사했는데 갈 곳이 없으면 종료
                for d in range(4):
                    dir += 1
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N: # 배열 범위 검사
                        continue
                    if room[r][c] + 1 == room[nr][nc]: # 이동 가능 조건
                        count += 1
                        r = nr
                        c = nc
                        dir = 0
            results.append((count, room[i][j])) # (이동 방 개수, 방 번호)
    
    results.sort(key = lambda x:(-x[0], x[1])) # count 기준 내림차순, 방 번호 기준 오름차순 정렬
    
    print(f'#{tc} {results[0][1]} {results[0][0]}')
