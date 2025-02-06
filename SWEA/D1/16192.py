T = int(input())

for tc in range(1, T+1):

    K, N, M = map(int, input().split())
    
    charges = list(map(int, input().split()))
    
    stops = [0] * (N+1) # 0부터 N까지 있는 리스트 생성

    for charge in charges:
        stops[charge] += 1 # 충전기가 있는 정류장에 1

    bus = 0 # 움직일 버스(처음 시작은 0) 인덱스를 나타냄
    count = 0 # 충전 횟수
    backwards = 0 # 뒤로 간 횟수

    bus += K # 시작 : 최대 이동 거리만큼 이동

    while True:

        if stops[bus]: # 이동한 정류장에 충전기가 있는 경우
            count += 1
            bus += K
            backwards = 0 # 충전소가 있는 정류장을 지나면 뒤로 간 횟수 초기화
        else:
            bus -= 1 # 충전기가 없으면 뒤로 한칸
            backwards += 1

        if bus >= N: # 종점 도착
            break

        if backwards == K: # 종점 도착X : 최대 거리만큼 이동했으나 그 사이에 충전소가 없는 경우 == 뒤로 이동한 횟수가 최대 이동 거리만큼
            break
    
    if bus >= N: # 종점 도착
        print(f'#{tc} {count}')
    else:
        print(f'#{tc} 0')    
