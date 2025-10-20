from collections import deque

q = deque()

N = int(input())
for _ in range(N):
    commands = input()

    if commands.startswith('push'):
        command, num = commands.split(' ')
    else:
        command = commands

    if command == 'push_back':
        q.append(num)
    
    if command == 'push_front':
        q.appendleft(num)
    
    if command == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print('-1')
    
    if command == 'pop_back':
        if q:
            print(q.pop())
        else:
            print('-1')
    
    if command == 'size':
        print(len(q))
    
    if command == 'empty':
        if q:
            print('0')
        else:
            print('1')
    
    if command == 'front':
        if q:
            print(q[0])
        else:
            print('-1')
    
    if command == 'back':
        if q:
            print(q[-1])
        else:
            print('-1')