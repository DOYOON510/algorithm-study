data = input()
cnt0 = 0
cnt1 = 0
rst = int(data[0])

if int(data[-1]) == 0 : cnt0 += 1
else : cnt1 += 1

for i in data:
    if rst == int(i):
        continue
    elif rst != int(i):
        rst = int(i)
        if i=='0': cnt1 += 1
        else : cnt0 += 1

if min(cnt0, cnt1) == 0 : print(0)
else : print(min(cnt0, cnt1))
