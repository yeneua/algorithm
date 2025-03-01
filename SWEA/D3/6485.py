T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 버스 노선 개수

    result = []
    bus_route = [] # 각 버스 노선별 다니는 정류장 번호 범위
    bus_stop = [0] * 5001 # 버스 정류장 <- 몇개의 버스 노선이 다니는지(버스 정류장 번호 == 인덱스)

    for _ in range(N):
        s, e = map(int,input().split())
        bus_route.append((s,e))

    for route in bus_route:
        for i in range(route[0], route[1]+1):
            bus_stop[i] += 1
    
    P = int(input()) # 버스 정류장 개수
    
    for _ in range(P):
        temp = int(input())
        result.append(bus_stop[temp])
    
    print(f'#{tc}', *result)

'''
1~5000번 버스 정류장을 미리 만든다
각각 버스 정류장별로 지나가는 노선을 전부 +1
입력받은 버스 정류장 번호만 따로 result에 저장
'''
