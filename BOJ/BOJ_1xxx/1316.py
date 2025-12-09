
n = int(input())
cnt = 0

for _ in range(n):
    data = input()
    word = []
    word.append(data[0])
    for j in range(1, len(data)):
        if data[j-1] != data[j]:
            word.append(data[j])
    if len(set(word))==len(word):
        cnt += 1
print(cnt)

