T = int(input())
for _ in range(T):
    floor_0 = list(range(15)) # 0층
    rooms = [floor_0] + [[0] * 15 for _ in range(14)]
    
    for k in range(1,15):
        for n in range(1,15):
            rooms[k][n] = rooms[k-1][n] + rooms[k][n-1]
    
    k = int(input())
    n = int(input())
    print(rooms[k][n])

'''
DP(dynamic programming)
- 작은 문제가 반복이 일어남
- 같은 문제는 구할 때마다 정답이 같음

처음에 작성했던 재귀 함수 -> 답은 맞으나 시간 초과
def func(k,n):
    
    if k > 0:
        result = 0
        for i in range(1, n+1):
            result += func(k-1, i)
        return result
    else:
        return n
'''
