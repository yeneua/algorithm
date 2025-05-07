N = int(input())
check = '666'
count = 0
i = 0

while True:
    i += 1
    if check in str(i):
        count += 1
    i = int(i)
    if count == N:
        print(i)
        break
    
