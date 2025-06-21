T = int(input())
for _ in range(T):
    N = int(input())
    fib_lst = [0] * 41 # 0 <= N <= 40
    
    fib_lst[0] = (1,0) # (0 호출 횟수, 1 호출 횟수)
    fib_lst[1] = (0,1)
    
    for i in range(2, N+1):
        fib_lst[i] = (fib_lst[i-1][0] + fib_lst[i-2][0], fib_lst[i-1][1] + fib_lst[i-2][1])

    print(*fib_lst[N])