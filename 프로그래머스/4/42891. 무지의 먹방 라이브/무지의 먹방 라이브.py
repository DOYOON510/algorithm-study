import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    length = len(food_times)

    sum_times = 0
    prev = 0 
    
    q = []
    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))
    
    while sum_times + ((q[0][0] - prev) * length) < k:
        now = heapq.heappop(q)[0]
        sum_times += (now-prev)*length
        length -= 1
        prev = now
        
    rst = sorted(q, key = lambda x : x[1])
    
    return rst[(k-sum_times)%length][1]