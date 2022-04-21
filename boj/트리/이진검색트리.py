import sys

input = sys.stdin.readline


sys.setrecursionlimit(10**6)

tree = []
count = 0
while 1:
    try:
        temp = int(input())
        tree.append(temp)
    except:
        break


def post_order(start, end):

    if start > end:
        return

    root = tree[start]
    idx = start + 1

    while idx <= end:
        if tree[idx] > root:
            break
        idx += 1

    post_order(start + 1, idx - 1)
    post_order(idx, end)

    print(root)


post_order(0, len(tree) - 1)
