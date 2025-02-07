'''
부분집합을 모두 만들고
원소 개수가 N 일때
부분집합의 합이 K 인 경우 계산
'''

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    numbers = [0] * 12
    for i in range(12):
        numbers[i] = i+1

    count = 0

    for i in range(1<<12):
        subset = []
        subset_sum = 0

        for j in range(12):
            if i & (1<<j):
                subset.append(numbers[j])
                subset_sum += numbers[j]

        if len(subset) == N and subset_sum == K:
            count += 1

    print(f'#{tc} {count}')
