import heapq

n = int(input())

card = []
for _ in range(n):
    card.append(int(input()))
temp = 0
heapq.heapify(card)
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    temp += a + b
    heapq.heappush(card, a + b)
print(temp)
