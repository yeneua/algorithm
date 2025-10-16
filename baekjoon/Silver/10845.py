from collections import deque
q = deque()

N = int(input())
for _ in range(N):
    commands = input()
    
    if commands.startswith('push'):
        command, number = commands.split()
    else:
        command = commands
    
    if command == 'push':
        q.append(number)
    
    elif command =='pop':
        if q:
            print(q.popleft())
        else:
            print('-1')
    
    elif command == 'size':
        print(len(q))
    
    elif command == 'empty':
        if q:
            print('0')
        else:
            print('1')
    
    elif command == 'front':
        if q:
            print(q[0])
        else:
            print('-1')
    
    elif command == 'back':
        if q:
            print(q[-1])
        else:
            print('-1')
