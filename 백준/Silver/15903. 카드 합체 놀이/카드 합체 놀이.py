import heapq
n, m = map(int, input().split())
lst = list(map(int, input().split()))
heapq.heapify(lst)

for _ in range(m):
    x = heapq.heappop(lst) + heapq.heappop(lst)
    heapq.heappush(lst, x)
    heapq.heappush(lst, x)

print(sum(lst))