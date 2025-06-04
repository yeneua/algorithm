N, M = map(int, input().split())
lst = list(map(int, input().split()))

prefix = [0] * (N+1) # 입력으로 들어오는 구간이 1부터 시작이니까 0을 제일 앞에 둔다
total = 0

for i in range(N):
    total += lst[i]
    prefix[i+1] = total

for _ in range(M):
    start, end = map(int, input().split())
    print(prefix[end] - prefix[start-1])


'''
입력 : [5,4,3,2,1]
누적합 : [0,5,9,12,14,15]
prefix[0] = 0 : 0번째 원소까지의 합
prefix[1] = 5 : 1번째 원소까지의 합
prefix[2] = 9 : 2번째 원소까지의 합
prefix[3] = 12 : 3번째 원소까지의 합
prefix[4] = 14 : 4번째 원소까지의 합
prefix[5] = 15 : 5번째 원소까지의 합

ex. 2~4 구간 합
(4번재 원소까지의 합) - (1번째 원소까지의 합)

=> prefix[end] - prefix[start-1]
'''
