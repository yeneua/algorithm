def make_set(n):
    parents = [i for i in range(n+1)]
    return parents

def find_set(x): # 어느 집합에 속해있는지?
    if parents[x] != x:
        return find_set(parents[x])
    return x

def union(x,y): # x 집합 y 집합 합치기(작은쪽으로)
    rep_x = find_set(x)
    rep_y = find_set(y)
    
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    parents = make_set(N)
    
    for i in range(M):
        x, y = map(int, input().split())
        union(x,y)
    
    rep_set = set()
    for i in range(1, N+1):
        rep_set.add(find_set(i))
    
    print(f'#{tc} {len(rep_set)}')
