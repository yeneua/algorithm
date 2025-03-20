import math

def find_set(x):
    if x == parents[x]:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    rep_x = find_set(x)
    rep_y = find_set(y)
    
    if rep_x == rep_y:
        return
    
    if rep_x <rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    x_position = list(map(int, input().split()))
    y_position = list(map(int, input().split()))
    E = float(input())
    
    graph = []
    
    for i in range(N): # 정점 하나를 기준으로
        for j in range(i+1,N): # 나머지 모든 정점들에 대한 가중치를 계산
            length = math.sqrt((x_position[j] - x_position[i]) ** 2 + (y_position[j] - y_position[i]) ** 2) # 좌표간의 거리를 계산하여 가중치 계산
            weight = E * (length ** 2) # 가중치 구하기
            graph.append((i,j,weight))
    graph.sort(key=lambda x:x[2]) 
    parents = [i for i in range(N)]
    
    result = 0
    cnt = 0
    
    for start, end, weight in graph:
        if find_set(start) != find_set(end):
            union(start, end)
            result += weight
            cnt += 1
        
            if cnt == N-1:
                break
            
    print(f'#{tc} {format(result, ".0f")}')

'''
모든 정점들이 연결되어야함
양방향
최소 가중치
=> MST
- 무방향 가중치 그래프에서 모든 정점을 연결하는 가중치의 합이 최소가 되는 트리
''' 
