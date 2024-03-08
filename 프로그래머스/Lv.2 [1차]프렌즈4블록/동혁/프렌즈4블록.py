# 각 행을 역순으로 정렬하여 왼쪽으로 90도 회전
def rotate_90_degrees(matrix):
    # 행과 열을 바꾸기
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    rotated_matrix = [list(reversed(row)) for row in transposed_matrix]

    return rotated_matrix


def solution(m, n, board):
    answer = 0
    board = rotate_90_degrees(list(map(list, board)))

    while True:
        temp = []
        clear = False

        for i in range(n - 1):
            for j in range(m - 1):
                #                 4개가 같은지 검사
                #                 0은 빈공간이므로 건너뜀
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] and board[i][j] != '0':
                    #                    4개가 검사된 죄표 저장
                    temp.append([i, j])
                    #                    겹치는 캐릭터가 존재
                    clear = True

        if clear:
            for a in temp:
                i = a[0]
                j = a[1]

                board[i][j] = '0'
                board[i][j + 1] = '0'
                board[i + 1][j] = '0'
                board[i + 1][j + 1] = '0'

            for row in board:
                zero_indices = [i for i, x in enumerate(row) if x == '0']
                for zero_index in reversed(zero_indices):
                    row.pop(zero_index)
                    row.append('0')
            clear = False
        else:
            break

    for i in board:
        answer += i.count('0')
    return answer