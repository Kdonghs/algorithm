def solution(word):
    answer = 0

    result = ['A', 'E', 'I', 'O', 'U']
    queue = ['A', 'E', 'I', 'O', 'U']
    while queue:
        temp = queue.pop(0)
        # result.append(temp)
        if len(temp) < 5:
            result.append(temp + 'A')
            result.append(temp + 'E')
            result.append(temp + 'I')
            result.append(temp + 'O')
            result.append(temp + 'U')

            queue.append(temp + 'A')
            queue.append(temp + 'E')
            queue.append(temp + 'I')
            queue.append(temp + 'O')
            queue.append(temp + 'U')
    result.sort()
    # print(result)
    return result.index(word) + 1