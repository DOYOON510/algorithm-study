data = input()

lst = [int(i) for i in data]
length=int(len(data)/2)

sum1 = sum(lst[:length])
sum2 = sum(lst[length:])

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')
