def solution(s):
    ans = len(s)
    for i in range(1, int(len(s) / 2 + 1)):
        com = ''
        cnt = 1
        prev = s[:i]
        for j in range(i, len(s)+1, i):
            if prev == s[j:j + i]:
                cnt += 1
            else:
                if cnt > 1:
                    com += str(cnt) + prev
                else:
                    com += prev
                prev = s[j:j+i]
                cnt = 1
        if cnt > 1:
            com += str(cnt) + prev
        else:
            com += prev

        ans = min(ans, len(com))

    return ans
