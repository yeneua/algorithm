stack = []

N = int(input())
for _ in range(N):
    commands = input()
    
    if commands.startswith('push'):
        command, num = commands.split()
        stack.append(num)
    
    elif commands == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            num = stack.pop()
            print(num)
    
    elif commands == 'size':
        print(len(stack))
    
    elif commands == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    
    elif commands == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])