from collections import deque

def solution(start, end):
    q = deque()
    visited = [-1] * 200001 # current*2 일 경우를 고려해서 N,K의 최대 범위인 100,000의 두배까지 설정

    visited[start] = 0
    q.append(start)

    while q:
        current = q.popleft()
        
        if current == end:
                return visited[current]

        for next in (current-1, current+1, current*2):

            if next > 200000 or next < 0:
                continue
            
            if visited[next] != -1:
                continue

            visited[next] = visited[current] + 1
            q.append(next)

N, K = map(int, input().split())
if N == K:
    print('0')
else:
    answer = solution(N, K)
    print(answer)
