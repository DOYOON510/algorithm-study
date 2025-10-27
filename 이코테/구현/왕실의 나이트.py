data = input()
row = int(data[1])
column = ord(data[0])-96

move_types = [(1,2), (2,1), (-1,2), (2,-1), (1,-2), (-2,1), (-1,-2), (-2,-1)]
cnt = 0

for i in move_types:
    if i[0]+row>=1 and i[1]+column>=1 and i[0]+row<=8 and i[0]+column<=8:
        cnt+=1
        print(i)
    else: continue

print(cnt)