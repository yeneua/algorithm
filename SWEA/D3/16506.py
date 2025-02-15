def check_graph_route(V, S, G):
    visited = [0] * (V+1) # 방문했는지 아닌지
    stack = []

    v = S # 시작위치
    visited[v] = 1

    while True:
        for w in adj_matrix[v]: # 갈 수 있는 정점들
            if visited[w] == 0: # 방문하지 않았다면
                v = w # 정점 이동
                if v == G:
                    return 1
                stack.append(w)
                visited[w] = 1 # 방문으로 표시
                break # 그 다음 정점으로
        else: # 갈 수 있는 정점이 없다면
            if stack:
                v = stack.pop()
            else:
                return 0
            

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_matrix = [[] for _ in range(V+1)]       
 
    for _ in range(E):  # 노드 간선 정보 받기
        s, e = map(int, input().split())
        adj_matrix[s].append(e)
    
    S, G = map(int, input().split())

    print(f'#{tc} {check_graph_route(V, S, G)}')