n = int(input())
data = []
for _ in range(n):
    [name, kor, eng, math] = map(str, input().split())

    data.append([name, int(kor), int(eng), int(math)])

data = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in data:
    print(student[0])
