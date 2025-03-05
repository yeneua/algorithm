T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # N : 노드 개수, M : 리프 노드 개수, L : 출력 노드 번호
    nodes = [0] * (N+1)

    for i in range(M): # 리프 노드 번호 저장
        node_num, num = map(int, input().split())
        nodes[node_num] = num
    
    for k in range(N,1,-1): # 1은 부모가 없는 루트노드니까 2번까지 수행
        nodes[k//2] += nodes[k] # 부모 노드에 자식 더하기 -> t 노드의 부모 노드는 t//2

    print(f'#{tc} {nodes[L]}')
