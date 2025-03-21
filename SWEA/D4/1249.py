import heapq

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def get_shortest(start_r, start_c): # 다익스트라
    distance = [[float('inf')] * N for _ in range(N)]

    # 시작점 처리
    heap = [(0, start_r, start_c)]
    distance[start_r][start_c] = 0

    while heap:
        cur_distance, cur_r, cur_c = heapq.heappop(heap)

        if distance[cur_r][cur_c] < cur_distance: # 이미 더 짧은 경로로 온 적이 있으면 pass(등호x)
            continue

        for d in range(4):
            next_r = cur_r + dr[d]
            next_c = cur_c + dc[d]

            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N:
                continue

            new_distance = cur_distance + maps[next_r][next_c]

            if distance[next_r][next_c] <= new_distance: # 이미 더 짧은 경로로 온 적이 있으면 pass
                continue

            distance[next_r][next_c] = new_distance
            heapq.heappush(heap,(new_distance,next_r,next_c))

    return distance


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input())) for _ in range(N)]
    result = get_shortest(0, 0)
    print(f'#{tc} {result[N-1][N-1]} ')
