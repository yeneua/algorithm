N, M = map(int, input().split())
is_not_hear = set()
is_not_see = []
answer = []

for _ in range(N):
    is_not_hear.add(input())

for _ in range(M):
    is_not_see.append(input())
    
for i in range(M):
    if is_not_see[i] in is_not_hear:
        answer.append(is_not_see[i])

answer.sort()

print(len(answer))
for person in answer:
    print(person)
