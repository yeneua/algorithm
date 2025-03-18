def costing(row, cur_cost, cur_selected): # 행, 현재 비용, 열 사용 체크 리스트
    global min_cost

    if cur_cost > min_cost:
        return

    if row == N:
        min_cost = min(cur_cost, min_cost)
        return

    for j in range(N):
        if cur_selected[j]:
            continue
        else:
            cur_selected[j] = 1
            costing(row+1, cur_cost + cost[row][j], cur_selected)
            cur_selected[j] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    min_cost = float('inf')
    selected = [0] * N # 열 체크
    costing(0, 0, selected)

    print(f'#{tc} {min_cost}')
