# 평균값 구하기

T = int(input())

for test_case in range(T):
    numbers = list(map(int, input().split()))
    sum_numbers = 0
    for num in numbers:
        sum_numbers += num
    result = round(sum_numbers/len(numbers))
    print(f'#{test_case+1} {result}')