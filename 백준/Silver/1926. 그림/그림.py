from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    area = 0

    while q:
        x, y = q.popleft()
        area += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=0 and nx<n and ny>=0 and ny<m and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0

    return area

cnt = 0
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            ans = max(ans, bfs(i,j))


print(cnt)
print(ans)