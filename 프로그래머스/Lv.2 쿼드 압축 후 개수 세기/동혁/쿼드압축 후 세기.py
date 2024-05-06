def fourth(arr):
    answer = []

    a = arr[:len(arr) // 2]
    b = arr[len(arr) // 2:]

    temp = []
    for i in a:
        temp.append(i[:len(a[0]) // 2])

    answer.append(temp)
    temp = []
    for i in a:
        temp.append(i[len(a[0]) // 2:])

    answer.append(temp)
    temp = []
    for i in b:
        temp.append(i[:len(b[0]) // 2])

    answer.append(temp)
    temp = []
    for i in b:
        temp.append(i[len(b[0]) // 2:])

    answer.append(temp)

    return answer


def match(arr):
    num = arr[0][0]

    for i in arr:
        for j in i:
            if num != j:
                return -1
    return num


def solution(arr):
    zero = 0
    one = 0
    queue = [arr]

    a = match(arr)
    if a != -1:
        if a == 0:
            return [1, 0]
        else:
            return [0, 1]

    while queue:
        temp = fourth(queue.pop(0))

        for i in temp:
            if len(i) == 1:
                if i[0][0] == 0:
                    zero += 1
                elif i[0][0] == 1:
                    one += 1
            else:
                num = match(i)
                if num == -1:
                    queue.append(i)
                    continue
                elif num == 0:
                    zero += 1
                elif num == 1:
                    one += 1
    return [zero, one]