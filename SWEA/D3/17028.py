def find_set(x): # 대표자를 찾아주는 함수
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y): # x,y 집합을 합침
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
        start, end, weight = map(int,input().split())
        edges.append((start, end, weight))
    edges.sort(key = lambda x:x[2]) # 가중치 기준 오름차순 정렬

    parents = [i for i in range(V+1)]
    total_weight = 0
    count = 0

    for start, end, weight in edges: # 최소 신장 트리 - 크루스칼 알고리즘 이용
        if find_set(start) != find_set(end): # 연결이 되어 있지 않으면
            union(start,end) # 연결하고
            total_weight += weight # MST 가중치에 더하기
            count += 1

        if count == V: # MST 구성 끝. N개의 노드라면 간선은 N-1개(이 문제에서 노드는 V+1개임)
            break

    print(f'#{tc} {total_weight}')