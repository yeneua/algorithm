N = int(input())
numbers = list(map(int, input().split()))

max_v = numbers[0]
min_v = numbers[0]

for i in range(N):
    if max_v < numbers[i]:
        max_v = numbers[i]
    if min_v > numbers[i]:
        min_v = numbers[i]

print(min_v, max_v)
