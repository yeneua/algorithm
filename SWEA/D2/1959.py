# 첫 번째 방법
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers1 = list(map(int, input().split()))
    numbers2 = list(map(int, input().split()))

    max_sum = float('-inf')

    if N > M:
        for i in range(N-M+1): # 검사 시작 인덱스
            temp_sum = 0
            j = 0
            while j < M:
                temp_sum += numbers1[i+j]*numbers2[j]
                j += 1
            if max_sum < temp_sum:
                max_sum = temp_sum
    else:
          for i in range(M-N+1): # 검사 시작 인덱스
            temp_sum = 0
            j = 0
            while j < N:
                temp_sum += numbers1[j]*numbers2[i+j]
                j += 1
            if max_sum < temp_sum:
                max_sum = temp_sum

    print(f'#{tc} {max_sum}')


# 두 번째 방법
T = int(input())

for tc in range(1, T+1):
    len1, len2 = map(int, input().split())
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))

    if len1 > len2:
        long, short = len1, len2
        long_list, short_list = num1, num2
    else:
        long, short = len2, len1
        long_list, short_list = num2, num1

    max_sum = float('-inf')

    for i in range(long-short+1): # 검사 시작 인덱스
            temp_sum = 0
            j = 0
            while j < short:
                temp_sum += long_list[i+j]*short_list[j]
                j += 1
            if max_sum < temp_sum:
                max_sum = temp_sum

    print(f'#{tc} {max_sum}')
