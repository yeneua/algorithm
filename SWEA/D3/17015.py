def make_set(x): # 자기 자신을 대표로하는 집합을 만들어주는 함수
    parents = [i for i in range(x+1)]
    return parents


def find_set(x): # 대표를 찾아주는 함수
    if parents[x] == x: # 자기 자신이 대표자면 그대로 리턴
        return x
    return find_set(parents[x]) # 자기 자신이 대표자가 아니라면 부모를 통해 대표자를 찾아감

def union(x,y): # x와 y를 합치는 함수 -> 대표를 합침!(작은걸로 합침)
    
    rep_x = find_set(x)
    rep_y = find_set(y)
    
    if rep_x != rep_y:
        if rep_x < rep_y:
            parents[rep_y] = rep_x
        else:
            parents[rep_x] = rep_y


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    groups = list(map(int, input().split()))
    
    parents = make_set(N)

    for i in range(M):
        union(groups[i*2], groups[i*2+1])    
    
    rep = set() # 대표자 몇명인지
    for i in range(1,N+1):
        rep.add(find_set(i))

    print(f'#{tc} {len(rep)}')
