T = int(input())

for tc in range(1,T+1):
    N = int(input())
    dock = [] * N
    for _ in range(N):
        start, end = map(int, input().split())
        dock.append((start,end)) # (시작 시간, 종료 시간) 튜플로 저장
    dock.sort(key=lambda x:x[1]) # 종료시간 기준 오름차순 정렬

    count = 0
    end_time = 0
    for luggage in dock:
        if end_time <= luggage[0]: # 이전 화물의 종료 시간 <= 현재 화물 시작 시간
            end_time = luggage[1]
            count += 1

    print(f'#{tc} {count}')
