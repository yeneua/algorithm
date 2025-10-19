from collections import deque

N, K = map(int, input().split())

q = deque(range(1, N+1))
result = '<'

while q:
    for i in range(K-1):
        temp = q.popleft()
        q.append(temp)
    
    front = q.popleft()
    if len(q) == 0:
        result += f'{front}>'
    else:
        result += f'{front}, '

print(result)

'''
1~N까지 담은 큐 생성
앞에서 K-1명을 꺼내고 다시 뒤에 push
그러면 front에 제거할 사람이 남음
'''