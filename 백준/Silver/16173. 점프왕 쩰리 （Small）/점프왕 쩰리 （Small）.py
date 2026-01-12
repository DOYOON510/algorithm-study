from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = []
for _ in range(n):
    visited.append([False]*n)

dx = [0, 1]
dy = [1, 0]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        if graph[x][y] == -1:
            return 'HaruHaru'

        jump = graph[x][y]
        for i in range(2):
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump

            if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = True
    return 'Hing'

print(bfs(0,0))