N = int(input())
members = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    
    members.append((age, name, i))

members.sort(key=lambda x : (x[0], x[2]))

for k in range(N):
    print(members[k][0], members[k][1])
