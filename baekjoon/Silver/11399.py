N=int(input())
lst=list(map(int,input().split()))

lst.sort()
total=wait=0


for i in range(N):
    wait+=lst[i]
    total+=wait
print(total)
