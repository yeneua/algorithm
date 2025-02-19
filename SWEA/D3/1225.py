for _ in range(1, 11):
    tc = int(input())

    password = list(map(int, input().split()))

    size = 9
    pw_queue = [0] * size
    front = rear = 0
    for i in range(8):
        rear = (rear+1)%size
        pw_queue[rear] = password[i]

    number = 0
    while True:
        front = (front + 1) % size
        number = number % 5 + 1
        temp = pw_queue[front] - number
        pw_queue[front] = 0
        if temp <= 0:
            temp = 0
            rear = (rear+1) % size
            pw_queue[rear] = temp
            break
        else:
            rear = (rear+1) % size
            pw_queue[rear] = temp
    
    result = []
    for i in range(size):
        result.append(pw_queue[(i+front) % 9]) # front : 시작 인덱스
    result = result[1:]
    
    print(f'#{tc}', *result)
