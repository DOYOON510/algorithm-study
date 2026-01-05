def solution(n):
    if n%2==1:
        i=n//2
        return '수박'*i+'수'
    else:
        j=n//2
        return '수박'*j