T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_v = sum(numbers[:M])
    min_v = sum(numbers[:M])

    for i in range(N-M+1):
        temp = 0
        for j in range(i, i+M):
            temp += numbers[j]
        if max_v < temp:
            max_v = temp
        if min_v > temp:
            min_v = temp
    
    print(f'#{test_case+1} {max_v-min_v}')
