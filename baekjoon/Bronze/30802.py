N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

shirts = 0

for i in range(6):
    if size[i] % T == 0:
        shirts += size[i] // T
    else:
        shirts += (size[i] // T) + 1

print(shirts)
print(N//P , N%P)
