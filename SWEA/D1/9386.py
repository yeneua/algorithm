T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = input()

    max_count = 0
    count = 0


    for i in range(N):
        if numbers[i] == '1':
            count +=1
        else:
            count = 0
        if max_count < count:
            max_count = count

    print(f'#{tc} {max_count}')