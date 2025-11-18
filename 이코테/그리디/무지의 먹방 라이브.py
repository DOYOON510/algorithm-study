import heapq
food_times = [3, 2,1]
k = 5

if sum(food_times) <= k:
    print(-1)

q = []

for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i],i+1))

sum_value = 0 ## 먹기위해 사용한 시간
previous = 0 ## 직전에 다 먹은 음식 시간

length = len(food_times) ## 남은 음식의 개수

while sum_value + ((q[0][0]-previous)*length) <= k:
    now = heapq.heappop(q)[0] ## 가장 작은 음식의 양
    sum_value += (now-previous)*length
    length -= 1 ## 다먹은 음식 제외
    previous = now ## 이전 음식 시간 재설정

rst = sorted(q, key=lambda x:x[1])
print(rst[(k-sum_value)%length][1])

