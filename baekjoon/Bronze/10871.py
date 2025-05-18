N, X = map(int, input().split())
lst = list(map(int, input().split()))

for item in lst:
    if item < X:
        print(item, end=' ')
