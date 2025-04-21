total = int(input())
N = int(input())

cal_total = 0
for _ in range(N):
    amount, ea = map(int, input().split())
    cal_total += amount * ea

if cal_total == total:
    print('Yes')
else:
    print('No')
