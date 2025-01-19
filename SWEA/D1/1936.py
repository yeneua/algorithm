# 1대1 가위바위보

a, b = map(int, input().split())

if a < b:
    print("B")
elif a == 3 and b == 1:
    print("B")
else:
    print("A")