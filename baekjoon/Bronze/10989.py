N = int(input())
numbers = [0] * 10001 # 카운팅 정렬 활용

for _ in range(N):
    idx = int(input())
    numbers[idx] += 1
    
for i in range(len(numbers)):
    if numbers[i] == 0:
        continue
    if numbers[i]:
        for j in range(numbers[i]):
            print(i)
