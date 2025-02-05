h, m = map(int, input().split())

if h != 0 and m >= 45:
    print(h, m-45)

if h != 0 and m < 45:
    print(h-1, m+15)

if h == 0 and m >= 45:
    print(h, m-45)

if h == 0 and m < 45:
    h = 23
    print(h, m+15)
