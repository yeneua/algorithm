import heapq

def dijkstra(start, end): # 다익스트라
    distance = [float('inf')] * (N+1)
    
    heap = [(0,start)] # 시간(가중치), 시작 정점
    distance[start] = 0
    
    while heap:
        
        weight, node = heapq.heappop(heap)
        
        if node == end: # 현재 노드가 end면 그 정점의 누적 거리 리턴
            return distance[node]
        
        if distance[node] < weight:
            continue
        
        for next in graph[node]:
            next_weight = next[0]
            next_node = next[1]
            
            new_weight = weight + next_weight
            
            if distance[next_node] <= new_weight:
                continue
            
            distance[next_node] = new_weight
            heapq.heappush(heap,(new_weight, next_node))
    

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, weight = map(int, input().split())
        graph[start].append((weight,end))
    
    max_time = float('-inf')
    for k in range(1, N+1):
        if k == X: continue
        time = dijkstra(k,X) + dijkstra(X,k) # i번 노드 ~ X까지 거리 + X ~ i로 돌아오는 거리
        max_time = max(max_time, time)
    
    print(f'#{tc} {max_time}')
