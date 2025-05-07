N = int(input())

words = set()
for _ in range(N):
    words.add(input())

words = list(words)
words.sort(key=lambda x : (len(x), x)) # 길이순, 사전순 정렬

for word in words:
    print(word)