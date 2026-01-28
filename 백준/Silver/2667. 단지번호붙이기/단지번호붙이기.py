from collections import deque

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

    return cnt


ans = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(bfs(i, j))

print(len(ans))

ans.sort()
for i in ans:
    print(i)
