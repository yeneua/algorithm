def move_bus(idx, cnt):
    global min_cnt

    if cnt >= min_cnt:  # 가지치기 - '이상'으로 조건 부여, 같은 경우에도 볼 필요 없다.(호출 횟수 차이 있음)
        return

    if idx >= N - 1:  # 종점 이상이면 리턴
        min_cnt = min(min_cnt, cnt)
        return

    # 종점은 N-1
    # move_bus(idx+k, cnt+1)에서 idx+k를 전달하는데
    # 이때 idx+k가 N-1 이상이면 리턴되기 때문에 인덱스 에러 x
    # 충전지(station)의 인덱스는 0 ~ N-2
    for k in range(1, station[idx] + 1):  # 현재 idx에서 갈 수 있는 거리만큼 검사
        move_bus(idx + k, cnt + 1)  # k 선택하면 idx+k로 자리 교환


T = int(input())

for tc in range(1, T + 1):
    inputs = list(map(int, input().split()))
    N = inputs[0]
    station = inputs[1:]

    min_cnt = float('inf')
    move_bus(0, 0)  # 시작 위치, 카운트

    print(f'#{tc} {min_cnt - 1}')