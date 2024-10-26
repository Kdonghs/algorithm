from collections import deque


def solution(board):
    def bfs(start):
        # 북,동,남,서 순서
        y = [-1, 0, 1, 0]
        x = [0, 1, 0, -1]

        length = len(board)
        visited = [[987654321] * length for _ in range(length)]
        visited[0][0] = 0

        q = deque([start])  # x, y, cost, dir
        while q:
            temp = q.popleft()
            for i in range(4):  # 북,동,남,서 순서
                nx = temp[0] + x[i]
                ny = temp[1] + y[i]

                # board 안에 있고, 벽이 아닌지 확인
                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:

                    # 비용계산
                    if i == temp[3]:
                        ncost = temp[2] + 100
                    else:
                        ncost = temp[2] + 600
                    # 최소 비용이면 갱신 후 endeque!
                    if ncost < visited[nx][ny]:
                        visited[nx][ny] = ncost
                        q.append([nx, ny, ncost, i])

        return visited[-1][-1]

    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])