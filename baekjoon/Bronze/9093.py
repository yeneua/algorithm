N = int(input())
for _ in range(N):
    sentence = list(input().split())
    
    for word in sentence:
        print(''.join(reversed(word)), end=' ')