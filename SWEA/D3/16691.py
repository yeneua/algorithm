T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        p = edges[i*2]
        c = edges[i*2+1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # 트리 안에 속한 노드의 개수 알기 -> 순회
    count = 0
    def pre_order(t): # 전위순회 : 부모 - 왼 - 오
        if t:
            global count
            count += 1
            pre_order(left[t])
            pre_order(right[t])

    pre_order(N)
    print(f"#{tc} {count}")
