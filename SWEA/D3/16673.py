from collections import deque

def check_edges(V, edges, S, G):
    visited = [0] * (V+1)    # 방문여부
    q = deque()   # 큐 생성

    v = S
    q.append(v) # 인큐
    visited[v] = 1 # 방문 표시

    while q:
        v = q.popleft()
        for w in edges[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
                if w == G:
                    return visited[w]-1 # 처음 시작 노드가 1로 시작. 그 다음 방문 노드는 2가 됨(근데 간선은 하나만 지나니까!)
    return 0


T = int(input())

for tc in range(1, T+1):
    V,E = map(int,input().split()) # 노드 개수, 간선정보

    edges = [[] for _ in range(V+1)] # 간선정보
    for _ in range(E):
        start, end = map(int, input().split())
        edges[start].append(end)
        edges[end].append(start)
    S, G = map(int, input().split()) # 출발, 도착
    
    print(f'#{tc} {check_edges(V,edges,S,G)}')
