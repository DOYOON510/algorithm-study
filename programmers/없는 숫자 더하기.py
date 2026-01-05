def solution(numbers):
    # return sum(range(0,10))-sum(numbers)
    r=set(range(0,10))
    for i in range(1,10):
        if i in numbers:
            r.remove(i)
    return sum(r)