from sys import stdin
input = stdin.readline

N = int(input())
lst = list(map(int, input().split()))
length = [1] * N # 수열 길이를 저장할 배열 -> 자기 자신을 포함하니 초기값 1로 설정

# 자기 자신을 포함하여 만들 수 있는 가장 긴 증가하는 부분 수열의 길이를 저장해야함!

for i in range(N): # 현재 탐색하는 원소에서
    for j in range(i): # 앞에 위치한 원소들을 모두 확인
        if lst[i] > lst[j]:
            length[i] = max(length[i], length[j]+1)

print(max(length))
         
'''
처음 접근 방식
ex. [10, 20, 10, 30, 20, 50] -> [1, 2, 2, 3, 3, 4]
- 탐색하고 있는 원소의 앞 수열이 가지고 있는 LIS 길이를 찾음
- 그 길이를 가지고 있는 가장 첫번째 원소를 찾음
- 그 원소와 현재 탐색하고 있는 원소 크기 비교

i=5일 때 20이 가지고 있는 길이는 3
3 길이를 가지고 있는 원소 중 가장 앞 원소는 30
30과 50 숫자 크기 비교

'''
