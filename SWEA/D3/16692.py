# 첫 번째 풀이
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 간선 정보 만들기 <- 완전 이진 트리!
    edges = []
    for i in range(1,N//2+1):
        edges.extend([i,i*2])
        if N%2 == 0 and i == N//2:
            break
        edges.extend([i,i*2+1])

    # 부모 번호를 인덱스로 자식 표현
    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(0, N-1):
        p = edges[i*2]
        c = edges[i*2+1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c


    # 중위 순회로 트리에 값 넣기
    tree = [0] * (N+1)

    k = 1
    def in_order(t):
        global k
        if t :
            in_order(left[t])
            tree[t] = k
            k += 1
            in_order(right[t])

    in_order(1)

    root_node = tree[1]
    nth_node = tree[N//2]

    print(f'#{tc} {root_node} {nth_node}')


'''
중위순회 - 왼 -> 부모 -> 오
1. 완전 이진 트리에 대한 간선 정보 만들기
2. left, right 부모 노드 번호를 인덱스로 해서 만들기
=> 트리 구조 완성!
3. 중위 순회로 트리 값 넣기
4. 루트 노드, N//2 노드 출력
'''


# 두 번째 풀이
def in_order(t):
    global num
    if t > N:
        return
    in_order(2*t)
    tree[t] = num
    num += 1
    in_order(2*t+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
