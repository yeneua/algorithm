for tc in range(1,11):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0

    def sorting(num_list):
        counts = [0] * 101
        new_num_list = [0] * 100

        for i in num_list:
            counts[i] += 1
        
        for j in range(1, len(counts)):
            counts[j] += counts[j-1]
        
        for k in range(len(num_list)-1, -1, -1):
            counts[num_list[k]] -= 1
            new_num_list[counts[num_list[k]]] = num_list[k]

        global numbers
        numbers = new_num_list        
        
    for _ in range(N):
        sorting(numbers)
        numbers[0] += 1
        numbers[-1] -=1
    
    sorting(numbers)

    result = numbers[-1] - numbers[0]

    print(f'#{tc} {result}')
