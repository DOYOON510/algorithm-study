def solution(arr):
    answer=[]
    for i in arr:
        if i not in answer:
            answer.append(i)
        if i !=answer[-1]:
            answer.append(i)
    return answer