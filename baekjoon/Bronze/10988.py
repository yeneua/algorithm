word = list(input())
N = len(word)

result = 1

for i in range(N//2):
    if word[i] != word[N-1-i]:
        result = 0
        break

print(result)
