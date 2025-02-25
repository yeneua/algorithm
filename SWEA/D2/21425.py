T = int(input())

for tc in range(1, T+1):
    A, B, N = map(int, input().split())
    count = 0
    
    while True:
        if A < B: # 작은 수에 큰 수를 더하는 게 더 빨리 커진다
            A, B = A,B
            A += B
            count += 1
            if A > N:
                break
            B += A
            count += 1
            if B > N:
                break
        else:
            A, B = B, A
            A += B
            count += 1
            if A > N:
                break
            B += A
            count += 1
            if B > N:
                break

    print(count)
