T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    weights.sort(reverse=True) # 화물 무게 내림차순 정렬
    trucks.sort(reverse=True) # 트럭 적재용량 내림차순 정렬

    if N <= M: idx = N # weights, trucks 중 길이가 작은거 만큼 for문
    else: idx = M

    result = 0
    truck_num = 0 # 트럭 0번째부터 검사
    for k in range(idx):
        if weights[k] <= trucks[truck_num]:
            result += weights[k]
            truck_num += 1 # 적재용량 초과해서 못 옮길 경우 그 다음 화물로도 검사해야함 -> 트럭 인덱스 따로 관리

    print(f'#{tc} {result}')



