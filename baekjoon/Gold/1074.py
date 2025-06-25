N, r, c = map(int, input().split())

def find_nth(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n-1)
    
    if r < half and c < half: # 1시분면
        return find_nth(n-1, r, c)
    
    if r < half and c >= half: # 2사분면
        return half**2 + find_nth(n-1, r, c-half)
    
    if r >= half and c < half: # 3사분면
        return 2*half*half + find_nth(n-1, r-half, c)
    
    if r >= half and c >= half: # 4사분면
        return 3*half*half + find_nth(n-1, r-half, c-half)

answer = find_nth(N,r,c)
print(answer)

'''
half = 2 ** (n-1)

N=2일때
1사분면 -> 0부터 ~ 
2사분면 -> 4 ~ : half ** 2
3사분면 -> 8 ~ : 2 * half * half
4사분면 -> 12 ~ : 3 * half * half

N=3일때
1사분면 -> 0부터 ~
2사분면 -> 16 ~ : half ** 2
3사분면 -> 32 ~ : 2 * half * half
4사분면 -> 48 ~ : 3 * half * half

각 재귀호출시마다 return 꼭 써주기!!
위 단계로 결과 넘겨줘야되니까
'''


'''
# 처음 풀었던 코드 -> 메모리 초과
N, r, c = map(int, input().split())

lst= [[0] * (2**N) for _ in range(2**N)] # 0으로 채운 2^N * 2^N 배열

# 1 ~ 2^N * 2^N까지 배열 채우기
k = 1
for i in range(2**N):
    for j in range(2**N):
        lst[i][j] = k
        k+= 1

answer = lst[r][c] # lst 배열에서 r행 c열 숫자 저장

result = [] # 방문 순서대로 숫자를 저장할 배열

def find_nth(N, arr):
    if N > 1:
        # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 순서로 재귀 호출
        # N이 3이상일 때를 고려하여 2차원 배열로 넘겨줌
        find_nth(N-1, [row[0:2**(N-1)] for row in arr[0:2**(N-1)]])
        find_nth(N-1, [row[2**(N-1):2**N] for row in arr[0:2**(N-1)]])
        find_nth(N-1, [row[0:2**(N-1)] for row in arr[2**(N-1):2**N]])
        find_nth(N-1, [row[2**(N-1):2**N] for row in arr[2**(N-1):2**N]])
    else:
        for row in arr: # 2차원 배열로 넘어오기 때문에 2중 for문으로 result 배열에 추가
            for num in row:
                result.append(num) # 방문 순서대로 인덱스에 저장
        return

find_nth(N, lst)
print(result.index(answer)) # r행 c열에 있는 숫자의 방문 순서 출력 == 인덱스 번호

"""
N=3일 때
[row[0:2**(N-1)] for row in arr[0:2**(N-1)]] => arr[0:4][0:4]
[row[2**(N-1):2**N] for row in arr[0:2**(N-1)]] => arr[0:4][4:8]
[row[0:2**(N-1)] for row in arr[2**(N-1):2**N]] => arr[4:8][0:4]
[row[2**(N-1):2**N] for row in arr[2**(N-1):2**N]] => arr[4:8][4:8]
"""
'''
