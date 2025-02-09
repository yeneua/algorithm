A = int(input())
B = int(input())
C = int(input())

number = A*B*C
number_to_string = str(number)
number_list = list(number_to_string)

for i in range(10):
    print(number_list.count(str(i)))
