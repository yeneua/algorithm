# min max

T = int(input())

for test_case in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers:
        if max_value < num:
            max_value = num
        if min_value > num:
            min_value = num
    
    print(f'#{test_case+1} {max_value-min_value}')
