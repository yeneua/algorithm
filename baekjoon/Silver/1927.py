import sys
import heapq

h = []
N = int(sys.stdin.readline()) # 빠른 입출력 방식

for _ in range(N):
    num = int(sys.stdin.readline()) # 빠른 입출력 방식
    if num == 0: # 입력이 0
        if len(h) == 0:
            print('0')
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, num)
