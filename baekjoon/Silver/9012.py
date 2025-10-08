N = int(input())

for _ in range(N):
    PS = input()
    
    stack = []
    for parentheses in PS:
        if parentheses == '(':
            stack.append(parentheses)
        
        elif parentheses == ')':
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')