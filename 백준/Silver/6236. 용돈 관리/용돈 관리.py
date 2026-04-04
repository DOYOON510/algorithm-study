import sys

n, m = map(int,sys.stdin.readline().split())
money = []
for i in range(n):
    money.append(int(sys.stdin.readline()))

start, end = max(money), sum(money)

while start <= end:
    mid = (start + end) // 2 
    charge = mid
    count = 1
    for i in money: 
        if charge - i < 0: 
            count += 1
            charge = mid
        charge -= i 
    if count > m: 
        start = mid + 1
    else: 
        end = mid - 1
print(start)