def solution(n, k, cmd):
    answer = ['O'] * n
    delete = []  # 삭제된 행 기록
    index = k  # 현재 선택된 행
    table = {i: [i - 1, i + 1] for i in range(n)}  # 링크드 리스트

    for c in cmd:
        if c[0] == 'U':
            x = int(c.split()[1])
            for _ in range(x):
                index = table[index][0]  # 이전 행으로 이동
        elif c[0] == 'D':
            x = int(c.split()[1])
            for _ in range(x):
                index = table[index][1]  # 다음 행으로 이동
        elif c[0] == 'C':
            prev, next = table[index]
            delete.append((index, prev, next))  # 삭제된 행 기록
            answer[index] = 'X'  # 삭제 상태 표시

            if next == n:  # 마지막 행인 경우
                index = prev
            else:  # 마지막 행이 아닌 경우
                index = next

            # 링크드 리스트 갱신
            if prev != -1:
                table[prev][1] = next
            if next != n:
                table[next][0] = prev
        elif c[0] == 'Z':
            restore, prev, next = delete.pop()
            answer[restore] = 'O'  # 복구 상태 표시

            # 링크드 리스트 복구
            if prev != -1:
                table[prev][1] = restore
            if next != n:
                table[next][0] = restore

    return ''.join(answer)
