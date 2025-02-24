words = [list(input()) for _ in range(5)]

max_len = 0
for i in range(5):
    if max_len < len(words[i]):
        max_len = len(words[i])

for i in range(5):
    if len(words[i]) < max_len:
        for j in range(max_len - len(words[i])):
            words[i].append("")

for j in range(max_len):
    for i in range(5):
        print(words[i][j], end='')