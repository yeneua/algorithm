from collections import deque

def calculate(num, operation):
    if operation == 0:
        return num + 1
    elif operation == 1:
        return num - 1
    elif operation == 2:
        return num * 2
    elif operation == 3:
        return num - 10

def operate_count(start): # bfs
    q = deque()
    q.append((start, 0)) # 현재 숫자, 연산 횟수 함께 저장
    visit_set.add(start)

    while q:
        now, count = q.popleft()

        if now == M:
            return count

        for i in range(4):
            if now > M and (i % 2 == 0): # 가지치기 - 현재 결과가 M보다 큰 상태에서 '+','*' 연산이라면 리턴
                continue

            next = calculate(now, i) # 연산의 중간 결과

            if next > 1000000:  # 가지치기 -  연산 중간 과정이 백만을 넘으면 리턴(문제 조건)
                continue

            if next in visit_set: # 가지치기 - 이미 연산한 결과면 리턴 -> 더 적은 연산 횟수로 도출할 수 있는 결과니까
                continue

            visit_set.add(next)
            q.append((next, count + 1))


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    visit_set = set() # 연산의 중간 결과 저장, visited 배열처럼 활용 -> 리스트 사용시 시간초과!, set의 in 연산은 O(1)
    print(f'#{tc} {operate_count(N)}')
