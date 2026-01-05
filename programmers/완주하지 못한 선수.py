def solution(participant, completion):
    d={}
    for x in participant:
        d[x]=d.get(x,0)+1
    for x in completion:
        d[x]-=1
    answer=[x for x,y in d.items() if y>0]
    return answer[0]