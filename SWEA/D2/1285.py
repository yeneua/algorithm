T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    position = list(map(int, input().split()))
    
    distance = 100000
    count = 0
    for i in range(N):
        cur_distance = abs(position[i]-0)
        distance = min(distance, cur_distance)

    count = position.count(distance) + position.count(-distance)
    print(f'#{tc} {distance} {count}')
