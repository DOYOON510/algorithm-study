def solution(n, lost, reserve):
    all_lst=[1]*(n+2)
    for i in reserve:
        all_lst[i]+=1
    for i in lost:
        all_lst[i]-=1
    for i in range(1,n+1):
        if all_lst[i-1]==0 and all_lst[i]==2:
            all_lst[i-1:i+1]=1,1
        elif all_lst[i+1]==0 and all_lst[i]==2:
            all_lst[i:i+2]=1,1
    answer=len([x for x in all_lst[1:-1] if x > 0])
    return answer