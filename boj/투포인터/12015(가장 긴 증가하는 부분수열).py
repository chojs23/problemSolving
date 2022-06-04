n = int(input())
cases = list(map(int, input().split()))
lis = [0]

for case in cases:
    if lis[-1] < case:
        lis.append(case)
    else:
        left = 0
        right = len(lis) - 1

        while left < right:
            mid = (right + left) // 2
            if lis[mid] < case:
                left = mid + 1
            else:
                right = mid
        lis[right] = case

print(lis)
