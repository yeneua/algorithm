for tc in range(1, 11):
    N, password = input().split()
    stack = [0] * int(N)
    top = -1

    for num in password:
        top += 1
        stack[top] = num
        if top > 0 and stack[top] == stack[top-1]:
            stack[top] = 0
            stack[top-1] = 0
            top -= 2
            
    print(f'#{tc}',end=' ')
    i = 0
    while True:
        print(stack[i], end='')
        i += 1
        if stack[i] == 0:
            break
    print()
