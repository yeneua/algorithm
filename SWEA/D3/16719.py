def insert_heap(item):
    global heap, last
    last += 1 # 마지막 원소 위치를 1증가시키고
    heap[last] = item # 그 자리에 원소를 넣음
    c = last
    p = c//2 # 완전 이진 트리에서 부모는 자식//2
    while p and heap[p] > heap[c]: # 부모가 존재하고(루트노드면 바꿀필요x), 자식보다 부모가 큰지 검사
        heap[p], heap[c] = heap[c], heap[p] # 자리바꾸기
        c = p # 업데이트. 다시 그 위에 노드들 검사
        p = c//2

def calculate(N, heap):
    idx = N
    result = 0
    while idx > 0:
        idx //= 2
        result += heap[idx]
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0 # 마지막에 삽입한 위치

    for num in numbers:
        insert_heap(num)

    answer = calculate(N, heap)
    print(f'#{tc} {answer}')
