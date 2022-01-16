n = int(input())

part = list(map(int, input().split()))

m = int(input())
order = list(map(int, input().split()))

part.sort()


def bis(array, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bis(array, target, start, mid - 1)
    else:
        return bis(array, target, mid + 1, end)


for item in order:
    if bis(part, item, 0, len(part) - 1) == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
