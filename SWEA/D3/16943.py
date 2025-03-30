def binary_search(num):
    start = 0
    end = N-1
    
    flag = ''

    while start <= end:
        mid = (start+end) // 2
        
        if A[mid] == num:
            return 1
        
        if A[mid] > num:
            if flag == 'left':
                return 0
            end = mid-1
            flag = 'left'
        
        if A[mid] < num:
            if flag == 'right':
                return 0
            start = mid+1
            flag = 'right'

    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    
    result = 0
    
    for i in range(M):
        if binary_search(B[i]):
            result += 1
    
    print(f'#{tc} {result}')
