def route(node):
    global count
    
    if node == G:
        count += 1
        return
    
    for next in edges[node]: # 인접한 노드 탐색
        if visited[next]: # 방문한 적이 없는 노드만 탐색
            continue
        visited[next] = 1 # 방문 처리
        route(next) # 재귀 호출
        visited[next] = 0 # 방문하지 않은 상태로 되돌리기 -> 다른 재귀 호출을 위해서
    

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    inputs = list(map(int, input().split()))
    S, G = map(int, input().split())
    
    edges = [[] for _ in range(N+1)]
    
    for i in range(E):
        s, e = inputs[i*2], inputs[i*2+1]
        edges[s].append(e)
    
    visited = [0] * (N+1)
    count = 0
    route(S)
    
    print(f'#{tc} {count}')
