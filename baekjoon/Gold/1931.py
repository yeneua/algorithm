answer = 0
timetable = []

N = int(input())

for _ in range(N):
    start, end = map(int, input().split())
    timetable.append((start, end))

timetable.sort(key = lambda x:(x[1], x[0]))
end_time = 0
for i in range(N):
    if timetable[i][0] == timetable[i][1] or end_time <= timetable[i][0]:
        answer += 1
        end_time = timetable[i][1]

print(answer)
