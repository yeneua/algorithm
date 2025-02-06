# 숫자카드

T = int(input())

for tc in range(T):
    N = int(input())

    numbers = list(map(int, input()))

    # 1. 빈 배열(0~9 숫자 배열)
    counts = [0] * 10

    # 2. 숫자별로 개수 세기
    for i in range(N):
        counts[numbers[i]] += 1

    # 3. 가장 많은 숫자
    max_num = 0 # 가장 많은 카드의 숫자
    max_counts = 0 # 장 수
    for i in range(10):
        if max_counts <= counts[i]:
            max_counts = counts[i]
            max_num = i

    print(f'#{tc+1} {max_num} {max_counts}')
