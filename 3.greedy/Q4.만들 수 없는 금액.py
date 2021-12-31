n = int(input())

coin = list(map(int, input().split()))

coin.sort()


target = 1


for i in coin:
    if i < target:
        break
    else:
        target += i
print(target)
