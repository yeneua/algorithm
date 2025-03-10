T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    corridor = [0] * 201 # 방 사이 복도
    
    for _ in range(N): # 학생마다
        room1, room2 = map(int, input().split())
        if room1 < room2:
            start, end = room1, room2
        else:
            start, end = room2, room1

        corridor_set = set() # 지나가는 복도 번호 저장할 집합
        
        for i in range(start, end+1):
            idx = (i+1) // 2 # 지나가는 복도 번호(인덱스)
            corridor_set.add(idx) # 집합으로 중복 제거
            
        for k in corridor_set: # 지나가는 복도에 +1
            corridor[k] += 1

    print(f'#{tc} {max(corridor)}') # 최대값 -> 가장 많이 겹치는 구간
