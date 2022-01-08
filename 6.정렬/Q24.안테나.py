n = int(input())

house = list(map(int, input().split()))
house.sort()

print(house[(len(house) - 1) // 2])
