import bisect

n, x = map(int, input().split())

arr = list(map(int, input().split()))
ans = bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)
print(ans if ans > 0 else -1)
