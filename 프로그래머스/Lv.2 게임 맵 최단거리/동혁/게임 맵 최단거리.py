def solution(maps):
    goal=[len(maps),len(maps[0])]
    queue = [[0, 0, 1]]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        temp = queue.pop(0)

        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]

            if nx < 0 or ny < 0 or ny >= goal[0] or nx >= goal[1]:
                continue
            else:
                if maps[ny][nx] == 1 or maps[ny][nx] > temp[2] + 1:
                    maps[ny][nx] = temp[2] + 1
                    if ny == goal[0] - 1 and nx == goal[1] - 1:
                        return temp[2] + 1
                    queue.append([nx, ny, temp[2] + 1])
    return -1
