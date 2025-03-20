import heapq

def dijkstra(start_node):
    distance = [float('inf')] * (N+1) # 누적 거리를 저장하는 리스트
    
    # 시작 정점 처리
    heap = [(0,start_node)]
    distance[start_node] = 0
    
    while heap: # 대기열이 빌때까지
        weight, node = heapq.heappop(heap)
        
        if distance[node] < weight: # 이미 더 짧은 경로로 온 적이 있다면 pass (등호 없는 이유 : 등호가 있으면 이미 최단 경로로 확정된 정점들도 continue됨)
            continue
        
        for next in graph[node]:
            next_node, next_weight = next[0], next[1]
            
            next_distance = weight + next_weight # 현재 거리 + 다음으로 이동할 거리
            
            if distance[next_node] <= next_distance: # 이미 최단 경로로 확정되어 있다면 볼 필요x
                continue
            
            distance[next_node] = next_distance
            heapq.heappush(heap, (next_distance, next_node))
    
    return distance
                 
T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((end,weight))
    
    result = dijkstra(0)
        
    print(f'#{tc} {result[-1]}') # N번 노드까지 갈 때 최단 거리

'''
E개의 단방향 간선
0~N개의 노드 == N+1개
최소한의 거리? -> 다익스트라
'''
