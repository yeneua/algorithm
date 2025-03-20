import heapq

dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

def find_route(r, c): # 다익스트라
    # 힙, 누적 거리 생성
    heap = []
    distance = [[float('inf')] * N for _ in range(N)] # 누적 거리(가중치) 저장

    # 시작 정점 처리
    heapq.heappush(heap, (0, r, c))
    distance[r][c] = 0 # 시작점의 누적 거리는 0

    while heap:
        weight, r, c = heapq.heappop(heap)

        if weight > distance[r][c]: # 현재 가중치가 이미 방문했던 가중치보다 크면 볼 필요x
            continue

        for d in range(4):
            next_r = r + dr[d]
            next_c = c + dc[d]
            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N:
                continue

            diff = 1 # 문제 조건
            if heights[next_r][next_c] > heights[r][c]: # 이동 높이 만큼 가중치 증가
                diff += heights[next_r][next_c] - heights[r][c]

            new_weight = weight + diff # 현재 가중치 + 다음 칸으로 이동하는 가중

            if new_weight >= distance[next_r][next_c]: # 현재 최소 누적 가중치랑 비교. 같거나 더 크면 볼 필요x
                continue

            distance[next_r][next_c] = new_weight # 누적 거리 저장
            heapq.heappush(heap, (new_weight, next_r, next_c)) # 힙에 넣기

    return distance[N-1][N-1] # 마지막 좌표 값 리턴


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    result = find_route(0, 0)
    print(f'#{tc} {result}')


'''
다익스트라 알고리즘 이용
0,0에서 시작
상하좌우 중 갈 수 있는 정점 탐색
가중치를 distance에 저장
가장 작은 가중치를 저장
'''