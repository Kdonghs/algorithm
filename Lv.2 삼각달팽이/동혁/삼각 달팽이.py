def solution(n):
    answer = []
    all = 0
    li = [[0] * i for i in range(1, n + 1)]

    x, y = -1, 0
    num = 6

    for i in range(n):
        for j in range(n - i):

            # 아래로
            if num == 6:
                x += 1
            # 오른쪽
            elif num == 3:
                y += 1
            # 위로
            elif num == 12:
                x -= 1
                y -= 1
            all += 1
            li[x][y] = all

        if num == 6:
            num = 3
        elif num == 3:
            num = 12
        elif num == 12:
            num = 6

    return sum(li, [])


print(solution(4))
