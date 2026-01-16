from collections import deque
n, m = map(int, input().split())
lst = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=0 and nx<n and ny>=0 and ny<m and lst[nx][ny]==1 :
                q.append((nx, ny))
                lst[nx][ny] = lst[x][y] + 1

    return lst[n-1][m-1]

print(bfs(0,0))