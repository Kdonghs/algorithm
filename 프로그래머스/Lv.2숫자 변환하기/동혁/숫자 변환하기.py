def solution(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)

    while dp:
        if y in dp:
            return answer
        else:
            temp = set()
            for i in dp:
                if i + n <= y:
                    temp.add(i + n)
                if i * 2 <= y:
                    temp.add(i * 2)
                if i * 3 <= y:
                    temp.add(i * 3)
            dp = temp
            answer += 1
    return -1