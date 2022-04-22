import sys

input = sys.stdin.readline


N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))

arr = sorted(arr, key=lambda x: (x[1], x[0]))

cnt = 1
end_time = arr[0][1]
for i in range(1, N):
    if arr[i][0] >= end_time:
        cnt += 1
        end_time = arr[i][1]

print(cnt)
