def partitioning(left, right):
    pivot = num[left]
    i = left + 1
    j = right
    
    while i <= j:
    
        while i <= j and num[i] <= pivot:
            i += 1
        
        while i <= j and num[j] >= pivot:
            j -= 1
            
        if i < j:
            num[i], num[j] = num[j], num[i]
    
    num[left], num[j] = num[j], num[left]
    
    return j
    
def quick_sort(left, right):
    
    if left < right:
        pivot = partitioning(left,right)
        quick_sort(left, pivot-1)
        quick_sort(pivot+1, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    quick_sort(0, N-1)
    print(f'#{tc} {num[N//2]}')
