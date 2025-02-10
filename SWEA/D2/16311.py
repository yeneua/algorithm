T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 정렬
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N): # 최소값찾기
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    # 절반을 중심으로 분리
    if N % 2: # 홀수
        min_numbers = numbers[0:N//2] # 0 ~ N//2-1
        max_numbers = numbers[N-1:N//2-1:-1] # N//1-1 ~ N-1
    else: # 짝수
        min_numbers = numbers[0:N//2] # 0 ~ N//2
        max_numbers = numbers[N-1:N//2-1:-1] # N//2 ~ N-1

    print(f'#{tc}', end=' ')
    for i in range(N//2):
        if i == 5: break
        print(max_numbers[i], min_numbers[i], end=' ')
    print()
