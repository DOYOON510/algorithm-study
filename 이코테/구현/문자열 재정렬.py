# data = input()
#
# num_lst = [str(i) for i in range(10)] ## 하드코딩으로 비효율적임
# num = 0
# strs = ''
# for i in data:
#     if i in num_lst:
#         num += int(i)
#     else:
#         strs += i ## 반복문에서 문자열을 + 하는건 느리고 비효율적임 ''.join 쓰기
#
# ans = strs+str(num)
# print(ans)

data = input()
lst = []
num = 0

for i in data:
    if i.isalpha():
        lst.append(i)
    else:
        num += int(i)

lst.sort()

if num !=0:
    lst.append(str(num))

print(''.join(lst))


