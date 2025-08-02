L, P = map(int, input().split())
lst = list(map(int, input().split()))

for i in range(len(lst)):
    print(lst[i] - (L*P), end=' ')
