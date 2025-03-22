# 첫 번째 풀이 - 프림
import heapq

def prim(start):
    visited = [0] * (V+1)
    total_weight = 0
    
    # 시작 정점 처리
    heap = [(0, start)]
    
    while heap:
        weight, node = heapq.heappop(heap) # 뽑으면서 가중치, 방문 처리
        
        if visited[node] == 1:
            continue
        
        visited[node] = 1
        total_weight += weight
        
        for next in edges[node]:
            next_node = next[0]
            next_weight = next[1]
            
            if visited[next_node]:
                continue
            
            heapq.heappush(heap, (next_weight, next_node))  # 갈 수 있는 간선 모두 push. 여기서는 방문, 가중치 처리x
    return total_weight

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges[start].append((end, weight)) # MST는 양방향(무방향) 간선!!!!!
        edges[end].append((start, weight))
        
    result = prim(1)

    print(f'#{tc} {result}')
    

# 두 번째 풀이 - 크루스칼
def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    rep_x = find_set(x)
    rep_y = find_set(y)
    
    if rep_x == rep_y:
        return
    
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges.append((start,end,weight))
        
    edges.sort(key=lambda x:x[2])
    parents = [i for i in range(V+1)]
    
    total_weight = 0
    count = 0
    for start, end, weight in edges:
        if find_set(start) != find_set(end):
            union(start,end)
            total_weight += weight
            count += 1
            
            if count == V-1:
                break
            
    print(f'#{tc} {total_weight}')


'''
실행시간
- Prim : 6128ms
- Kruskal : 7996ms

문제
정점 개수 1 <= V <= 100,000
간선 개수 1 <= E <= 200,000

시간 복잡도
1. Prim
- (V+E) log V
- 정점에 비해 간선이 많을수록 유리

2. Kruskal
- E log E
- 정점에 비해 간선이 적을수록 유리
'''
