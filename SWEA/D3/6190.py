def is_valid(num):
    nums = [int(k) for k in str(num)]
    
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            continue
        else:
            return False
    
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    max_value = -1 # 1 <= Aj <= 30000
    
    for i in range(N-1):
        for j in range(i+1, N):
            num = numbers[i] * numbers[j]
            if is_valid(num):
                max_value = max(max_value, num)
            
    print(f'#{tc} {max_value}')
