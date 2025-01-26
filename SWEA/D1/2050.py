# 알파벳을 숫자로 변환

text = input()

for element in text:
    print(ord(element) - 64, end=' ')