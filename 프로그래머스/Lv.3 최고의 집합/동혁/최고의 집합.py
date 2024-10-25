def solution(n, s):
    if n > s:
        return [-1]

    answer = []
    value = s // n
    temp = s % n

    for i in range(n):
        if temp != 0:
            temp -= 1
            answer.append(value + 1)
        else:
            answer.append(value)

    answer.sort()
    return answer