from collections import deque

def solution(bandage, health, attacks):
    atk_q = deque(attacks)
    time = 1
    count = 0
    cur_h = health
    
    while len(atk_q) != 0:
        next_atk = atk_q[0]
        if time == next_atk[0]:
            cur_atk = atk_q.popleft()
            cur_h -= cur_atk[1]
            count = 0
            if cur_h <= 0:
                return -1
        else:
            cur_h += bandage[1]
            count += 1
            if count == bandage[0]:
                cur_h += bandage[2]
                count = 0
            cur_h = min(cur_h, health)
        
        time += 1
                
    return cur_h