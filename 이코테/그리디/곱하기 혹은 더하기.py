data = input()
rst=0

for i in data:
    if int(i)==0 or int(i)==1:
        rst+=int(i)
    else:
        rst*=int(i)

print(rst)